# funcs

import numpy as np
import pandas as pd


def molecular_mass_calculator(string: str):
    """
    Calculate and returm "mass", i.e molecular mass in g/mol for "string" containing atomic formula for molecule
    \n\n        ex) "C2H6O" -> 46.07 g/mol

    To be added:
        - make () work, i.e C6(OH)4
        - also make number <9 work
    """

    # import periodic table of elements as pandas dataframe:
    df = pd.read_csv(
        "/Users/simon/Documents/Projects/Data Analysis Scripts/buffer_calculator/Periodic Table of Elements.csv",
        sep=",",
        header=0,
        usecols=["Symbol", "AtomicMass"],
    )

    # look at each char in string
    mass = []
    for i, symbol in enumerate(string):

        # if it is a integer, then multply previous atom by it
        if symbol.isdigit():
            if float(symbol) > 1:
                mass.append(
                    float(df[df["Symbol"].str.fullmatch(string[i - 1])]["AtomicMass"])
                    * (float(symbol) - 1)
                )

        # if it is a letter, then extract the corresponding atomic mass and add it to list
        elif symbol.isalpha():
            mass.append(float(df[df["Symbol"].str.fullmatch(symbol)]["AtomicMass"]))

        # if it isnt a letter or a number, send error
        else:
            return print("i'm confused...")
    return sum(mass)


def HH_approx(pH: float, pKa: float):
    """ 
    Enter a pH and pKa and returns the molar ratio of weak acid and conjugate base. Based on the Henderson Hendelbach approximation:

    pH = Ka * [HA]/[A-], where Ka = 10^(-pKa) -> [HA]/[A-] = pH / 10^(-pKa)
    """
    return pH / (10 ** (-pKa))


def UI_buffer_choice(df: pd.DataFrame):
    """ UI asking for which buffer """
    print("Which Buffer?")

    for i, column in enumerate(df["Buffer"]):  # iterate over buffers in excel sheet
        print(f"{i}. {column}")

    # get user choice via input()
    while True:

        # check for valid option, only integers accepted
        try:
            return df.iloc[int(input()), :]

        # if not int, the repeat the while loop
        except ValueError:
            print("That wasn't a valid choice...\n Please try again:")


def UI_buffer_protocol(
    buffer: pd.DataFrame, conc: float, volume: float, pH: float, m_acid: float
):
    print(f"\nProtocol for making {buffer['Buffer']}:")
    print(
        f"1. Weigh {m_acid:.2f}g of your salt and dissolve it in {volume*0.8:.1f} L of MilliQ water"
    )
    print(f"2. Adjust pH using HCl / NaOH to final pH {pH:.1f}")
    print(
        f"3. Top up with MilliQ water up to {volume:.1f} L, giving final concentration of {conc:.1f} M "
    )


def buffer_calculator(conc: float, volume: float, pH: float):
    """ """

    # Load excel sheet of buffer salt data
    df = pd.read_excel(
        "/Users/simon/Documents/Projects/Data Analysis Scripts/buffer_calculator/buffers.xlsx",
    )

    # let's user choose buffer and check if within pH range:
    while True:
        buffer = UI_buffer_choice(df)

        # if not within range, have user pick new buffer type
        if buffer["low pH range"] <= pH <= buffer["high pH range"]:
            break
        else:
            print(
                f"this buffer is out of range, maybe try another one? \n({buffer['Buffer']}: pH {buffer['low pH range']}-{buffer['high pH range']}, and yours is pH {pH})\n\n"
            )

    # calculate molar ratio of weak acid / conjugate base
    ratio = HH_approx(pH=pH, pKa=buffer["pKa"])

    # calculate molar concentration of acid and base
    # total conc = [HA] + [A-], ratio = [HA]/[A-]
    c_acid = (conc * ratio) / (ratio + 1)
    c_base = c_acid / ratio

    # molar amount by multiplying by volume
    n_acid = c_acid * volume
    n_base = c_base * volume

    # calculate weight required of acid
    m_acid = n_acid * buffer["MW [g/mol]"]

    # provide protocol for user
    UI_buffer_protocol(buffer=buffer, conc=conc, volume=volume, pH=pH, m_acid=m_acid)


if __name__ == "__main__":
    # molecular_mass_calculator(r"C2H4O")
    buffer_calculator(conc=1, volume=1, pH=5.5)
