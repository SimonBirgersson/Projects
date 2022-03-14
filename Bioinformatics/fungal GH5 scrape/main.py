# getting FASTA sequences of each fungal GH5 enzyme in a file
import os

from accession_codes import get_accession_codes
from genbank_fetch import get_fasta, get_fasta_in_chunks

# clears terminal window
os.system("clear")

# paths for accesion codes fetching
"""PATH_ALL = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_all.txt"
PATH_FUNGAL = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_fungal.txt"
FILE_PATH = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/fungal_GH5_genbank_Acc_codes_"
"""
# Just GH5_7 fungal sequences
PATH_ALL = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_7_all.txt"
PATH_FUNGAL = (
    "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_7_fungal.txt"
)
FILE_PATH = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/fungal_GH5_7_genbank_Acc_codes_"


# call on function to get all accession codes in file, TAKES LONG TIME RUN ONLY ONCE.
get_accession_codes(PATH_ALL, PATH_FUNGAL, "Eukaryota", FILE_PATH)

# call on function to download all FASTA files in 360 seq-sized chunks:

"""get_fasta_in_chunks(
    "/Users/simon/OneDrive - Lund University/Fungal GH5 order/fungal_GH5_7_genbank_Acc_codes_2022-03-10",
)"""


"""
with open(
    "/Users/simon/Documents/Projects/Bioinformatics/fungal GH5 scrape/gh5_7 slice.txt",
    "r",
    encoding="utf-8",
) as f:
    acc = f.read()
get_fasta(acc)
"""
