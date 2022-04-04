from datetime import date

import matplotlib.pyplot as plt
from utils.maldi_tof import load_ms_csv
from utils.peaks import plot_vert

PATH = "/Users/simon/OneDrive - Lund University/Synergy paper/click chemistry/data/MALDI ToF/click metOH 220324/text files/"

df = load_ms_csv(PATH)


plots = ["sample 2", "AM1 ctrl 1", "DPAP ctrl 1", "3MPA ctrl 1", "metOH ctrl 1"]
# plots = ["sample 2"]


f, axs = plt.subplots(len(plots), 1, figsize=(10, 8), sharex=True, sharey=True)
for i, plot in enumerate(plots):

    mz = df[plot]["mz"]
    signal = df[plot]["signal"]

    if len(plots) > 1:
        ax = f.add_subplot(axs[i])

    for line in [243.08, 279.0997, 347.9897]:
        plot_vert(line)

    plt.plot(mz, signal, "-", color="black", linewidth=1)
    plt.xlabel("m/z")
    plt.ylabel("Signal")
    plt.xlim([200, 450])
    # plt.xlim([300, 370])
    plt.ylim([0, max(signal) * 1.05])
    plt.grid()
    plt.legend({plot}, loc="best")


plt.suptitle("Mass Spectrum - %s" % date.today())
plt.show()
