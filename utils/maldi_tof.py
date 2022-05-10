"""
Provides function for loading .csv MALDI Data into dictionary of dataframes with keys according to the filename
"""
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from utils.timer import timer


@timer
def load_ms_csv(path: str):
    """
    load ms data from .csv export into a dictionary with key according to file name and dataframes of m/z and signal.
    """
    data = {}
    for file in os.listdir(path):
        if file.endswith(".txt"):
            print(f"fetching data for {file}...", end="\r")
            mz = np.loadtxt(path + file, usecols=(0,))
            signal = np.loadtxt(path + file, usecols=(1,))
            data[file[: len(file) - 11].replace("_", "")] = pd.DataFrame(
                {"mz": mz, "signal": signal}
            )
    return data


def plot_ms(plots, df: pd.DataFrame, check: list[float] = None):
    """
    creates a plot of the ms data with each spectrum in subplot.

    input:
        plots: names of the spectra in df to plot.
        check (optional: plot vertical lines at m/z provided for control

    output:
        a plot object.
    """
    f, axs = plt.subplots(len(plots), 1, figsize=(10, 8), sharex=True, sharey=True)
    for i, plot in enumerate(plots):

        mz = df[plot]["mz"]
        signal = df[plot]["signal"]

        if len(plots) > 1:
            ax = f.add_subplot(axs[i])

        if check:
            for line in check:
                plot_vert(line)

        plt.plot(mz, signal, "-", color="black", linewidth=1)
        plt.xlabel("m/z")
        plt.ylabel("Signal")
        plt.xlim([200, 400])
        # plt.xlim([300, 370])
        plt.ylim([0, max(signal) * 1.05])
        plt.grid()
        plt.legend({plot}, loc="best")

    plt.suptitle("Mass Spectrum - %s" % date.today())
