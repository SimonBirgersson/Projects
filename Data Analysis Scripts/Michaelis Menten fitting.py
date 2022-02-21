# Michaelis Menten fitting
import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model

# sample data, two lists s (initial substrate concentration) and v (reaction velocity in the inital regime) of equal list.
s = np.float_(np.array(range(0, 1201, 150)))
v = np.round(120 * s / (171 + s) + np.random.uniform(size=9, low=-10, high=10), 2)

# function to fit to
def michaelis_menten(substrate, vmax, km):
    """MM-function"""
    return vmax * substrate / (km + substrate)


# generate model class
mdl = Model(michaelis_menten)

# fit data to model, initial guesses for vmax, km
result = mdl.fit(v, substrate=s, vmax=100, km=181)

# using calculated coefficients, calculate predicted values with uncertainty
y_pred = result.eval(S=s)
y_bounds = result.eval_uncertainty(sigma=2, S=s)

# print report of fit
print(result.fit_report())

# Plots
cmap = plt.cm.PuBuGn
colors = cmap(np.linspace(0.4, 0.9, 10))
plt.figure()

# sample data
plt.plot(s, v, "o", markersize=8, color=colors[-1], label="observed")

# results of first fit, not nessecary at all
plt.plot(s, result.init_fit, "--", color=colors[-2], label="initial fit")

# results of best fit
plt.plot(s, result.best_fit, "-", color=colors[2], label="best fit")

# std dev
plt.fill_between(
    s, (y_pred + y_bounds), (y_pred - y_bounds), color=colors[1], alpha=0.3
)

plt.xlabel("Substrate concentration (mM)")
plt.ylabel("dP/dt (mM/s)")
plt.title("Nonlinear fit")
plt.grid()
plt.legend(loc="best")
plt.show()
