"""
Provides function for loading .csv MALDI Data into dictionary of dataframes with keys according to the filename
"""
import os

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
