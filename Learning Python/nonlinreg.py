# Michaelis Menten fitting
import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model

# sample data, two lists s (initial substrate concentration) and v (measured reaction velocity in the inital regime) of equal size lists.

# 2d array with duplicates
s = np.float_(np.array(range(0, 1201, 150)))
v = np.round(120 * s / (171 + s) + np.random.uniform(size=9, low=-20, high=20), 2)

# data lifted from Lovisas weekly report 22-02-21
# s = np.array([2, 5, 10])  # [mM]
# v = np.array([93.54, 171.3, 198])  # [nkat/mg]


# function to fit to
def michaelis_menten(x, vmax=120, km=171):
    """
    MM-function.
    INPUT: "substrate" is a list of initial substrate concentrations. "vmax" is the maximum reaction velocity achievable for this system, usually fitted. "km" is the michaelis mentet coefficient, which is the substrate concentration at which 1/2 vmax is reached. Commonly referred to as affinity, which isn't entirely true.

    OUTPUT: the function returns the initial reaction velocity in the units corresponding to the units entered.
    """
    return vmax * x / (km + x)


def nonlinreg(func, x, y):
    """
    Function that fits coefficient in given function "func" using independent variable "x" and response variable "y". "func": needs to be a function with optional coefficients as input, will use default values as initial guesses, as well as depdendent variable needs to be called "x".
    """

    # generate model class
    mdl = Model(func)

    # fit data to model, initial guesses for vmax, km
    result = mdl.fit(y, x=x)

    # using calculated coefficients, calculate predicted values with uncertainty
    y_pred = result.eval(S=x)
    y_bounds = result.eval_uncertainty(sigma=2, S=x)

    # print report of fit
    print(result.fit_report())

    # Plots
    cmap = plt.cm.PuBuGn
    colors = cmap(np.linspace(0.4, 0.9, 10))
    plt.figure()

    # [v.mean(axis=1) if v.ndim > 1 else v]
    # sample data
    plt.plot(
        x,
        y,
        "o",
        markersize=8,
        color=colors[-1],
        label="observed",
    )

    # results of first fit, not nessecary at all
    plt.plot(x, result.init_fit, "--", color=colors[-2], label="initial fit")

    # results of best fit
    plt.plot(x, result.best_fit, "-", color=colors[2], label="best fit")

    # std dev
    plt.fill_between(
        x, (y_pred + y_bounds), (y_pred - y_bounds), color=colors[1], alpha=0.3
    )

    # plt.xlabel("Substrate concentration (mM)")
    # plt.ylabel("dP/dt (mM/s)")
    plt.title("Nonlinear fit")
    plt.grid()
    plt.legend(loc="best")
    plt.show()


nonlinreg(michaelis_menten, s, v)
