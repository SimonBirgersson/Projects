# HPLC analysis of 40 ml TrMan5A + Aga27A + allyl alcohol

# imports
import os
from datetime import date

import matplotlib.pyplot as plt

import HPAEC_analysis

# finds absolute PATH of working directory and saves it as "script_dir"
script_dir = os.path.dirname(__file__)

# creates PATH to new directory and saves it as "output_dir"
output_dir = os.path.join(script_dir, "figures/")

# doesnt if there already is one.
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# read data
PATH = "/Users/simon/OneDrive - Lund University/Synergy project/40ml incubation chromatogram 210527/"


# Enter titles of plots
plots = [
    "TrMan5A + Aga27A + allyl alcohol",
    "Resuspended pellet from ACN dilution",
    "Standard series of allyl-alpha-mannose",
]

# Figures - enter files to plot
chromatograms = [
    [
        "New LBG Iso 1CAD_1",
    ],
    [
        "Resuspended Pellet Iso 1CAD_1",
    ],
    [
        "3 mM iso 1CAD_1",
        "5 mM iso 1CAD_1",
        "10 mM Iso 1CAD_1",
    ],
]

# load HPLC data into data and the formatted names of each injection into filename
data, filename = HPAEC_analysis.load_hplc_data(PATH, 77, ".TXT")

HPAEC_analysis.plot_hplc_chromatograms(data, filename, plots, chromatograms)
# saves the figure
plt.savefig(
    "/Users/simon/Documents/Projects/Data Analysis Scripts/figures/"
    + "40ml incubation "
    + str(date.today())
    + ".png",
    dpi=800,
    bbox_inches="tight",
)
