# Playing around with OOP for linear regression in activity measurements 220409
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress as linreg


def estimate(abs, slope, intercept):
    """
    calculates the concentration from absorbance using slope and intercept from standard data, corrects for dilution factor as well.

    y   = x * slope + intercept -> x = (y - intercept) / slope

    abs = c * slope + intercept -> c = (abs - intercept) / slope
    """
    return (abs - intercept) / slope


class Absorbance:
    """
    Parent class that allows numpy arrays of absorbance data with absorbance mean and std

    INPUT:
        abs is the absorbance values that were measured in each cuvette ordered in a numpy array (matrix-like), default is that the each column is a unique experiment and each row of that column is the amount of replicates.

        shape is a modifier to how the numpy array is read, rows switches experiments and replicates instead.

    OUTPUT:
        calculates mean absorbance and its standards deviation as self.mean and self.std
    """

    def __init__(
        self,
        absorbance: np.ndarray,  # array of abs values
        shape: str = "columns",  # orientation of values vs. replicates.
    ) -> None:
        self.abs = absorbance

        if shape == "columns" or "Columns" or "col":
            self.mean = np.mean(self.abs, axis=0)
            self.std = np.std(self.abs, axis=0)

        elif shape == "rows" or "Rows":
            self.mean = np.mean(self.abs, axis=1)
            self.std = abs(np.std(self.abs, axis=1))

        else:
            print("please enter either 'columns' or 'rows' for the shape.")


class Standard(Absorbance):
    """
    child Class for std data. Provides method for fitting, plotting and showing data.

    input:
        absorbance: numpy array of your absorbance data, default is experiments in rows, replicates in col.

        concentration: numpy array of your known std concentration

        x_unit: str of the unit of concentration

        y_unit: str of unit for signal, default is absorbance.

        shape: modifies the order of experiments and replicates.

        self.fit is a regression object (see scipy -> linreg for further details)

    output:
        printing the class shows matrix of data

        "plot()" function creates a pyplot object of the data
    """

    def __init__(
        self,
        absorbance: np.ndarray,  # array of abs values
        concentration=np.ndarray,  # array of known concentration
        x_unit: str = None,  # unit of concentrations, i.e [mM]
        y_unit: str = "AU",  # unit of absorbance
        shape: str = "columns",  # orientation of data array
    ) -> None:
        super().__init__(absorbance, shape)

        self.c = concentration
        self.fit = linreg(self.c, self.mean)
        self.x_unit = x_unit
        self.y_unit = y_unit

    def __repr__(self):

        # generate a dataframe of mean abs and std for abs
        df = pd.DataFrame(
            {
                self.x_unit: self.c,
                f"mean [{self.y_unit}]": self.mean,
                f"+/- [{self.y_unit}]": self.std,
            }
        )

        # insert columns of replicate data into dataframe
        for i, _ in enumerate(self.abs):
            df.insert(i + 1, f"abs #{i+1}", self.abs[i, :])

        return f"Standard Data: \n {df}  \n\nResulting std equation is:\n\n    abs = c * {self.fit.slope:.2f} + {self.fit.intercept:.2f}\n\nWith an R^2 of {self.fit.rvalue**2:.4f}"

    def plot(self):
        """
        create the plot object of the standard curve
        """

        # data points
        plt.errorbar(
            self.c,
            self.mean,
            self.std,
            fmt="*-",
            color="black",
            linewidth=1,
            capsize=3,
            label="std data",
        )

        # regression line
        plt.plot(
            self.c,
            self.c * self.fit.slope + self.fit.intercept,
            color="green",
            linestyle="--",
            linewidth=1,
            label=f"Fit: abs = {self.fit.slope:0.2f} * c + {self.fit.intercept:0.2f}",
        )
        plt.grid(True)
        plt.xlabel(f"Concentration [{self.x_unit}]")
        plt.ylabel(f"Absorbance [{self.y_unit}]")
        plt.legend()
        plt.title(f"Standard Curve - {str(date.today())}")


