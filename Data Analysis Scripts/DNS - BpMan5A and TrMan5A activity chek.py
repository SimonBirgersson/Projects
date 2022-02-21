# DNS - BpMan5A and TrMan5A activity check 220217
from datetime import date
from statistics import mean

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import linregress as linreg


# Function to utilize later for calculation of concentration
def func(data, slope, intercept):
    """calculates the concentration from absorbance "x" using "k" and "m" from linreg."""
    conc = (data - intercept) / slope
    return conc


# function for linreg unit analysis etc.
def calculate(
    std,
    data,
    samplename=0,
    protein_concentration=0,
    dilution=1,
):
    """Input: \n
    Dataframe of std data with column 1 as dependent variable (conc, in mM), and the rest of columns being replicates of absorbance values, ex) column 2 is "abs #1" column 2 is "abs #2".

    Data frame with sample data  in the same fashion minus the first column.

    List of names of each sample, will be rownames in final dataframe

    "Protein_concentration" is optional for adding specific activity to to the dataframe, use unit mg and stock protein concentration

    "dilution" is optional for getting the values for the protein stock, use total dilution factor from measured sample to stock

    Output: \n
    Returns the same dataframe as added in "data" with new columns for concentration, and activity"""

    # calculate average and std for std absorbances
    std["avg abs"] = std.iloc[:, 1:].mean(axis=1)
    std["+/- abs"] = std.iloc[:, 1:].std(axis=1)

    # Fits the data into a linear regression class
    regr = linreg(std.iloc[:, 0], std["avg abs"])

    # calculate mean and stdev for sample data
    data["avg abs"] = data.iloc[:, 1:].mean(axis=1)
    data["+/- abs"] = data.iloc[:, 1:].std(axis=1)

    # Predicts concentrations of sample points
    data[["conc. [mM]", "+/- mM"]] = (
        data[["avg abs", "+/- abs"]]
        .apply(lambda x: func(x, regr.slope, regr.intercept))
        .multiply(dilution, axis="index")
    )

    # multiply by dilution factor
    if dilution == 1:
        pass
    else:
        try:
            data[["conc. [mM]", "+/- mM"]] = data[["conc. [mM]", "+/- mM"]].multiply(
                dilution, axis="index"
            )

        except:
            print("\n Beep! some problem with dilution, maybe too few elements in list")

    # unit conversion to activity
    data[["[nkat/ml]", "+/- nkat/ml"]] = data[["conc. [mM]", "+/- mM"]].apply(
        lambda x: x * 10**3 / 600
    )

    # if protein concentration is in calculate specific activity
    if protein_concentration == 0:
        pass
    elif protein_concentration != 0:
        data[["[nkat/mg]", "+/- nkat/mg"]] = data[["[nkat/ml]", "+/- nkat/ml"]].apply(
            lambda x: x / protein_concentration
        )

    # change row names to "samplename"
    if samplename == 0:
        pass
    elif isinstance(samplename, list):
        try:
            data.index = samplename
        except:
            print(
                "\n Beep! sample name doesn't work in calculate, maybe to few row names..."
            )

    # Prints the functions from the linear regression
    print("\nFitted equation is: abs = %.3f * c + %.3f" % (regr.slope, regr.intercept))

    # The coefficient of determination R2: 1 is perfect prediction
    print("\nCoefficient of determination (R2): %.4f" % regr.rvalue)

    return data, regr.slope, regr.intercept


# --------------------------------------------------------------------------------------------------------
# standard data
std_1 = pd.DataFrame(
    {
        "Conc. M1 [mM]": [5, 10, 20, 40, 50],
        "abs #1": [x - 0.123 for x in [0.148, 0.299, 0.667, 1.382, 1.767]],
        "abs #2": [x - 0.124 for x in [0.154, 0.307, 0.668, 1.349, 1.675]],
    }
)


data_1 = pd.DataFrame(
    {
        "abs #1": [
            x - mean([0.129, 0.128])
            for x in [1.279, 0.145, 0.129, 0.132, 1.483, 0.162, 0.127, 0.131]
        ],
        "abs #2": [
            x - mean([0.129, 0.128])
            for x in [1.392, 0.142, 0.129, 0.132, 1.258, 0.152, 0.128, 0.130]
        ],
        "abs #3": [
            x - mean([0.129, 0.128])
            for x in [1.305, 0.146, 0.128, 0.130, 1.161, 0.151, 0.128, 0.129]
        ],
    }
)

