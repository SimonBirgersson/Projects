# prep hplc analysis


import fnmatch
import os

import matplotlib.pyplot as plt
import pandas as pd
import pyexcel as p
import xlrd
from openpyxl import load_workbook

from HPAEC_analysis import load_hplc_data, plot_hpaec_chromatograms

os.system("clear")

# finds absolute PATH of working directory and saves it as "script_dir"
script_dir = os.path.dirname(__file__)

# creates PATH to new directory and saves it as "output_dir"
output_dir = os.path.join(script_dir, "figures/")

# doesnt if there already is one.
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

PATH = "/Users/simon/OneDrive - Lund University/data/HPLC/prep_hplc/2021-06-02/"


data = pd.read_excel(
    PATH + "lbg allyl transfer 1 5ml_2021-06-02 15-05-23_SA220nm.xlsx",
    engine="openpyxl",
)


# data, filename = load_hplc_data(PATH, 4, ".xlsx")
print(data)
# pyexcel.transcode() "$file" "${file}x"; done;
