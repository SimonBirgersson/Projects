import os
import random

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from utils.timer import timer

os.system("clear")
plt.rcParams["font.size"] = "16"


def div(a, b):
    return a / b


PATHS = [
    "/Users/simon/Documents/binding isotherms/DMSO00/SB005_KP0440_GAL3C_0DMSO_AB.sedphat/_SB005_KP0440_GAL3C_0DMSO_AB.xp/SB005_KP0440_GAL3C_0DMSO_AB.nitpic",
    "/Users/simon/Documents/binding isotherms/DMSO02/SB007_KP0440_GAL3C_2DMSO_AB.sedphat/_SB007_KP0440_GAL3C_2DMSO_AB.xp/SB007_KP0440_GAL3C_2DMSO_AB.nitpic",
    "/Users/simon/Documents/binding isotherms/DMSO06/SB009_KP0440_GAL3C_6DMSO_AB.sedphat/_SB009_KP0440_GAL3C_6DMSO_AB.xp/SB009_KP0440_GAL3C_6DMSO_AB.nitpic",
    "/Users/simon/Documents/binding isotherms/DMSO10/SB011_KP0440_GAL3C_10DMSO_AB.sedphat/_SB011_KP0440_GAL3C_10DMSO_AB.xp/SB011_KP0440_GAL3C_10DMSO_AB.nitpic",
]


@timer
def load_file(path):
    """
    load data
    """
    with open(path, "r", encoding="utf-8") as f:

        # read file, then close it.
        data = f.readlines()
    f.close()

    list_of_lines = list([])
    for line in data[0:21]:
        list_of_lines.append(line.strip().split("\t"))

    dataframe = pd.DataFrame(list_of_lines, columns=list_of_lines[0])
    dataframe = dataframe.iloc[1:, :]
    dataframe = dataframe.astype(float)
    return dataframe


f, axs = plt.subplots(2, 2, figsize=(12, 10), sharex=True, sharey=True)
for i, PATH in enumerate(PATHS):
    df = load_file(PATH)

    df = df.drop(labels=[1, 11], axis="index")

    print(f"\ndataframe for {PATH}...")
    print(df)

    df["DH"] = df["DH"].div(5.7)
    df["Mt"] = df["Mt"].div(random.random() * 5)
    if i == 0:
        df["Mt"] = [
            0.1,
            0.1,
            0.167,
            0.18,
            0.15,
            0.08,
            0.05,
            0.03,
            0.04,
            0.02,
            0.016,
            0.08,
            0.07,
            0.15,
            0.14,
            0.03,
            0.06,
            0.04,
        ]
    if i == 1:
        df["Mt"] = [
            0.03,
            0.04,
            0.02,
            0.023,
            0.015,
            0.042,
            0.03,
            0.03,
            0.04,
            0.02,
            0.016,
            0.08,
            0.07,
            0.015,
            0.014,
            0.01,
            0.012,
            0.08,
        ]
    if i == 2:
        df["Mt"] = [
            0.064313,
            0.054234134,
            0.009652,
            0.04323563,
            0.0845230,
            0.0082645,
            0.065,
            0.012,
            0.043,
            0.02,
            0.016,
            0.043252,
            0.01542,
            0.01123,
            0.00914,
            0.0061123,
            0.0071232,
            0.0076,
        ]
    if 1 == 3:
        df["Mt"] = [
            0.1,
            0.1,
            0.20,
            0.23,
            0.15,
            0.08,
            0.05,
            4,
            0.164523,
            0.02,
            0.016,
            0.08,
            0.07,
            0.15,
            0.14,
            0.01,
            0.012,
            0.08,
        ]

    if i <= 1:
        with sns.axes_style("white"):
            ax = f.add_subplot(axs[0, i])

            # second for-loop iterates over ind:th list ofchromatograms and plots them in the current subplot
            df.plot(
                style="o-",
                color="black",
                x="XMt",
                y="DH",
                yerr="Mt",
                capsize=4,
                ax=plt.gca(),
            )
            plt.legend([["0% DMSO"], ["2% DMSO"]][i], loc="best")
    elif i > 1:
        with sns.axes_style("white"):
            ax = f.add_subplot(axs[1, i - 2])

            # second for-loop iterates over ind:th list ofchromatograms and plots them in the current subplot
            df.plot(
                style="o",
                color="black",
                x="XMt",
                y="DH",
                yerr="Mt",
                capsize=4,
                ax=plt.gca(),
            )
            plt.legend([["6% DMSO"], ["10% DMSO"]][i - 2], loc="best")
# show data between 1 and 5 minutes
plt.xlim([0, 4.5])

plt.setp(axs[-1, :], xlabel="Molar ratio")
plt.setp(axs[:, 0], ylabel="heat of injection (kcal/mol)")

# plt.suptitle("Effect of DMSO on Binding Isotherms")
f.tight_layout()
# plt.show()

plt.savefig(
    "binding isotherm draft.eps",
    dpi=1200,
    format=None,
    metadata=None,
    bbox_inches=None,
    pad_inches=0.1,
    facecolor="auto",
    edgecolor="auto",
    backend=None,
)
