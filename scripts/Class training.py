# Class training

# imports
import statistics as stat
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import linregress as linreg

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


class Enzyme:
    def __init__(self, abs, dil, temp, pH):
        self.dil = dil
        self.abs = abs
        self.temp = temp
        self.pH = pH
        self.c = (abs - m) / k
        pass


TrMan5A = Enzyme(
    np.array([[0.350], [0.361]]) - 0.102,
    4,
    40,
    6,
)
