# getting FASTA sequences of each fungal GH5 enzyme in a file
from datetime import date  # allows for time and day

from accession_codes import get_accession_codes
from genbank_fetch import get_fasta, get_fasta_in_chunks
from merge_fasta import merge_fasta

# clears terminal window
# os.system("clear")

# All fungal GH5 sequences
# export path for accession codes
FILE_PATH = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/"
FILE_NAME = "fungal_GH5_genbank_Acc_codes_"

# path to file of all genbank accession codes for given family
PATH_ALL = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_all.txt"

# path to file with smaller group to be used as key for getting accession codes
PATH_FUNGAL = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_fungal.txt"

"""
# Just GH5_7 fungal sequences
# export path for accession codes
FILE_PATH = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/"
FILE_NAME = "fungal_GH5_7_genbank_Acc_codes_"

# path to file of all genbank accession codes for given family
PATH_ALL = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_7_all.txt"

# path to file with smaller group to be used as key for getting accession codes
PATH_FUNGAL = (
    "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_7_fungal.txt"
)

"""
# allowed length of single FASTA file, before merging chunks
N = 360

# call on function to get all accession codes in file, TAKES LONG TIME RUN ONLY ONCE.
get_accession_codes(PATH_ALL, PATH_FUNGAL, "Eukaryota", FILE_PATH + FILE_NAME)


# check how many accession codes are in file:
with open(
    FILE_PATH + FILE_NAME + str(date.today()),
    "r",
    encoding="utf-8",
) as f:

    # read contents of genbank accession code file:
    acc = f.read()

    # if 'acc' contains fewer than N seqs, just get single file:
    if len(acc.split(",")) <= N:
        print(f"fetching {len(acc.split(','))} FASTA seqs in a single file...")
        get_fasta(acc)

    # if longer, get fastas in chunks, then merge them:
    elif len(acc.split(",")) > N:
        print(
            "The amount of accession codes in your file is too high to get in one file, chunking is required... \n"
        )
        # call on function to download all FASTA files in 360 seq-sized chunks:
        get_fasta_in_chunks(
            FILE_PATH + FILE_NAME + str(date.today()),
            5,
            N,
        )

        # Here the user should put their newly downloaded FASTA chunks into a folder, then paste folder path into terminal.
        FASTAS_PATH = input("Please input path to FASTA files: ")
        merge_fasta(FASTAS_PATH + "/")
