# GGM comp calculation
import matplotlib.pyplot as plt
import pandas as pd

# Quantative data for different galactoglucomannan purification fractions. TS = Total Solids, ASL = Acid Soluble Lignin, AIL = Acid Insoluble Lignin, SEC = Size Exclusion Chromatography, NMR = Nuclear Magnetic Resonance.
GGM_mass_comp = pd.DataFrame(
    {
        "STEX REF 2 liquid": [2.7, 21.1, 7.8, 7.9, 4.6, 4.6, 8.1, 10, 26.3, 6.1],
        "Membr. Conc. 50%VR": [
            6.8,
            9.7,
            5.5,
            4.4,
            1.7,
            5.5,
            9.4,
            10,
            32.3,
            5.7,
        ],
        "Diafiltration Retentate": [
            4.8,
            11.2,
            5.9,
            0.1,
            1.2,
            5.9,
            10.5,
            6.7,
            38,
            6.9,
        ],
    },
    index=[
        "TS [g/g]",
        "ASL [% of TSL",
        "AIL (% of TS)",
        "Monosaccharides (% of TS)",
        "Arabinan (% of TS)",
        "Galactan (% of TS)",
        "Glucan (% of TS)",
        "Xylan (% of TS)",
        "Mannan (% of TS)",
        "Acetate groups (% of TS)",
    ],
)
print(GGM_mass_comp)

# Calculated molar composition (corrected for bound state) [% mol/total mol]
GGM_mol_comp = pd.DataFrame(
    {
        "STEX REF 2 liquid": [
            7.97,
            6.80,
            11.97,
            12.13,
            38.86,
            22.27,
            100.000,
        ],
        "Membr. Conc. 50%VR": [
            2.66,
            7.33,
            12.53,
            15.64,
            43.06,
            18.78,
            100.000,
        ],
        "Diafiltration Retentates": [
            1.74,
            7.31,
            13.01,
            9.74,
            47.08,
            21.13,
            100.000,
        ],
    },
    index=[
        "Arabinan (% of TS)",
        "Galactan (% of TS)",
        "Glucan (% of TS)",
        "Xylan (% of TS)",
        "Mannan (% of TS)",
        "Acetate groups (% of TS)",
        "total percent",
    ],
)
print(GGM_mol_comp.T)

print(GGM_mol_comp.T["Galactan (% of TS)"])


print(GGM_mol_comp.T["Galactan (% of TS)"] * range(100))
