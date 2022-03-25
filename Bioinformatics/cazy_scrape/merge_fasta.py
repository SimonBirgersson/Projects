import fnmatch
import os

from utils.timer import timer


@timer
def merge_fasta(path):
    """
    Merge chunked FASTA files in single .txt, clustal omega MSA can only do MSA for files <10.48576 MB ≈ 3008 seqs

    CAUTION: after running the function the .fasta file with complete seq in ends up in the same folder as the chunks were, re-running the script will merge the complete seqs with the chunks yielding duplicates.
    """

    # create empty strings
    DATA = NEWFILE = ""

    # for each ".fasta" file in path:
    print("Merging all .fasta files in the chosen directory...")
    for i, file in enumerate(fnmatch.filter(os.listdir(path), "*" + ".fasta")):
        print(f"{i}: {file}")
        # open file
        with open(path + file, encoding="utf-8") as f:

            # read contents as str:
            DATA = f.read()

            # if this isn't the first iteration, add newline between chunks
            if i != 0:
                NEWFILE = NEWFILE + "\n"

            # then add next chunk
            NEWFILE = NEWFILE + DATA

    # create new file with complete sequences in:
    with open(path + "complete_seqs.fasta", "w", encoding="utf-8") as f:
        f.write(NEWFILE)
    print(
        "Finished! file named 'complete_seqs.fasta' should now be in the same folder as the fasta seqs."
    )
