# HPAEC analysis 220206

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
PATH = "/Users/simon/OneDrive - Lund University/HPAEC figure making package/Simon-lovisa run 27.03.21/"

# Figures - enter files to plot
chromatograms = [
    [
        "TpMan5A M5 0h  100uM 2_ED_1",
        "TpMan5A M5 1h  100uM 2_ED_1",
        "TpMan5A M5 48h  100uM 2_ED_1",
    ],
    [
        "water_ED_1",
        "buffer_ED_1",
        "M5 ctrl 24h  100uM 1_ED_1",
        "TpMan5A ctrl 24h  100uM 2_ED_1",
    ],
    [
        "2.5  um 1_ED_1",
        "10 um 1_ED_1",
        "20 um 1_ED_1",
        "30 um 1_ED_1",
    ],
]

# Enter titles of plots
plots = ["TpMan5A + M5", " Controls", "Standard series"]

HPAEC_analysis.plot_hpaec_chromatograms(
    HPAEC_analysis.load_hpaec_data(PATH, 44, ".txt"), plots, chromatograms
)
plt.show()
# saves the figure
"""plt.savefig(
    "/Users/simon/Documents/Projects/Data Analysis Scripts/figures/"
    + "TpMan5A "
    + str(date.today())
    + ".png",
    dpi=800,
    bbox_inches="tight",
)
"""
