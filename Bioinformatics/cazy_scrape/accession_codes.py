# function file for getting genbank accession codes from large cazy organism lists.
import re
import urllib.request  # allows to access internet pages
from datetime import date  # allows for time and day

from utils.timer import timer


@timer
def get_all_accession_codes(
    all_path: str,
    your_slice_path: str,
    cell_type: str = "Eukaryota",
    end_location_path: str = None,
):
    """
    Function that finds the organisms matching "cell_type" (default is Eukaryote) matching those "your_slice_path" in the master file "all_path" and fetches the genbank accession number in file "acc_codes" located in "end_location_path"

    all_path is the complete GH family txt file that can be downloaded at cazy, whilst your_slice_path is found by downloading all the organisms that have an GHx enzyme beloning to a certain family, subfamily etc. (my first case was all fungal GH5 enzymes)
    """

    print(
        f"Trying to finds matching species names in: \n 0. {all_path}\n 1. {your_slice_path}..."
    )
    # opens and reads all_path file into a list
    with open(
        all_path,
        "r",
        encoding="utf-8",
    ) as f:
        all_species = f.readlines()

    # opens and reads your_slice_path into a list
    with open(
        your_slice_path,
        "r",
        encoding="utf-8",
    ) as f:
        slice_species = f.readlines()

    # extremely suboptimized loop for getting acc codes from matching organisms
    accession_codes = []

    # for each GH5 enzyme:
    for line in all_species:

        # if the organism belongs to your cell type of choice, like "Eukaryota"
        if cell_type in " ".join(line.split()):

            # for each organism in the slice list:
            for slice_line in slice_species:

                # if the first three words in the slice is in the master list (should be species name):
                if " ".join(slice_line.split()) in " ".join(line.split()):

                    # if so, add the last word of that line to list "accesion codes"
                    accession_codes.append("".join(line.split()[-1]))

    # if this list isn't empty:
    if accession_codes:

        # remove duplicates that are formed due to suboptimized code
        accession_codes = list(dict.fromkeys(accession_codes))

        # create file in end path location
        text_file = open(
            end_location_path + str(date.today()),
            "w",
            encoding="utf-8",
        )

        # then write each accession code as comma separated value.
        text_file.write(
            ",".join(accession_codes)
        )  # fills the file with all the genbank codes
        text_file.close()

        print(
            f"File written successfully, {len(accession_codes)} matching sequences where found.\n"
        )

    else:
        print("file of accession codes were empty and could not be written")


@timer
def get_characterized_accession_codes(url: str):
    """currently only works for 1 page (looks at HTML code for entered url)

    returns: list of accession codes
    """

    # download and read the HTML-code for the given url
    u = urllib.request.urlopen(url).read()

    # regex to find all elements surrounded by <b>, i.e links etc. in cazy
    hits = re.findall("<a((.|\s)+?)</a>", str(u))

    # for each element in HTML code
    str1 = ""
    for ele in hits:

        # divide hits into lines
        str1 += str(ele)

    # divides list wherever )( appears
    str2 = str1.split(")(")

    # find genbank acc number in links
    start = "protein&val="  # the characteristics is like this: protein&val="CODE GOES HERE" target=_link>
    end = " target=_link>"
    code = []

    # Saves the accession codes in "code"
    for line in str2:

        # if line is a link
        if re.match("(.*)protein&val=(.*)", line):

            # find whatever is in between "start" and "end", i.e. code
            results = re.search("%s(.*)%s" % (start, end), line)

            # put accession codes in list
            code.append(results.group(1) + ",")  # uniprot codes in a lis

    return code


if __name__ == "__main__":
    hej = get_characterized_accession_codes(
        url="http://www.cazy.org/GH36_characterized.html"
    )

    for line in hej:
        print(f"{type(line)}: {line}")
