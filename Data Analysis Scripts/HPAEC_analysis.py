# HPAEC analysis module 220207
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# function that checks directory indicated in PATH for txt files, the grabs first and third column of data,
# after skip_rows, and stores it in DataFram df with column header as the filename
def load_data(PATH, skip_rows):
    # for loop that stores time vector as first column, then the signal vectors as each following vector
    # sorts files in directory in descending order after last character in filename, i.e .txt files first, then .xls files
    for i, file in enumerate(
        sorted(os.listdir(PATH), key=lambda x: x[::-1], reverse=True)
    ):
        # checks if file ends with .txt AND is the first iteration of the loop:
        if file.endswith(".txt") and i == 0:
            print("fetching data from %s..." % file)
            # initialize variable for storing filenames
            filename = []
            # loads time and signal vector for the first injection
            data = np.loadtxt(PATH + file, skiprows=skip_rows, usecols=(0, 2))
            # adds the first filename minus file extension to the list "filename"
            filename.append(file[: len(file) - 4])

        # if the the filetype is .txt but not the first iteration of the loop:
        elif file.endswith(".txt"):
            print("fetching data from %s..." % file)
            # adds a new colum containing the signal vector for the next injection
            data = np.append(
                data,
                np.loadtxt(PATH + file, skiprows=skip_rows, usecols=(2,)).reshape(
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
    df = pd.DataFrame(data, columns=["time [min]"] + filename)

    return df


# plots chromatograms in a vertical plot, with subplots as titled in "plots", containing chromatograms from dataframe according to
def plot_chromatograms(data, plots, chromatograms):

    # size of plot and subplot dimensions
    f = plt.figure(figsize=(9, len(plots) * 6))
    gs = f.add_gridspec(len(plots), 1)

    # first for-loop iterates over titles of subplots
    for ind, subplot in enumerate(plots):

        # style of subplot and position
        with sns.axes_style("darkgrid"):
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
