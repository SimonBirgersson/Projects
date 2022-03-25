import matplotlib.pyplot as plt
import numpy as np


def peak_id(signal, threshold):
    """
    Peak identification function - (220121)

     input is vector of y values and minimum value for peak, returns indices of each peak
    """
    peaks = []  # x positions of the peaks, or rather, their index
    for i in range(
        len(signal) - 1
    ):  # len(signal)-1 because you will be checking the value after than your last i
        if (
            signal[i - 1] < signal[i]
            and signal[i + 1] < signal[i]
            and threshold < signal[i]
        ):  # three conditions to be a peak, bigger than the previous and next value, and over the threshold
            peaks.append(i)  # puts the index in "signal" for the peak here.
    return peaks


def centroid(x, signal, peaks):
    """
    centroid identification function - (220121)

     input is x and y vector, and indices for peaks from "peak_id" function. returns x values of mass centered centroids
    """
    centroids = []  # Values for all the centroids
    for i in peaks:
        # Calculate how far backward and forward to go:
        half_max = signal[i] / 2.0
        xmin = (np.where(signal[i::-1] < half_max)[0])[0]
        xmax = (np.where(signal[i:] < half_max)[0])[0]
        x_range = x[i - xmin : i + xmax]
        I_range = signal[i - xmin : i + xmax]
        x_range = np.array(x_range)
        I_range = np.array(I_range)
        xcm = np.sum((x_range * I_range)) / np.sum(I_range)
        centroids.append(xcm)
    return centroids


def plot_vert(x):
    """
    Just plots vertical lines, in blue dashes
    """
    plt.axvline(x, color="blue", ls="-.")


def plot_centroids(centroids, signal, peaks):
    """
    plots centroid data
    """
    for index, i in enumerate(peaks):
        plt.vlines(
            centroids[index],
            0,
            signal[i],
            colors="k",
            linestyles="solid",
            Linewidth=1,
        )


def plot_mz_text(mz, signal, threshold, xmin, xmax):
    """
    plot mz data
    """
    for index, i in enumerate(peak_id(signal, threshold)):
        centr = centroid(mz, signal, peak_id(signal, threshold))
        if mz[i] < xmax and mz[i] > xmin:
            plt.text(
                centr[index],
                signal[i] + 1000,
                str(mz[i]),
                fontsize=8,
                horizontalalignment="center",
                verticalalignment="center",
            )
