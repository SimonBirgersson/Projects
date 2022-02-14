import matplotlib.pyplot as plt
import pandas as pd

# import dataset
pop_tot = pd.read_csv(
    "/Users/simon/Documents/Projects/Learning Python/datasets/Energy/population_total.csv"
)

# lambda function that converts population amounts to floats of the value
func = (
    lambda y: float(y[: len(y) - 1]) * 10**9
    if y.find("B") != -1
    else (
        float(y[: len(y) - 1]) * 10**6
        if y.find("M") != -1
        else (
            float(y[: len(y) - 1]) * 10**3
            if y.find("k") != -1
            else (float(y) if type(y) == str else y)
        )
    )
)
# apply function to population data in dataframe
for i in range(0, pop_tot.shape[0]):
    pop_tot.loc[i, "1800":] = pop_tot.loc[i, "1800":].apply(func)

# plots population growth for countries indicated in "countries"
index = []
countries = "Sweden", "Norway"
for country in countries:
    for index in [
        i for i, elem in enumerate(list(pop_tot.loc[:, "country"])) if country in elem
    ]:
        plt.plot(
            pd.to_datetime(pop_tot.columns[1:]), pop_tot.iloc[index, 1:], label=country
        )
plt.title("Population Growth")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.show()
