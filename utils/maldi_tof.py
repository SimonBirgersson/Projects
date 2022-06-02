"""
Provides function for loading .csv MALDI Data into dictionary of dataframes with keys according to the filename
"""
import os
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from utils.peaks import plot_vert
from utils.timer import timer


@timer
def load_ms_csv(path: str):
    """
    load ms data from .csv export into a dictionary with key according to file name and dataframes of m/z and signal.
    """

    # create empty directory
    data = {}

    # for each file in the path directory:
    for file in os.listdir(path):

        # if the file is a txt file:
        if file.endswith(".txt"):

            # print message without starting new line
            print(f"fetching data for {file}...", end="\r")

            # load m/z and signal values and put them in DataFrame with filename as key
            mz = np.loadtxt(path + file, usecols=(0,))
            signal = np.loadtxt(path + file, usecols=(1,))
            data[file[: len(file) - 11].replace("_", "")] = pd.DataFrame(
                {"mz": mz, "signal": signal}
            )
    # return the dataframe
    return data


@timer
def plot_ms(
    plots: list[list[str]],
    df: dict,
    check: list[float] = None,
    xlim: tuple[float, float] = None,
    ylim: tuple[float, float] = None,
):
    """
    creates a plot of the ms data with each spectrum in subplot.

    input:
        plots: list containing lists of names of the spectra in df to plot in each subplot.
        check (optional: plot vertical lines at m/z provided for control

    output:
        a plot object.
    """
    # create plot object
    f, axs = plt.subplots(len(plots), 1, figsize=(15, 8), sharex=True, sharey=True)

    # for each list in plots:
    for i, subplot in enumerate(plots):

        # if this isn't the first plot, create new subplot
        if len(plots) > 1:
            ax = f.add_subplot(axs[i])

        # for each str in subplot:
        for j, plot in enumerate(subplot):

            # store values for plotting
            mz = df[plot]["mz"]
            signal = df[plot]["signal"]

            # if vertical lines, plot them in the subplot

            # plot the data, add labels
            plt.plot(mz, signal + 10000 * j, "-", linewidth=1)
            plt.xlabel("m/z")
            plt.ylabel("Signal")

            # if user adds x limits, change them
            if xlim:
                plt.xlim(xlim)

            if ylim:
                plt.ylim(ylim)
            else:
                # y limits is 0 to 105% of highest signal
                plt.ylim([0, max(signal) * 1.05])

        # add grid and put legend at best location.
        plt.grid()
        plt.legend(subplot, loc="best")
        if check:
            for line in check:
                plot_vert(line)

    # title above the entire plot.
    plt.suptitle("Mass Spectrum - %s" % date.today())