data_1, k1, m1 = calculate(
    std=std_1,
    data=data_1,
    samplename=[
        "BpMan5A 1 1x",
        "BpMan5A 1 10x",
        "BpMan5A 1 50x",
        "BpMan5A 1 100x",
        "TrMan5A 1 1x",
        "TrMan5A 1 10x",
        "TrMan5A 1 50x",
        "TrMan5A 1 100x",
    ],
)
# dilution=[1, 10, 50, 100, 1, 10, 50, 100]
print("\nBpMan5A and TrMan5A at 65°C:")
print(data_1)
# --------------------------------------------------------------------------------------------------------
# standard data
std_2 = pd.DataFrame(
    {
        "Conc. M1 [mM]": [5, 10, 20, 40, 50],
        "abs #1": [x - 0.109 for x in [0.171, 0.326, 0.711, 1.390, 1.837]],
        "abs #2": [x - 0.114 for x in [0.164, 0.325, 0.697, 1.393, 1.722]],
    }
)

data_2 = pd.DataFrame(
    {
        "abs #1": [
            x - mean([0.129, 0.128])
            for x in [1.795, 0.226, 0.112, 0.115, 1.848, 0.490, 0.130, 0.136]
        ],
        "abs #2": [
            x - mean([0.129, 0.128])
            for x in [1.767, 0.185, 0.119, 0.117, 1.826, 0.534, 0.129, 0.135]
        ],
        "abs #3": [
            x - mean([0.129, 0.128])
            for x in [1.859, 0.210, 0.115, 0.107, 1.687, 0.524, 0.131, 0.136]
        ],
    }
)

data_2, k2, m2 = calculate(
    std_2,
    data_2,
    [
        "BpMan5A 1 1x",
        "BpMan5A 1 10x",
        "BpMan5A 1 50x",
        "BpMan5A 1 100x",
        "TrMan5A 1 1x",
        "TrMan5A 1 10x",
        "TrMan5A 1 50x",
        "TrMan5A 1 100x",
    ],
)
print("\nBpMan5A and TrMan5A at 40°C:")
print(data_2)

# --------------------------------------------------------------------------------------------------------
plt.figure(figsize=(8, 4), tight_layout=True)


with sns.axes_style("whitegrid"):
    # plot std points
    plt.errorbar(
        std_1["Conc. M1 [mM]"],
        std_1["avg abs"],
        std_1["+/- abs"],
        linewidth=1.0,
        label="standard points 65°C",
        marker="o",
        linestyle="none",
        capsize=2,
    )

    # plot linear regression
    plt.plot(
        np.linspace(5, 50),
        k1 * np.linspace(5, 50) + m1,
        linewidth=1.0,
        label="linear fit 65°C",
        linestyle="-",
    )

    # plot std points
    plt.errorbar(
        std_2["Conc. M1 [mM]"],
        std_2["avg abs"],
        std_2["+/- abs"],
        linewidth=1.0,
        label="standard points 40°C",
        marker="o",
        linestyle="none",
        capsize=2,
    )

    # plot linear regression
    plt.plot(
        np.linspace(5, 50),
        k2 * np.linspace(5, 50) + m2,
        linewidth=1.0,
        label="linear fit 40°C",
        linestyle="-",
    )
    # Plot BpMan5A 1 65°C points
    plt.errorbar(
        data_1["conc. [mM]"].iloc[:4],
        data_1["avg abs"].iloc[:4],
        data_1["+/- abs"].iloc[:4],
        linewidth=1.0,
        label="BpMan5A 1 65°C",
        marker="o",
        linestyle="none",
        capsize=2,
    )
    # Plot BpMan5A 1  65°C points
    plt.errorbar(
        data_1["conc. [mM]"].iloc[4:],
        data_1["avg abs"].iloc[4:],
        data_1["+/- abs"].iloc[4:],
        linewidth=1.0,
        label="BpMan5A 2 65°C",
        marker="o",
        linestyle="none",
        capsize=2,
    )
    # Plot BpMan5A  40°C points
    plt.errorbar(
        data_2["conc. [mM]"].iloc[:4],
        data_2["avg abs"].iloc[:4],
        data_2["+/- abs"].iloc[:4],
        linewidth=1.0,
        label="BpMan5A 1 40°C",
        marker="o",
        linestyle="none",
        capsize=2,
    )
    # Plot TrMan5A 40°C points
    plt.errorbar(
        data_2["conc. [mM]"].iloc[4:],
        data_2["avg abs"].iloc[4:],
        data_2["+/- abs"].iloc[4:],
        linewidth=1.0,
        label="TrMan5A 1 40°C",
        marker="o",
        linestyle="none",
        capsize=2,
    )

plt.legend(title="data:")
plt.title("DNS assay results - %s" % date.today())
plt.xlabel("concentration of reduced ends [mM]")
plt.ylabel("Absorbance (540nm)")
# plt.show()
