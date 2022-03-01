# HPAEC analysis module 220207
import fnmatch
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xlrd


def load_hpaec_data(path, skip_rows, filetype):
    """function that checks directory indicated in path for files with filetype as indicated by "filetype" (most usually ".txt"), the grabs first and third column of data, after skip_rows, and stores it in DataFrame with column headers as the filename"""

    # for loop that stores time vector as first column, then the signal vectors as each following vector
    # sorts files in directory in descending order after last character in filename, i.e .txt files first, then .xls files

    for i, file in enumerate(fnmatch.filter(os.listdir(path), "*" + filetype)):

        # checks if file ends with .txt AND is the first iteration of the loop:
        if file.endswith(filetype) and i == 0:
            print("fetching data from %s..." % file)

            # initialize variable for storing filenames
            filename = []

            # loads time and signal vector for the first injection
            data = np.loadtxt(path + file, skiprows=skip_rows, usecols=(0, 2))

            # adds the first filename minus file extension to the list "filename"
            filename.append(file[: len(file) - 4])

        # if the the filetype is .txt but not the first iteration of the loop:
        elif file.endswith(filetype):
            print("fetching data from %s..." % file)

            # adds a new colum containing the signal vector for the next injection
            data = np.append(
                data,
                np.loadtxt(path + file, skiprows=skip_rows, usecols=(2,)).reshape(
                    -1, 1
                ),
                axis=1,
            )

            # add the corresponding name to the list "filename"
            filename.append(file[: len(file) - 4])
        # if it isn't a .txt file, do nothing:
        else:
            pass

    # put all the data into a DataFrame, with column headers as the filenames:
    try:
        df = pd.DataFrame(data, columns=["time [min]"] + filename)
    except:
        pass

    return df


def load_hplc_data(path, skip_rows, filetype):
    """function that checks directory indicated in path for files with filetype as indicated by "filetype" (most usually ".txt"), the grabs first and third column of data, after skip_rows, and stores it in DataFrame with column headers as the filename. Difference from "load_HPAEC_data" is that it loads comma decimaled and tab delimited data."""
    data, filename = [], []
    # For-loop for collecting dataframes of each injection in a list
    for i, file in enumerate(fnmatch.filter(os.listdir(path), "*" + filetype)):
        # checks if file ends with .txt AND is the first iteration of the loop:

        if file.endswith(filetype):
            # print("fetching data from " + file + "...")
            if filetype == ".xlsx":
                try:
                    data.append(
                        pd.read_excel(
                            path + file,
                            decimal=".",
                            header=0,
                            names=["Time(min)", file[4 : len(file) - 4]],
                            skiprows=skip_rows,
                            usecols=(0, 2),
                            engine="openpyxl",
                        )
                    )

                except pd.errors.EmptyDataError:
                    pass
            # loads time and signal vector for the first injection
            if filetype == ".txt":
                try:
                    data.append(
                        pd.read_csv(
                            path + file,
                            encoding="unicode_escape",
                            decimal=",",
                            header=0,
                            names=["Time(min)", file[: len(file) - 4]],
                            skiprows=skip_rows,
                            encoding_errors="ignore",
                            sep="\t",
                            usecols=(0, 2),
                        )
                    )

                except pd.errors.EmptyDataError:
                    pass

            # adds the first filename minus file extension to the list "filename"
            filename.append(file[: len(file) - 4])

        # if it isn't a .txt file, do nothing:
        else:
            pass

    return data, filename


def plot_hpaec_chromatograms(data, plots, chromatograms):
    """plots chromatograms in DataFrame "data" in a vertical plot, with subplots as titled in "plots", containing chromatograms from dataframe columns "chromatograms" """
    # size of plot and subplot dimensions
    f = plt.figure(figsize=(36, len(plots) * 6))
    gs = f.add_gridspec(len(plots), 1)

    # first for-loop iterates over titles of subplots
    for ind, subplot in enumerate(plots):

        # style of subplot and position
        with sns.axes_style("whitegrid"):
            ax = f.add_subplot(gs[ind, 0])

            # second for-loop iterates over ind:th list ofchromatograms and plots them in the current subplot
            for column in chromatograms[ind][:]:
                data.plot(
                    kind="line",
                    x="time [min]",
                    y=column,
                    label=column,
                    ax=plt.gca(),
                )

        # show data between 1 and 5 minutes
        plt.xlim([1.0, 5])
        # plt.xlabel("time [min]")
        plt.legend(loc="best")
        plt.ylabel("signal [nC]")
        plt.title(subplot)
        f.tight_layout()


def plot_hplc_chromatograms(data, filename, plots, chromatograms):
    """Plots the data loaded in "load_hplc_data" in subplots denoted in "plots" with chromatogram denoted in "chromatograms" """
    # size of plot and subplot dimensions
    f = plt.figure(figsize=(6, len(plots) * 4))
    gs = f.add_gridspec(len(plots), 1)

    # loop over each subplot in "plots"
    for ind, subplot in enumerate(plots):

        # style of subplot and position
        with sns.axes_style("whitegrid"):
            ax = f.add_subplot(gs[ind, 0])

            # second for-loop iterates over ind:th list ofchromatograms and plots them in the current subplot
            for i, column in enumerate(chromatograms[ind][:]):
                try:
                    data[filename.index(column)].plot(
                        kind="line",
                        x="Time(min)",
                        y=column,
                        label=column,
                        ax=plt.gca(),
                    )
                except ValueError:
                    print(column + " is not in list")

        # show data between 1 and 5 minutes
        plt.xlim([3, 8])
        # plt.xlabel("time [min]")
        plt.legend(loc="best")
        plt.ylabel("Signal [pA]")
        plt.title(subplot)
        f.tight_layout()
