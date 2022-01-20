# Class training

# imports
import statistics as stat
from calendar import c
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import linregress as linreg

std = (
    np.array(
        [
            # std absorbance values
            [0.112, 0.253, 0.561, 1.162, 1.499],
            [0.118, 0.247, 0.567, 1.201, 1.463],
        ]
    )
    # substract blank values
    - stat.mean([0.097, 0.096])
)

print(std)

# fits the standard data
k, m, r_value, p_value, std_err = linreg(
    [5, 10, 20, 40, 50], np.mean(std, axis=0, dtype=np.float64)
)

# Prints the functions from the linear regression
print("\nFitted equation is: abs = %.3f * c + %.3f" % (k, m))

# The coefficient of determination R2: 1 is perfect prediction
print("\nCoefficient of determination (R2): %.4f" % r_value)


class Enzyme:
    def __init__(self, abs, dil, temp, pH):
        self.dil = dil
        self.abs = abs
        self.temp = temp
        self.pH = pH
        self.c = (abs - m) / k
        self.act = (abs - m) / k * 1000 / 600
        pass


TrMan5A = Enzyme(
    np.array([[0.350], [0.361]]),
    4,
    40,
    6,
)


print(np.mean(TrMan5A.c))
