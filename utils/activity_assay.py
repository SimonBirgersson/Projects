# Playing around with OOP for linear regression in activity measurements 220409
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress as linreg


def estimate(abs, slope, intercept):
    """calculates the concentration from absorbance using slope and intercept from standard data, corrects for dilution factor as well."""
    return (abs - intercept) / slope


class Absorbance:
    """
    Parent class that allows numpy arrays or absorbance data
    """

    def __init__(
        self,
        absorbance: np.ndarray,
        shape: str = "columns",
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
    Class for std data. Provides method for fitting, plotting and showing data.
    """

    def __init__(
        self,
        absorbance: np.ndarray,
        concentration=np.ndarray,
        x_unit: str = None,
        y_unit: str = "AU",
        shape: str = "columns",
    ) -> None:
        super().__init__(absorbance, shape)

        self.c = concentration
        self.fit = linreg(self.c, self.mean)
        self.x_unit = x_unit
        self.y_unit = y_unit

    def show(self):
        """
        shows the data in a pandas table
        """
        print("Standard Data:")
        print(
            pd.DataFrame(
                {
                    self.x_unit: self.c,
                    f"mean [{self.y_unit}]": self.mean,
                    f"+/- [{self.y_unit}]": self.std,
                }
            )
        )

    def plot(self):
        """
        shows the plot of the standard curve
        """
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
        plt.plot(
            range(self.c[-1]),
            range(self.c[-1]) * self.fit.slope + self.fit.intercept,
            color="green",
            linewidth=1,
            label=f"fit abs = {self.fit.slope:0.2f} * c + {self.fit.intercept:0.2f}",
        )
        plt.grid(True)
        plt.xlabel(self.x_unit)
        plt.ylabel(self.y_unit)
        plt.legend()
        plt.title(f"Standard Curve - {str(date.today())}")


class Enzyme(Absorbance):
    """
    Class for sample data
    """

    def __init__(
        self,
        absorbance: np.ndarray,
        Name: str,
        regr,
        dilution_factor: np.ndarray = 1,
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
        self.c = estimate(
            abs=self.mean, slope=self.regr.slope, intercept=self.regr.intercept
        )
        self.c_std = abs(
            estimate(abs=self.std, slope=self.regr.slope, intercept=self.regr.intercept)
        )

    def __repr__(self):
        df = pd.DataFrame(
            {
                f"mean [{self.y_unit}]": self.mean,
                f"+/- [{self.y_unit}]": self.std,
                f"c [{self.x_unit}]": self.c,
                f"+/- [{self.x_unit}]": self.c_std,
            }
        )

        return f"{self.name}: \n {df}"

    def plot(self) -> None:
        """
        shows the plot of the standard curve
        """
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
    std = Standard(
        absorbance=(np.array([1, 4, 6, 8, 10, 15, 20, 25]) + np.random.rand(3, 8)) * 4
        + 6,
        concentration=np.array([1, 4, 6, 8, 10, 15, 20, 25]),
        x_unit="mM",
        shape="columns",
    )

    TrMan5A = Enzyme(
        Name="10x Dil, 1h",
        absorbance=[15, 12, 16] + np.random.rand(3, 1) * 4 + 3,
        regr=std.fit,
        dilution_factor=10,
        x_unit=std.x_unit,
        y_unit=std.y_unit,
        shape="col",
    )

    print(TrMan5A)


if __name__ == "__main__":
    main()
