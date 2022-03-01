# MALDI-ToF BpMan5A sacharide transfer experiment 220121
import os
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import peaks

# PATH = "/Users/SimonsFolder/OneDrive - Lund University/data/MS/BpMan5A M4 sach transfer 220121/"
PATH = "/Users/SimonsFolder/OneDrive - Lund University/data/MS/BpMan5A M4 sach transfer 2201211/"

# creates a folder named "figures" if there isn't one in the working directory to store all images in
script_dir = os.path.dirname(
    __file__
)  # finds absolute PATH of working directory and saves it as "script_dir"
output_dir = os.path.join(
    script_dir, "figures/"
)  # creates PATH to new directory and saves it as "output_dir"

if not os.path.isdir(output_dir):  # doesnt if there already is one.
    os.makedirs(output_dir)

for file in os.listdir(PATH):
    if file.endswith(".txt"):
        print("fetching data for %s..." % file)
        mz = np.loadtxt(PATH + file, usecols=(0,))
        signal = np.loadtxt(PATH + file, usecols=(1,))

        centroids = peaks.centroid(mz, signal, peaks.peak_id(signal, 1000))
        print(mz[peaks.peak_id(signal, 1000)], centroids)

        print("printing figure as '%s.png'...\n" % file[: len(file) - 4])

        plt.plot(
            mz,
            signal,
            linewidth=1,
            label="spectrum",
            linestyle="-",
            color="r",
        )  # Plot the actual spectrum
        plt.grid()
        plt.title("Mass Spectrum - %s" % date.today())
        plt.xlabel("m/z")
        plt.ylabel("Signal")
        plt.xlim([200, 900])
        plt.legend(file, loc=2)
        # plt.show()  # Show it

        plt.savefig(
            "/Users/SimonsFolder/Projects/scripts/figures/"
            + file[: len(file) - 4]
            + ".png",
            dpi=400,
            bbox_inches="tight",
        )
        del mz, signal, centroids
"""
        try:
            for i in centroids[
                1:
            ]:  # Call my plotting function on every centroid except the first
                peaks.plot_vert(i)

            plt.axvline(
                centroids[0], color="blue", ls="-.", label="Centroid"
            )  # Reserve the first so I don't have a million "centroid" labels
            print("peaks detected at %0.3f m/z" % centroids)
        except TypeError:
            print("No peaks were detected")

        finally:
"""
