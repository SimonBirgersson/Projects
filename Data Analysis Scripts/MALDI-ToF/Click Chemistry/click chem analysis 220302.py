# click chem analysis 220302
import fnmatch
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

os.system("clear")

# finds absolute PATH of working directory and saves it as "script_dir"
script_dir = os.path.dirname(__file__)

# creates PATH to new directory and saves it as "output_dir"
output_dir = os.path.join(script_dir, "figures/")

# doesnt if there already is one.
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)
"""
PATH = "/Users/simon/Documents/Projects/Data Analysis Scripts/MALDI-ToF/Click Chemistry/220125 click chem try 1/"

f = plt.figure(figsize=(6, len(fnmatch.filter(os.listdir(PATH), "*" + ".txt"))))
gs = f.add_gridspec(len(fnmatch.filter(os.listdir(PATH), "*" + ".txt")), 1)

for i, file in enumerate(fnmatch.filter(os.listdir(PATH), "*" + ".txt")):
    # checks if file ends with .txt AND is the first iteration of the loop:
"""
data = pd.read_csv(
    "/Users/simon/Documents/Projects/Data Analysis Scripts/MALDI-ToF/Click Chemistry/220125 click chem try 1/2.txt",
    encoding="unicode_escape",
    decimal=".",
    header=0,
    names=["Time(min)", "sum of MS signal"],
    skiprows=0,
    encoding_errors="ignore",
    sep="\t",
    usecols=(0, 1),
)

# style of subplot and position
with sns.axes_style("whitegrid"):
    # ax = f.add_subplot(gs[i, 0])
    plt.plot(data["Time(min)"], data["sum of MS signal"])
    plt.title("chromatogram")
    plt.xlabel("time [min]")
    plt.ylabel("sum of MS signal")
    plt.show()
