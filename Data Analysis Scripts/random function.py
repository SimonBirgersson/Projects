import operator
import random

import numpy as np

import nonlinreg

x = np.float_(np.array(range(0, 1201, 150)))
y = np.round(s**120 + 171)


def rand_func(x, p=120, q=171):
    """random function"""
    return x**p + q


def randomCalc():
    """Provides random math operations"""
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    num1 = random.randint(0, 12)
    num2 = random.randint(1, 10)  # I don't sample 0's to protect against divide-by-zero
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1, num2)
    print("What is {} {} {}?\n".format(num1, op, num2))
    return answer


randomCalc
