# DNS - raffinose and stachyose evaluation
from datetime import date
from statistics import mean

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from activity_assay import calculate

# ---------------------------------------------------------------------------------------------------
# standard data
std_LBG = pd.DataFrame(
    {
        "Conc. M1 [mM]": [5, 10, 20, 40, 50],
        "abs #1": [x - 0.100 for x in [0.148, 0.315, 0.693, 1.440, 1.846]],
        "abs #2": [x - 0.103 for x in [0.148, 0.310, 0.644, 1.457, 1.716]],
    }
)
std_raff = pd.DataFrame(
    {
        "Conc. M1 [mM]": [5, 10, 20, 40, 50],
        "abs #1": [x - 0.172 for x in [0.364, 0.559, 0.947, 1.721, 2.056]],
        "abs #2": [x - 0.171 for x in [0.370, 0.557, 0.963, 1.709, 2.013]],
    }
)
std_stach = pd.DataFrame(
    {
        "Conc. M1 [mM]": [5, 10, 20, 40, 50],
        "abs #1": [x - 0.159 for x in [0.339, 0.521, 0.904, 1.649, 2.040]],
        "abs #2": [x - 0.165 for x in [0.331, 0.517, 0.914, 1.688, 2.061]],
    }
)

# Sample data LBG
data_LBG = pd.DataFrame(
    {
        "abs #1": [x - mean([0.119, 0.115]) for x in [0.681]],
        "abs #2": [x - mean([0.119, 0.115]) for x in [0.703]],
    }
)
# Sample data Raff
data_raff = pd.DataFrame(
    {
        "abs #1": [
            x - mean([0.204, 0.203])
            for x in [
                0.149,
                0.740,
                0.270,
                0.191,
                0.179,
                0.722,
                0.276,
                0.189,
            ]
        ],
        "abs #2": [
            x - mean([0.204, 0.205])
            for x in [
                0.149,
                0.740,
                0.270,
                0.191,
                0.173,
                0.704,
                0.317,
                0.188,
            ]
        ],
    }
)
# Sample data Stachyose
data_stach = pd.DataFrame(
    {
        "abs #1": [
            x - mean([0.176, 0.179])
            for x in [
                0.141,
                0.208,
                0.172,
                0.161,
                0.202,
                0.213,
                0.180,
                0.165,
            ]
        ],
        "abs #2": [
            x - mean([0.177, 0.172])
            for x in [
                0.126,
                0.214,
                0.176,
                0.168,
                0.191,
                0.212,
                0.1770,
                0.155,
            ]
        ],
    }
)

# ---------------------------------------------------------------------------------------------------
# calculate concentration and activity for LBG
data_LBG, k_LBG, m_LBG = calculate(
    std=std_LBG,
    data=data_LBG,
    samplename=["Aga27A 1 10x + 4.5% w/v% l.v LBG"],
)
# calculate concentration and activity for raffinose
data_raff, k_raff, m_raff = calculate(
    std=std_raff,
    data=data_raff,
    samplename=[
        "Aga27A 1 1x +  225 mM Raffinose",
        "Aga27A 1 10x +  225 mM Raffinose",
        "Aga27A 1 50x +  225 mM Raffinose",
        "Aga27A 1 100x +  225 mM Raffinose",
        "Aga27A 2 1x +  225 mM Raffinose",
        "Aga27A 2 10x +  225 mM Raffinose",
        "Aga27A 2 50x +  225 mM Raffinose",
        "Aga27A 2 100x +  225 mM Raffinose",
    ],
)
# calculate concentration and activity for stachyose
data_stach, k_stach, m_stach = calculate(
    std=std_stach,
    data=data_stach,
    samplename=[
        "Aga27A 1 1x +  225 mM Stachyose",
        "Aga27A 1 10x +  225 mM Stachyose",
        "Aga27A 1 50x +  225 mM Stachyose",
        "Aga27A 1 100x +  225 mM Stachyose",
        "Aga27A 2 1x +  225 mM Stachyose",
        "Aga27A 2 10x +  225 mM Stachyose",
        "Aga27A 2 50x +  225 mM Stachyose",
        "Aga27A 2 100x +  225 mM Stachyose",
    ],
)
# dilution=[1, 10, 50, 100, 1, 10, 50, 100]
print("\n Aga27A + LBG at 40°C:")
print(data_LBG)
print("\n Aga27A + raffinose at 40°C:")
print(data_raff)
print("\n Aga27A + stachyose at 40°C:")
print(data_stach)


