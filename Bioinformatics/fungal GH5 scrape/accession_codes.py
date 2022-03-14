# function file for getting genbank accession codes from large cazy organism lists.
from datetime import date  # allows for time and day


def get_accession_codes(
    all_path: str,
    your_slice_path: str,
    cell_type: str = "Eukaryota",
    end_location_path: str = None,
):
    """Function that finds the organisms mathing "cell_type" (default is Eukaryote) in "your_slice_path" in the master file "all_path" and fetches the genbank accession number in file "acc_codes" located in "end_location_path"
    all_path is the complete GHX family file that can be downloaded at cazy, whilst your_slice_path is found by downloading all the organisms that have an GHx enzyme beloning to a certain family, subfamily etc. (my first case was all fungal GH5 enzymes)"""

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
        # if cell_type in line:

        # for each organism in the slice list:
        for slice_line in slice_species:

            # if the first three words in the slice is in the master list (should be species name):
            if " ".join(slice_line.split()) == " ".join(line.split()[2:-1]):
                print(
                    f"match! {' '.join(slice_line.split())} = {' '.join(line.split()[2:-1])}"
                )
                # if so, add the last word of that line to list "accesion codes"
                accession_codes.append(line.split()[-1])

            else:
                print("Error")

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
    else:
        print("file of accession codes were empty and could not be written")
