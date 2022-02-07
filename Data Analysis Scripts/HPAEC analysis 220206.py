# HPAEC analysis 220206

# imports
import os
from datetime import date
from operator import index
from unittest import signals

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import peaks

# read data
PATH = "C:/Users/User/Downloads/OneDrive_2022-02-06/Simon-lovisa run 27.03.21/"

# creates a folder named "figures" if there isn't one in the working directory to store all images in

# finds absolute PATH of working directory and saves it as "script_dir"
script_dir = os.path.dirname(__file__)

# creates PATH to new directory and saves it as "output_dir"
output_dir = os.path.join(script_dir, "figures/")

if not os.path.isdir(output_dir):  # doesnt if there already is one.
    os.makedirs(output_dir)


for i, file in enumerate(os.listdir(PATH)):
    if file.endswith(".txt"):
        print("fetching data for %s..." % file)

        if i == 1:
            filename = []
            data = np.zeros(
                [
                    len(np.loadtxt(PATH + file, skiprows=44, usecols=(0,))),
                    len(os.listdir(PATH)) + 1,
                ]
            )
            data[:, i] = np.loadtxt(PATH + file, skiprows=44, usecols=(0,))
            data[:, i + 1] = np.loadtxt(PATH + file, skiprows=44, usecols=(2,))

        data[:, i + 1] = np.loadtxt(PATH + file, skiprows=44, usecols=(2,))
        filename.append(file[: len(file) - 4])


print(data.shape, filename.shape)
