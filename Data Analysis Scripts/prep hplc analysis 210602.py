# prep hplc analysis

import os

import matplotlib.pyplot as plt
import pandas as pd

from HPAEC_analysis import load_hplc_data

os.system("clear")

# finds absolute PATH of working directory and saves it as "script_dir"
script_dir = os.path.dirname(__file__)

# creates PATH to new directory and saves it as "output_dir"
output_dir = os.path.join(script_dir, "figures/")

# doesnt if there already is one.
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)


"""df = load_hplc_data(
    r"/Users/simon/OneDrive - Lund University/data/HPLC/prep_hplc/2021-06-02/",
    5,
    ".xls",
)"""

df = pd.read_excel(
    r"/Users/simon/OneDrive - Lund University/data/HPLC/prep_hplc/2021-06-02/lbg allyl transfer 1 5ml_2021-06-02 15-05-23_SA220nm.xls",
    decimal=".",
    header=0,
    names=["Time(min)", "KATT"],
    skiprows=5,
    usecols=(0, 2),
    engine="xlrd",
)
print(df)
