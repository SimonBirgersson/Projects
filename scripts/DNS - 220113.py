# DNS - 220113

# imports
import statistics as stat
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import linregress as linreg

# standard data entry in pandas data fram, blank values are removed from absorbance values
std = pd.DataFrame(
    {
        "Conc. M1 [mM]": [5, 10, 20, 40, 50],
        "abs #1": [
            x - stat.mean([0.097, 0.096]) for x in [0.112, 0.253, 0.561, 1.162, 1.499]
        ],
        "abs #2": [
            x - stat.mean([0.097, 0.096]) for x in [0.118, 0.247, 0.567, 1.201, 1.463]
        ],
    }
)

# Calulates average absorbance and stdev for standard absorbance
std["avg abs"] = std[["abs #1", "abs #2"]].mean(axis=1)
std["+/-"] = std[["abs #1", "abs #2"]].std(axis=1)

# Fits the data into a linear regression class
k, m, r_value, p_value, std_err = linreg(std["Conc. M1 [mM]"], std["avg abs"])
func = (
    lambda x: (x - m) / k
)  # Function to utilize later for calculation of concentration

# Sample data
# -------------------- TpMan5A ----------------------------------------------------------------
TpMan5A = pd.DataFrame(
    {
        "abs #1": [x - 0.102 for x in [0.350]],
        "abs #2": [x - 0.102 for x in [0.361]],
        "Dilution": 4,
    }
)
# Calulates average absorbance and stdev for sample absorbance
TpMan5A["avg abs"] = TpMan5A[["abs #1", "abs #2"]].mean(axis=1)
TpMan5A["+/-"] = TpMan5A[["abs #1", "abs #2"]].std(axis=1)

# Predicts concentrations of sample points
TpMan5A["Conc. red. ends"] = TpMan5A["avg abs"].apply(func)
TpMan5A["+/- mM"] = TpMan5A["+/-"].apply(func)

# -------------------- BpMan5A ----------------------------------------------------------------
BpMan5A = pd.DataFrame(
    {
        "abs #1": [x - 0.102 for x in [0.503]],
        "abs #2": [x - 0.102 for x in [0.532]],
        "Dilution": 4,
    }
)
# Calulates average absorbance and stdev for sample absorbance
BpMan5A["avg abs"] = BpMan5A[["abs #1", "abs #2"]].mean(axis=1)
BpMan5A["+/-"] = BpMan5A[["abs #1", "abs #2"]].std(axis=1)

# Predicts concentrations of sample points
BpMan5A["Conc. red. ends"] = BpMan5A["avg abs"].apply(func)
BpMan5A["+/- mM"] = BpMan5A["+/-"].apply(func)

# -------------------- TrMan5A ----------------------------------------------------------------
TrMan5A = pd.DataFrame(
    {
        "abs #1": [x - 0.102 for x in [0.637, 0.308, 0.135]],
        "abs #2": [x - 0.102 for x in [0.675, 0.303, 0.138]],
        "Dilution": [20, 40, 80],
    }
)
# Calulates average absorbance and stdev for sample absorbance
TrMan5A["avg abs"] = TrMan5A[["abs #1", "abs #2"]].mean(axis=1)
TrMan5A["+/-"] = TrMan5A[["abs #1", "abs #2"]].std(axis=1)

# Predicts concentrations of sample points
TrMan5A["Conc. red. ends"] = TrMan5A["avg abs"].apply(func)
TrMan5A["+/- mM"] = TrMan5A["+/-"].apply(func)
# ---------------------------------------------------------------------------------------------
# Shows the coefficients from the linear regression
"""
print("TpMan5A \n", TpMan5A)

print("BpMan5A \n", BpMan5A)

print("TrMan5A \n", TrMan5A)
"""
# Prints the functions from the linear regression
print("\nFitted equation is: abs = %.3f * c + %.3f" % (k, m))

# The coefficient of determination R2: 1 is perfect prediction
print("\nCoefficient of determination (R2): %.4f" % r_value)

plt.figure(figsize=(8, 4), tight_layout=True)
# plot std points
plt.errorbar(
    std["Conc. M1 [mM]"],
    std["avg abs"],
    std["+/-"],
    linewidth=1.0,
    label="standard points",
    marker="o",
    linestyle="none",
    capsize=2,
)

# plot linear regression
plt.plot(
    np.linspace(0, 50),
    k * np.linspace(0, 50) + m,
    linewidth=1.0,
    label="linear fit",
    linestyle="-",
)

# Plot TpMan5A points
plt.errorbar(
    TpMan5A["Conc. red. ends"],
    TpMan5A["avg abs"],
    TpMan5A["+/-"],
    linewidth=1.0,
    label="TpMan5A",
    marker="o",
    linestyle="none",
    capsize=2,
)

# Plot BpMan5A points
plt.errorbar(
    BpMan5A["Conc. red. ends"],
    BpMan5A["avg abs"],
    BpMan5A["+/-"],
    linewidth=1.0,
    label="BpMan5A",
    marker="o",
    linestyle="none",
    capsize=2,
)

# plots TrMan5A points
plt.errorbar(
    TrMan5A["Conc. red. ends"],
    TrMan5A["avg abs"],
    TrMan5A["+/-"],
    linewidth=1.0,
    label="TrMan5A",
    marker="o",
    linestyle="none",
    capsize=2,
)


plt.legend(title="data:")
plt.title("DNS assay results - %s" % date.today())
plt.xlabel("concentration of reduced ends [mM]")
plt.ylabel("Absorbance (540nm)")
plt.grid(True)
# plt.show()
