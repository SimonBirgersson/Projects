# PDF merger 220723
"""
    This script will merge all pdf:s in directory "directory" to one file named  "combined_document.pdf"
    can be ran from terminal in the directory with pdf be entering:

    python3 /Users/simon/Documents/Projects/utils/pdf_merger.py

    UPDATE:
     made .sh-script "merge_pdf.sh that can be ran in terminal 
"""
import os

import PyPDF2

from timer import timer


@timer
def pdf_merger(directory: "str" = None):
    """compiles all pdf files in a directory into one file"""

    # if ran from terminal, get current directory
    if directory is None:
        directory = os.curdir

    # create merger object
    merger = PyPDF2.PdfFileMerger()

    # for each file in directory
    for i, file in enumerate(os.listdir(directory)):
        if file.endswith(".pdf"):
            print(f"merging file {file}... ({i+1}/{len(os.listdir(directory))-1})")

            # merge the files
            merger.append(directory + file)

        # create merged file
        merger.write(directory + "combined_document.pdf")


def main():
    """main script"""

    # merge all pdfs in dokuments folder
    # pdf_merger("/Users/simon/Documents/Dokument/")

    # run function without argument for terminal use
    pdf_merger()


# run main function if this is the script being ran
if __name__ == "__main__":
    main()
