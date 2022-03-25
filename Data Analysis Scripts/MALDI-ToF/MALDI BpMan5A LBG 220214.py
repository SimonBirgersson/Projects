# MALDI-ToF BpMan5A LBG 220214
import os
from datetime import date

import matplotlib.pyplot as plt
import numpy as np

import peaks

PATH = "/Users/simon/OneDrive - Lund University/data/MS/BpMan5A LBG transfer 220214/text files/"


# creates a folder named "figures" if there isn't one in the working directory to store all images in
script_dir = os.path.dirname(
    __file__
)  # finds absolute PATH of working directory and saves it as "script_dir"
output_dir = os.path.join(
    script_dir, "figures/"
)  # creates PATH to new directory and saves it as "output_dir"

# doesnt if there already is one.
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# For-loop that reads MALDI data for each file, converts to centroids, plots it and saves it in folder "figures"
for file in os.listdir(PATH):
    if file.endswith(".txt"):
        print("fetching data for %s..." % file)
        mz = np.loadtxt(PATH + file, usecols=(0,))
        signal = np.loadtxt(PATH + file, usecols=(1,))

        centroids = peaks.centroid(mz, signal, peaks.peak_id(signal, 1000))

        print("printing figure as '%s.png'...\n" % file[: len(file) - 11])

        peaks.plot_centroids(centroids, signal, peaks.peak_id(signal, 1000))
        # plt.plot(mz, signal, label=file)
        peaks.plot_mz_text(mz, signal, 3000, 200, 900)

        plt.title("Mass Spectrum - %s" % date.today())
        plt.xlabel("m/z")
        plt.ylabel("Signal")
        plt.xlim([200, 900])
        plt.ylim([0, max(signal) * 1.05])
        plt.grid()
        plt.legend({file[: len(file) - 11]}, loc="best")
        # plt.show()  # Show it
    plt.savefig(
        "/Users/simon/Documents/Projects/Data Analysis Scripts/figures/"
        + file[: len(file) - 11]
        + ".png",
        dpi=400,
        bbox_inches="tight",
    )
    plt.clf()
    del mz, signal, centroids
