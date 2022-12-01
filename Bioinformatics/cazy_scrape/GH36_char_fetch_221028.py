from accession_codes import get_characterized_accession_codes
from genbank_FASTA_fetch import get_fasta

if __name__ == "__main__":

    # get list of accession codes
    accession_codes = get_characterized_accession_codes(
        url="http://www.cazy.org/GH36_characterized.html"
    )

    # get fasta sequences of accession codes from NCBI
    get_fasta("".join(accession_codes))
