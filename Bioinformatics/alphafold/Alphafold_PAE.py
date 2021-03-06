# PAE.json (structure) plotter

import json
import math
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# clears terminal window
os.system("clear")

# function that splits lists into N-sized chunks
def list_split(LIST, n):
    """splits long list into n equally sized chunks."""
    for x in range(0, len(LIST), n):
        every_chunk = LIST[x : n + x]

        if len(every_chunk) < n:
            every_chunk = every_chunk + [None for y in range(n - len(every_chunk))]
        yield every_chunk


# name of protein
NAME = "RhGal36A"
# AA_SEQ of the protein
AA_SEQ = r"MGMIKADGHIFVLETAHTTYCFRRMETGHLEHLYYGRHLTLPEHPAECDVAPLVEKHTFAPGNTNLCDGEHPAFS LEDMRLEMSSYGKGDIREPFVEIVHADGSTTSDFRYESYEITEKTAGTENGDLPGAYDEKGEAQRLSVRLRDHSY DLVLELHYDVYAECDAIVRSAVLFNESGETVRLNRLMSTQIDFDPAEYVFTTFTGAWAREMHRSDTRMEAGKHVN ASYTGTSSSRANPFVMIAKTDTTEDTGECYGCNLIYSGNHYEAAEVSGYGKMRLTAGINPQSFSWLLAPGENFAA PEAVMAYSCEGYNGMSQCMHAFVREHIVRGAFKHKVRPVLLNSWEAAYFDINERKLLALAKKAKEAGVELFVMDD GWFGERNDDAHSLGDWEVNEKKLPGGLAGLGRKIKALGLDFGIWVEPEMVNVNSHLYQAHPDWTIEIPGKPHAEG RNQRILDLTRTEVQDYIIETMTNVFSSAEISYVKWDMNRTFTDYYSGALPPERQGEVAHRYVLGLYRCMRELTAR FPDILFEGCSAGGNRFDLGILSYFPQIWASDDTDALCRAEIQTGYSYGYPMSVVSAHVSACPNHQTLRVTPLETR FAVAAFGICGYECNFCDLSREDFAAVKAQIALYKQWREVLQKGRFYRGRTFGEGAHESVLSQSAGNQMEWTCVSE DQTRAVGMLMQKLVVPNTQYHSYHAKGLKPDARYHFYNRSLKYNIKDFGDLVNTVSPVHIKQDSLALDLIARFKK MDGEIEDCHVAGDMLMYHGVKLKQAFGGTGYNNEVRYFQDFAARMYFMEEEKGHADSGEAEEKERAA"

TICKS = 30

PATH = r"/Users/simon/OneDrive - Lund University/RhGal36A/AlphaFold RhGal36B/predicted_aligned_error.json"


def predicted_aligned_error_plot(PATH, AA_SEQ=0, NAME=0, TICKS=30):
    """function for reading and plotting the PAE.json file that comes with each AlphaFold structure download. Independent of the 3D structure, AlphaFold produces an output called “Predicted Aligned Error”.

    The colour at (x, y) indicates AlphaFold’s expected position error at residue x if the predicted and true structures were aligned on residue y.
    If the predicted aligned error is generally low for residue pairs x, y from two different domains, it indicates that AlphaFold predicts well-defined relative positions for them.
    If the predicted aligned error is generally high for residue pairs x, y from two different domains, then the relative positions of these domains in the 3D structure is uncertain and should not be interpreted.

    The Predicted Aligned Error (PAE) is displayed as an image for each of the structure predictions. If you need the raw data with PAE for all residue pairs, you can download the PAE in a JSON format using the button at the top of the structure page.
    """

    # open PAE.json file from alphafold
    f = open(PATH, "r")

    # read file, then close it.
    data = json.load(f)
    f.close()

    # convert to Dataframe
    df = pd.DataFrame.from_dict(data)

    # residue1 is columns, residues 2 is rows, rename columns and index to corresponding residues
    if AA_SEQ != 0:

        # converts the string into list of AA with AA number as well
        AA = [AA + str(i + 1) for i, AA in enumerate(AA_SEQ)]

        # splits distance list of size res^2 into res sized lists
        split_list = list(list_split(df["distance"][0], len(AA_SEQ)))

        # create matrix of data with indices/rows as AA
        data = pd.DataFrame(
            split_list,
            columns=AA,
            index=AA,
        ).transpose()

        # plots heatmap of data, low (dark) values are better fitted.
        ax = sns.heatmap(data.to_numpy())

        try:
            # sets x ticks as AA sequence
            ax.set_xticks(range(0, len(AA), TICKS))
            ax.set_xticklabels(AA[::TICKS])

            # sets y ticks as AA sequence
            ax.set_yticks(range(0, len(AA), TICKS))
            ax.set_yticklabels(AA[::TICKS])

        except ValueError:
            print("somethings up with the AA sequence")

    else:
        # splits distance list of size res^2 into res sized lists
        split_list = list(
            list_split(df["distance"][0], math.isqrt(len(df["distance"][0])))
        )

        data = pd.DataFrame(
            split_list,
        ).transpose()

        # plots heatmap of data, low (dark) values are better fitted.
        ax = sns.heatmap(data.to_numpy())

    # prints the dataframe
    # print(data)

    ax.set_title(
        f"Predicted Aligned Error (PAE) for {NAME}"
        if NAME != 0
        else f"Predicted Aligned Error (PAE)"
    )
    ax.set_xlabel("Aligned AA-sequence")
    ax.set_ylabel("Scored AA-sequence")

    plt.show()


predicted_aligned_error_plot(PATH, AA_SEQ, NAME)
