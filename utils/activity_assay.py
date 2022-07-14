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


# Class for standard data storage and calc
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

        # generate a dataframe of mean abs and std for abs
        self.df = pd.DataFrame(
            {
                self.x_unit: self.c,
                f"mean [{self.y_unit}]": self.mean,
                f"+/- [{self.y_unit}]": self.std,
            }
        )

        # insert columns of replicate data into dataframe
        for i, _ in enumerate(self.abs):
            self.df.insert(i + 1, f"abs #{i+1}", self.abs[i, :])

    def __repr__(self):

        return f"Standard Data: \n {self.df}  \n\nResulting std equation is:\n\n    abs = c * {self.fit.slope:.2f} + {self.fit.intercept:.2f}\n\nWith an R^2 of {self.fit.rvalue**2:.4f}"

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


# Class for sample data storage and calc
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
        self.time = time

        # concentration of analyte in cuvette
        self.c = estimate(
            abs=self.mean, slope=self.regr.slope, intercept=self.regr.intercept
        )
        self.c_std = abs(
            estimate(abs=self.std, slope=self.regr.slope, intercept=self.regr.intercept)
        )

        # concentration factor concentration unit -> nM
        c_conversion_factor = {
            "nM": 1,  # nM/nM = 1
            "μM": 1000,  # nM/uM = 1000
            "uM": 1000,  # nM/uM = 1000
            "mM": 1000_000,  # nM/mM = 1000_000
            "M": 1000_000_000,  # nM/M = 1000_000_000
        }

        try:
            self.activity = (
                self.c  # calculated concentration from std curve
                * c_conversion_factor[
                    self.x_unit
                ]  # unit conversion factor depending concentration prefix
                / 1000  # L/ml = 10^-3
                / (self.time * 60)  # enzyme reaction time in minutes  # s/min
                * self.dil  # account for reaction dilution factor
            )
            print(len(self.activity))

            self.activity_std = (
                self.c_std  # calculated concentration from std curve
                * c_conversion_factor[
                    self.x_unit
                ]  # unit conversion factor depending concentration prefix
                / 1000  # L/ml = 10^-3
                / (self.time * 60)  # enzyme reaction time in minutes  # s/min
                * self.dil  # account for reaction dilution factor
            )

        except:
            print("Wrong unit for X-values, needs to be [nM],[μM],[mM], or [M]")

        # create dataframe of all data for presentation
        self.df = pd.DataFrame(
            {
                f"mean [{self.y_unit}]": self.mean,  # mean absorbance
                f"+/- [{self.y_unit}]": self.std,  # std absorbance
                f"conc. analyte [{self.x_unit}]": self.c,  # calc. conc.
                f"+/- [{self.x_unit}]": self.c_std,  # std conc.
                "conc [nM]": self.c * c_conversion_factor[self.x_unit],  # conc in nM
                "+/- [nM]": self.c_std
                * c_conversion_factor[self.x_unit],  # std conc in nM
                "conc [nmol/ml]": self.c * c_conversion_factor[self.x_unit] / 1000,
                "+/- [nmol/ml]": self.c_std * c_conversion_factor[self.x_unit] / 1000,
                "activity in assay [nkat/ml]": self.c
                * c_conversion_factor[self.x_unit]
                / 1000
                / (self.time * 60),
                "+/- in assay [nkat/ml]": self.c_std
                * c_conversion_factor[self.x_unit]
                / 1000
                / (self.time * 60),
                "activity [nkat/ml]": self.activity,  # calc. activity
                "+/- [nkat/ml]": self.activity_std,  # std activity
            },
            index=pd.Index([self.name]),  # index is experiment name
        )

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
            self.c,  # x-values is concentration
            self.mean,  # y-value is mean abs
            self.std,  # errorbar i std abs
            fmt="*",  # dots
            linewidth=1,  # linewidth of the errorbar
            capsize=3,  # size of the "T" on the errorbars
            label=self.name,  # add legend
        )
        plt.grid(True)
        plt.xlabel(f"concentration [{self.x_unit}]")
        plt.ylabel(f"Absorbance [{self.y_unit}]")
        plt.title(f"Standard Curve - {str(date.today())}")
        plt.legend()


"""
def compile_experiments(
    experiments: list[Enzyme], enzyme_stock_conc: float = None, enzyme_mw: float = None
):
    ""get a table of all experiments for export, calc. specific activity""

    # generate empty dataframe
    df = pd.DataFrame([])

    # enter each experiment data into dataframe
    for experiment in experiments:
        df[experiment.name] = experiment.T

    # calculate specific activity if there is a protein stock conc. entered.
    if enzyme_stock_conc:
        # requires that the stock conc. if in mg/ml and the activity is in stock nkat/ml.
        df.loc["spec. activity [nkat/mg]"] = (
            df.loc["activity [nkat/ml]"] / enzyme_stock_conc
        )
        df.loc["+/- [nkat/mg]"] = df.loc["+/- [nkat/ml]"] / enzyme_stock_conc

        # U/mg = umol/min/mg -> nmol/s/mg * 10^3 * 60 s/min = umol/min/mg
        df.loc["spec. activity [unit/mg]"] = (
            df.loc["spec. activity [nkat/mg]"] * 10**-3 * 60
        )
        df.loc["+/- [unit/mg]"] = df.loc["+/- [nkat/mg]"] * 10**-3 * 60

        # if enzyme molecular weight is addded, calc. spec activity
        if enzyme_mw:
            # kat/mol -> nmol/s/mg * 10^-9 [M/nM] * 10^3 [mg/g] * [g/mol] = kat/mol
            df.loc["spec. activity [kat/mol]"] = (
                df.loc["spec. activity [nkat/mg]"] * 10**-6 * enzyme_mw
            )
            df.loc["+/- [kat/mol]"] = df.loc["+/- [nkat/mg]"] * 10**-6 * enzyme_mw

    return df
"""


def generate_excel_report(
    exp_dfs: list[pd.DataFrame],
    std_dfs: list[pd.DataFrame],
    path: str,
    filename: str,
    notes: list[str] = None,
):
    """Print thoroughly made excel report with line of text describing each math operation."""

    notes_df = pd.DataFrame({"notes": notes})

    exp_dfs.append(notes_df.T)

    with pd.ExcelWriter(
        f"{path}{filename}.xlsx",
        engine="xlsxwriter",
    ) as writer:  # pylint: disable=abstract-class-instantiated

        # write all experiment data in sheet 1 with notes
        start_col = 0  # start to the leftmost side in the sheet
        for i, exp in enumerate(exp_dfs):  # assuming they're already DataFrames

            # only included indices (units) for first df
            if i == 0:
                ind = True
            else:
                ind = False

            # write df to excel
            exp.T.to_excel(
                writer, "sample raw data & calculation", startcol=start_col, index=ind
            )

            # where to place the next one
            if i == 0:
                start_col += len(exp.T.columns) + 1  # add a col for the column header?
            else:
                start_col += len(exp.T.columns)  # add a col for the column header?

        # write std data in seperate sheets with notes
        for i, std in enumerate(std_dfs):
            # write df to excel
            std.to_excel(writer, f"std {i+1}", startcol=0, startrow=1, index=False)


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
    std.plot()

    # initilazing class of example data
    TrMan5A = Enzyme(
        Name=" TrMan5A 10x Dil, 1h",
        absorbance=[15, 15.5, 16] + np.random.rand(3, 1) * 4 + 3,
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

    plt.show()


if __name__ == "__main__":
    main()
