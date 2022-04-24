import matplotlib.pyplot as plt
import numpy
import pandas as pd

# "/Users/simon/Documents/Projects/Learning Python/datasets/Energy/co2_emissions_tonnes_per_person.csv",
PATHS = [
    "/Users/simon/Documents/Projects/Learning Python/datasets/Energy/hydro_power_generation_per_person.csv",
    "/Users/simon/Documents/Projects/Learning Python/datasets/Energy/natural_gas_production_per_person.csv",
    "/Users/simon/Documents/Projects/Learning Python/datasets/Energy/nuclear_power_generation_per_person.csv",
    "/Users/simon/Documents/Projects/Learning Python/datasets/Energy/oil_production_per_person.csv",
]

data = list()
for path in PATHS:
    df = pd.read_csv(path)
    # print("saving file " + path + "...")
    data.append(df)
datasets = [
    "Hydro power generation per person",
    "Natural gas",
    "Nuclear power generation per person",
    "Oil generation per person",
]
# function removes mu and changes to float
func = (
    lambda y: float(y[: len(y) - 1]) * 10**-6
    if isinstance(y, str) and y.find("µ") != -1
    else (float(y) if isinstance(y, str) else y)
)

# apply function to population data in dataframe
for p, hatten in enumerate(data):
    for i in range(0, data[p].shape[0]):
        data[p].iloc[i, 1:] = data[p].iloc[i, 1:].apply(func)

# plots
index = []
COUNTRIES = ["United Kingdom"]
for country in COUNTRIES:
    for p in range(0, len(data)):
        for i, elem in enumerate(list(data[p].loc[:, "country"])):
            if elem == country:
                plt.plot(
                    pd.to_datetime(data[p].columns[1:]),
                    data[p].iloc[i, 1:],
                    label=datasets[p],
                )
            else:
                pass

    plt.title("Energy production of " + country)

plt.xlabel("Year")
plt.ylabel("Tonnes oil equivalent yearly")
plt.legend()
plt.grid(True)
plt.show()
