# HPAEC analysis 220206

# imports
import os
from datetime import date
from operator import index
from unittest import signals

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import HPAEC_analysis
import peaks

# read data
PATH = "C:/Users/User/Downloads/OneDrive_2022-02-06/Simon-lovisa run 27.03.21/"

# creates a folder named "figures" if there isn't one in the working directory to store all images in

# finds absolute PATH of working directory and saves it as "script_dir"
script_dir = os.path.dirname(__file__)

# creates PATH to new directory and saves it as "output_dir"
output_dir = os.path.join(script_dir, "figures/")

# doesnt if there already is one.
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

data = HPAEC_analysis.load_data(PATH, 44)
print(data)
