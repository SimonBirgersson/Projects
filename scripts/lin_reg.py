# Simple linear regression function

import statsmodels.api as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_boston = pd.read_csv('/Users/SimonsFolder/Projects/scripts/Boston Housing Prices.csv')
#print(df_boston)

y = df_boston['Value'] # dependent variable
x = df_boston['Rooms'] # independent variable

x = sm.add_constant(x) # adding a constant
lm = sm.OLS(y,x).fit() # fitting the model

print(lm.summary())


coeff = lm.params

y_pred = coeff[1] * x['Rooms'] + coeff[0]

# Plotting the data points
sns.scatterplot(x = x['Rooms'], y = y)

# Plotting the linear fit
plt.plot(x['Rooms'] , y_pred, color = 'r')

# Axes
plt.xlim(0)
plt.ylim(0)
plt.grid()
plt.show()

def lin_reg(x, y, xname, yname):
    
    x = sm.add_constant(x)

    lm = sm.OLS(y, x).fit()

    coeff = lm.params

    
