# HPAEC analysis module 220207
import os

import numpy as np
import pandas as pd


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
            print("fetching data for %s..." % file)
            # initialize variable for storing filenames
            filename = []
            # loads time and signal vector for the first injection
            data = np.loadtxt(PATH + file, skiprows=skip_rows, usecols=(0, 2))
            # adds the first filename minus file extension to the list "filename"
            filename.append(file[: len(file) - 4])

        # if the the filetype is .txt but not the first iteration of the loop:
        elif file.endswith(".txt"):
            print("fetching data for %s..." % file)
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
