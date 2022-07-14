# Script that experiments with random 1D functions for fitting program to use.
import operator
import random

import matplotlib.pyplot as plt
import numpy as np

# import nonlinreg

# dependent variable
X = np.float_(np.array(range(1, 20, 1)))

# random function function
def rand_func(x, num=3):
    """generate a random function"""
    # dict of math operations
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "^": operator.pow,
    }
    # initialize coefficient and operator lists
    k, op = [], []

    # loop that generates random coefficients and operators
    for i in range(0, num):
        k.append(
            random.randint(1, 10)
        )  # I don't sample 0's to protect against divide-by-zero
        op.append(random.choice(list(ops.keys())))

    # Prints the function
    print(
        f"Randomised function:\n y = ((x {op[0]} {k[0]}) {op[1]} {k[1]}) {op[2]} {k[2]}\n"
    )

    # define the function of randomized coefficients and operators
    def func(x, p=k):
        """random function resulted from "rand_func"."""
        # y = ops.get(op[2])(ops.get(op[1])(ops.get(op[0])(p[0], x), p[2]))
        y = ops.get(op[2])(ops.get(op[1])(ops.get(op[0])(x, p[0]), p[1]), p[2])
        return y

    return func


# randomize functions, and plot them
for i in range(0, 8):
    plt.plot(X, rand_func(X)(X), "-")

plt.ylim((-10, 100))
plt.show()