# ---------------------------------------------------------------------------------------------------
plt.figure(figsize=(8, 4), tight_layout=True)

with sns.axes_style("whitegrid"):
    # plot std points LBG
    plt.errorbar(
        std_LBG["Conc. M1 [mM]"],
        std_LBG["avg abs"],
        std_LBG["+/- abs"],
        linewidth=1.0,
        label="standard points LBG",
        marker="o",
        linestyle="none",
        capsize=2,
    )

    # plot linear regression LBG
    plt.plot(
        np.linspace(5, 50),
        k_LBG * np.linspace(5, 50) + m_LBG,
        linewidth=1.0,
        label="linear fit LBG",
        linestyle="-",
    )

    # plot std points raffinose
    plt.errorbar(
        std_raff["Conc. M1 [mM]"],
        std_raff["avg abs"],
        std_raff["+/- abs"],
        linewidth=1.0,
        label="standard points raffinose",
        marker="o",
        linestyle="none",
        capsize=2,
    )

    # plot linear regression raffinose
    plt.plot(
        np.linspace(5, 50),
        k_raff * np.linspace(5, 50) + m_raff,
        linewidth=1.0,
        label="linear fit raffinose",
        linestyle="-",
    )
    # plot std points stachyose
    plt.errorbar(
        std_stach["Conc. M1 [mM]"],
        std_stach["avg abs"],
        std_stach["+/- abs"],
        linewidth=1.0,
        label="standard points stachyose",
        marker="o",
        linestyle="none",
        capsize=2,
    )

    # plot linear regression stachyose
    plt.plot(
        np.linspace(5, 50),
        k_stach * np.linspace(5, 50) + m_stach,
        linewidth=1.0,
        label="linear fit stachyose",
        linestyle="-",
    )
    # Plot Aga27A 1 Raffinose points
    plt.errorbar(
        data_raff["conc. [mM]"].iloc[:4],
        data_raff["avg abs"].iloc[:4],
        data_raff["+/- abs"].iloc[:4],
        linewidth=1.0,
        label="Aga27A 1 + Raffinose",
        marker="o",
        linestyle="none",
        capsize=2,
    )
    # Plot Aga27A 2 Raffinose points
    plt.errorbar(
        data_raff["conc. [mM]"].iloc[4:],
        data_raff["avg abs"].iloc[4:],
        data_raff["+/- abs"].iloc[4:],
        linewidth=1.0,
        label="Aga27A 2 + Raffinose",
        marker="o",
        linestyle="none",
        capsize=2,
    )
    # Plot Aga27A 1 stachyose points
    plt.errorbar(
        data_stach["conc. [mM]"].iloc[:4],
        data_stach["avg abs"].iloc[:4],
        data_stach["+/- abs"].iloc[:4],
        linewidth=1.0,
        label="Aga27A 1 + Stachyose",
        marker="o",
        linestyle="none",
        capsize=2,
    )
    # Plot Aga27A 2 stachyose points
    plt.errorbar(
        data_stach["conc. [mM]"].iloc[4:],
        data_stach["avg abs"].iloc[4:],
        data_stach["+/- abs"].iloc[4:],
        linewidth=1.0,
        label="Aga27A 2 + Stachyose",
        marker="o",
        linestyle="none",
        capsize=2,
    )

plt.legend(title="data:")
plt.title("DNS assay results - %s" % date.today())
plt.xlabel("concentration of reduced ends [mM]")
plt.ylabel("Absorbance (540nm)")
# plt.show()
