# Reading NMR data from bruker 220520
import os

import matplotlib.pyplot as plt
import nmrglue as ng
import numpy as np

from utils.timer import timer


@timer
def load_bruker(exp_dir: str = "."):
    """
    load topspin processed data from experiment directory e.g (your_experiment_folder/1)

    output:

    dict of experiment parameters

    data of processed spectrum.
    """

    # access processing file "1" within experiment directory
    file = os.path.join(exp_dir, "pdata", "1")

    # if this file does NOT exist:
    if not os.path.exists(file):
        return print("no such folder")

    # but if it does:
    else:

        # check if 1D, quite unessecary
        p1r = os.path.join(file, "1r")
        if os.path.exists(p1r):
            print("This is a 1D NMR spectrum.")

        # read Bruker data
        bruker_dic, bruker_data = ng.bruker.read_pdata(file)

        # Convert to pipe format
        C = ng.convert.converter()  # create converter object
        C.from_bruker(bruker_dic, bruker_data, udic=None, remove_digital_filter=False)
        dic, data = C.to_pipe()  # make into pipe format

        return dic, data


@timer
def plot_2d_spectrum(
    dics: list,  # list of dictionaries with exp param
    datas: list,  # list of x and y values
    ax,  # current axis
    channels: list[str],  # str of what channels used
    xlim: list[int],  # limits of x axis in plot
    ylim: list[int],  # limits of y axis in plot
    contour_num: int = 20,  # number of contour levels
    contour_factor: float = 2.50,  # scaling factor between contour levels
    contour_level_start: int = 150_000_000,  # lowest signal shown
    title: str = "2D NMR Spectrum",  # plot title
    names: list = None,  # names of spectra
    colors: list = None,  # color of plot
):
    """
    plots the spectrum in data

    input:

        data: np.array,
        cmap,
        channels: tuple(str, str) = ("1H", "15N"),
        figsize: tuple(int, int) = (15, 10),
        xlim: tuple(float, float) = (0, 10),
        ylim: tuple(float, float) = (100, 140),

    output:

        plot of the spectrum
    """

    # loop over the files and colors
    for dic, data, color, name in zip(dics, datas, colors, names):

        # make ppm scale for dimension 1
        uc_x = ng.pipe.make_uc(dic, data, dim=1)  # create unit conversion object
        ppm_x = uc_x.ppm_scale()  # create ppm scale
        ppm_x0, ppm_x1 = uc_x.ppm_limits()  # create left and right limt of ppm scale

        # make ppm scale for dimension 2
        uc_y = ng.pipe.make_uc(dic, data, dim=0)  # create unit conversion object
        ppm_y = uc_y.ppm_scale()  # create ppm scale
        ppm_y0, ppm_y1 = uc_y.ppm_limits()  # create left and right limt of ppm scale

        # calculate contour levels
        cl = contour_level_start * contour_factor ** np.arange(contour_num)

        # printing som plot info for user:
        print(f"Plotting spectrum in file: {name}")
        print(f"x-dim limits: {ppm_x0:.2f}, {ppm_x1:.2f}")
        print(f"y-dim limits: {ppm_y0:.2f}, {ppm_y1:.2f}")
        print(f"color: {color}\n\n")

        # plot the contours
        plot = ax.contour(
            data,
            cl,
            colors=color,
            extent=(ppm_x0, ppm_x1, ppm_y0, ppm_y1),
            linewidths=0.5,
        )

        # get plot legend, no colored lines?
        if name:
            plot.collections[0].set_label(f"{name} ({color})")

    # sets axis limit
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    # invert axis order
    ax.invert_xaxis()
    ax.invert_yaxis()

    # decorate the axes
    ax.set_xlabel(f"{channels[0]} (ppm)")
    ax.set_ylabel(f"{channels[1]} (ppm)")
    ax.legend(loc="best")
    ax.set_title(title)


@timer
def main():
    """
    exectubale part of script

    input:

    # cmap = matplotlib.cm.Reds_r  # contour map (colors to use for contours)
    """

    PATHS = [
        "/Users/simon/Library/CloudStorage/OneDrive-LundUniversity/BoMan26A NMR Project/nmr/BoMan26A_220519/2",
        "/Users/simon/Library/CloudStorage/OneDrive-LundUniversity/BoMan26A NMR Project/nmr/BoMan26A_220519/3",
    ]

    NAMES = ["BoMan26A 15°C 220519", "BoMan26A 4°C 220519"]

    COLORS = ["blue", "red"]

    # Gather all data in large list of tuples
    data_list = []
    for i, PATH in enumerate(PATHS):
        data_list.append(load_bruker(PATH))

    # split exp info and processed data into two lists
    dics, datas = [], []
    for spectrum in data_list:
        dics.append(spectrum[0])
        datas.append(spectrum[1])

    # plot style from R
    plt.style.use("ggplot")

    # create the figure
    fig = plt.figure(figsize=[15, 10])
    ax = fig.add_subplot(111)

    plot_2d_spectrum(
        names=NAMES,
        dics=dics,
        datas=datas,
        channels=["$^1H$", "$^{15}N$"],
        xlim=[6, 10],
        ylim=[105, 135],
        contour_level_start=150_000_000,
        colors=COLORS,
        ax=ax,
    )

    plt.show()


if __name__ == "__main__":
    main()