class Enzyme(Absorbance):
    """
    child Class for sample data, allows for calculation of concentration and activity based on std data.

    input:
    absorbance: numpy array of your absorbance data, default is experiments in rows, replicates in col.
    Name: str of experiment name
    dilution_factor: numpy array of the dilution factors of each experiment.
    time: time in [min]
    x_unit: str of the unit of concentration
    y_unit: str of unit for signal, default is absorbance.
    shape: modifies the order of experiments and replicates.

    concentration: numpy array of estimated concentrations.

    output:
    printing the class shows matrix of data
    "plot()" function creates a pyplot object of the data

    """

    def __init__(
        self,
        absorbance: np.ndarray,
        Name: str,
        regr,
        time: list[float],
        dilution_factor: np.ndarray = 1,
        enzyme_stock_conc: float = None,
        x_unit: str = None,
        y_unit: str = "AU",
        shape: str = "columns",
    ) -> None:
        super().__init__(absorbance, shape)

        self.abs = absorbance
        self.name = Name
        self.regr = regr
        self.x_unit = x_unit
        self.y_unit = y_unit
        self.dil = dilution_factor
        self.stock_conc = enzyme_stock_conc
        self.time = time

        # concentration of analyte in cuvette
        self.c = estimate(
            abs=self.mean, slope=self.regr.slope, intercept=self.regr.intercept
        )
        self.c_std = abs(
            estimate(abs=self.std, slope=self.regr.slope, intercept=self.regr.intercept)
        )

        # calculate activity in nkat/ml based on unit in "x_unit"
        if self.x_unit == "nM":
            # [nM] / 1000_000_000 [M/nM] * 1000_000_000 [nM/M] /1000 [l/ml] / 600 [1/s] = nmol/ml/s = nkat/ml
            self.activity = self.c / 1000 / 600 * self.dil
            self.activity_std = self.c_std / 1000 / 600 * self.dil

        elif self.x_unit == "μM" or self.x_unit == "uM":
            # [uM] / 1000_000 [M/uM] * 1000_000_000 [nM/M] /1000 [l/ml] / 600 [1/s] = nmol/ml/s = nkat/ml
            self.activity = self.c * 1 / 600 * self.dil
            self.activity_std = self.c_std * 1 / 600 * self.dil

        elif self.x_unit == "mM":
            # [mM] / 1000 [M/mM] * 1000_000_000 [nM/M] /1000 [l/ml] / 600 [1/s] = nmol/ml/s = nkat/ml
            self.activity = self.c * 1_000 / 600 * self.dil
            self.activity_std = self.c_std * 1_000 / 600 * self.dil

        elif self.x_unit == "M":
            # [M] * 1000_000_000 [nM/M] /1000 [l/ml] / 600 [1/s] = nmol/ml/s = nkat/ml
            self.activity = self.c * 1_000_000 / 600 * self.dil
            self.activity_std = self.c_std * 1_000_000 / 600 * self.dil

        else:
            print("Wrong unit for X-values, needs to be [nM],[μM],[mM], or [M]")
            raise NotImplementedError

        # create dataframe of all data for presentation
        self.df = pd.DataFrame(
            {
                f"mean [{self.y_unit}]": self.mean,
                f"+/- [{self.y_unit}]": self.std,
                f"conc. analyte [{self.x_unit}]": self.c,
                f"+/- [{self.x_unit}]": self.c_std,
                "activity [nkat/ml]": self.activity,
                "+/- [nkat/ml]": self.activity_std,
            },
            index=pd.Index([self.name]),
        )

        # calculate specific activity if there is a protein stock conc. entered.
        if enzyme_stock_conc and self.activity:
            # requires that the stock conc. if in mg/ml and the activity is in stock nkat/ml.
            self.specific_activity = self.activity / self.stock_conc
            self.specific_activity_std = self.activity_std / self.stock_conc

            # adds it to the dataframe
            self.df["spec. activity [nkat/mg]"] = self.specific_activity
            self.df["+/- [nkat/mg]"] = self.specific_activity_std

        # insert raw replicate data depending on how many replicates
        for i, _ in enumerate(self.abs):
            self.df.insert(i, f"abs #{i+1}", self.abs[i, :])

    # if Enzyme class is printed, it returns the dataframe table
    def __repr__(self):
        return f"{self.name}: \n {self.df}"

    # function for plotting the data points.
    def plot(self) -> None:
        """
        Create the plot object of the sample data.
        """

        # data points for sample.
        plt.errorbar(
            self.c,
            self.mean,
            self.std,
            fmt="*",
            linewidth=1,
            capsize=3,
            label=self.name,
        )
        plt.grid(True)
        plt.xlabel(f"concentration [{self.x_unit}]")
        plt.ylabel(f"Absorbance [{self.y_unit}]")
        plt.title(f"Standard Curve - {str(date.today())}")
        plt.legend()


def main():
    """
    executable part of script.
    """

    # initilazing class of example data
    std = Standard(
        absorbance=(np.array([1, 4, 6, 8, 10, 15, 20, 25]) + np.random.rand(3, 8)) * 4
        + 6,
        concentration=np.array([1, 4, 6, 8, 10, 15, 20, 25]),
        x_unit="mM",
        y_unit="AU",
    )

    # initilazing class of example data
    TrMan5A = Enzyme(
        Name=" TrMan5A 10x Dil, 1h",
        absorbance=[15, 12, 16] + np.random.rand(3, 1) * 4 + 3,
        regr=std.fit,
        dilution_factor=10,
        time=60.0,
        x_unit=std.x_unit,
        y_unit=std.y_unit,
    )

    # shows the data in matrix form
    print(std)
    print(TrMan5A)

    # shows the data in plot window
    TrMan5A.plot()
    std.plot()
    plt.show()


if __name__ == "__main__":
    main()
