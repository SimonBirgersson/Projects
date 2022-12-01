import matplotlib.pyplot as plt
from utils.maldi_tof import load_ms_csv, plot_ms

if __name__ == "__main__":

    data = load_ms_csv(
        r"/Users/simon/Library/CloudStorage/OneDrive-LundUniversity/Current Projects/GH130 paper/MALDI-ToF data/RhMOP130A synthesis reactions AM1 M2 221101/"
    )

    # allyl-hexose weight with Na aducts up AH6+Na
    AHX_mz = [243.084, 405.137, 567.190, 729.243, 891.296, 1053.349]

    # oligo-hexose weight with Na aducts up M12
    MX_mz = [
        203.053,
        365.106,
        527.159,
        689.212,
        851.265,
        1013.318,
        1175.371,
        1337.424,
        1499.477,
        1661.530,
        1823.583,
        1985.636,
    ]

    # data["RhMOP130A AM1 M1P TRIS 1 dil 221101"]["mz"] = data[
    #    "RhMOP130A AM1 M1P TRIS 1 dil 221101"
    # ]["mz"].subtract(16.18)

    # list available spectra
    for i, spectrum in enumerate(data.keys()):
        print(f"{i}. {spectrum}")

    # plot spectra
    plot_ms(
        plots=[
            ["RhMOP130A AM1 M1P Citrate 221101"],
            ["RhMOP130A M2 M1P Citrate 2 221101"],
            ["AM1 M1P citrate ctrl 221101", "M2 M1P Citrate ctrl 221101"],
        ],
        df=data,
        xlim=(200, 1100),
        ylim=(0, 60_000),
        check=MX_mz,
    )

    # plot text
    """for i, x in enumerate(AHX_mz):
        plt.text(x, 86000 / (i + 1), f"AM{i+1} + Na", ha="center")"""

    plt.show()

    # save fig in this directory
    save_path = "/Users/simon/Library/CloudStorage/OneDrive-LundUniversity/Current Projects/GH130 paper/figures/MS figs"

    # save figure
    """
    plt.savefig(
        f"{save_path}/AM1_M2_elong_screening_221107.pdf",
        dpi=400,
        bbox_inches="tight",
        transparent=True,
    )
    """
