# test

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from Linear_Regression import lin_reg

x = pd.DataFrame({"Absorbance": [1, 2, 3, 4, 5, 6, 7, 8, 9]})
y = 35 * x + 30
print(
    np.random.random_sample(
        x.shape,
    )
)
coeff = lin_reg(x, y)


y_pred = coeff[1] * x + coeff["Absorbance"]

print("y = {0:.1f} * x + {1:.1f}".format(coeff[1], coeff[0]))


ax = sns.regplot(x, y, color="b")

plt.title("Linear Regression")
plt.grid(True)
plt.show()
