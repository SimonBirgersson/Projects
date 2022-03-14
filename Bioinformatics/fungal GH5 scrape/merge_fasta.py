# Merge chunked FASTA files in single .txt, clustal omega MSA can only do MSA for files <10.48576 MB ≈ 3008.20983607 AA-seq
import fnmatch
import os

PATH = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_7 FASTA/"

# create empty strings
DATA = NEWFILE = ""

# for each ".fasta" file in PATH:
print("Merging all .fasta files in the chosen directory...")
for i, file in enumerate(fnmatch.filter(os.listdir(PATH), "*" + ".fasta")):
    print(f"{i}: {file}")
    # open file
    with open(PATH + file, encoding="utf-8") as f:

        # read contents as str:
        DATA = f.read()

        # if this isn't the first iteration, add newline between chunks
        if i != 0:
            NEWFILE = NEWFILE + "\n"

        # then add next chunk
        NEWFILE = NEWFILE + DATA

# create new file with complete sequences in:
with open(PATH + "complete_seqs.fasta", "w", encoding="utf-8") as f:
    f.write(NEWFILE)
