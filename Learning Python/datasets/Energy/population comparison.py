import matplotlib.pyplot as plt
import pandas as pd

# import dataset
pop_tot = pd.read_csv(
    "/Users/simon/Documents/Projects/Learning Python/datasets/Energy/population_total.csv"
)

# Create array years, and format to datetime
years = pop_tot.columns
years = pd.to_datetime(years[1:])
years = years.to_numpy()

# make array out of dataset
pop_tot = pop_tot.to_numpy()

# Separate into country names and poulation amounts
country_names = pop_tot[:, 0]
pop_tot = pop_tot[:, 1:]

# Change data to floats instead of strings
for xind, x in enumerate(pop_tot):
    for yind, y in enumerate(x):

        if y.find("B") != -1:
            pop_tot[xind, yind] = float(y[: len(y) - 1]) * 10**9

        elif y.find("M") != -1:
            pop_tot[xind, yind] = float(y[: len(y) - 1]) * 10**6

        elif y.find("k") != -1:
            pop_tot[xind, yind] = float(y[: len(y) - 1]) * 10**3

        else:
            pop_tot[xind, yind] = float(y)

# plots population growth for countries indicated in "countries"
index = []
countries = "Sweden", "Norway"
for country in countries:
    plt.plot(
        years,
        pop_tot[
            [i for i, elem in enumerate(country_names) if country in elem], :
        ].transpose(),
        label=country,
    )

plt.title("Population Growth")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.show()

# NExt, show the different kinds if energy productions of the different countries over the years
