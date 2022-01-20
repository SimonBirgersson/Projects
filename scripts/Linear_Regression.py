# Simple linear regression function

import statsmodels.api as sm


# must enter Pandas DataFrame variables into this function
def lin_reg(x, y):
    x = sm.add_constant(
        x
    )  # adds constant to value, allows for fit of intercept as well as constant

    lm = sm.OLS(y, x).fit()  # fits the data to variable lm

    print(lm.summary())  # provides som information in the terminal about the fit

    coeff = lm.params  # saves k, m in coeff

    coeff.rename(index={"const": "m", "0": "k"})  # renames columns

    return coeff
