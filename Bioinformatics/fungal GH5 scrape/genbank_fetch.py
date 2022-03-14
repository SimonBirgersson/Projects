# getting FASTA files from genbank accession codes
import webbrowser

from timer import countdown


def get_fasta(acc_codes: str):
    """Short function that opens new tab in web browser to dowload accession codes in "acc_codes", which is a comma seperated string of all desired accession codes. Be careful not to include to many."""
    webbrowser.open(
        "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=fasta&retmode=text&id="
        + acc_codes,
        new=2,
    )


def get_fasta_in_chunks(
    acc_codes_path: str, wait_time: int = 5, size_of_chunks: int = 360
):
    """if you file of accession codes is to big ()>~400 sequences), this function divides the file in chunks and submits, getting several FASTA files"""
    with open(
        acc_codes_path,
        "r",
        encoding="utf-8",
    ) as f:
        acc = f.read()

    acc = acc.split(",")

    # divides the huge list of acc codes into nth sized chunks
    # API limit is 3, query size limit is between 360-400

    # chunk size
    n = size_of_chunks

    # for the least amount of nth sized chunks + 1 remainder
    for i in range(round(len(acc) / n)):

        # if API-query limit is reached i.e every three iterations, wait for t seconds
        if i % 3 == 0 and i != 0:
            t = 5
            print(f"API query limit reached, sleeping for {t}s to wait...")
            countdown(wait_time)

        if i == 0:
            print("first one!")
            get_fasta(",".join(acc[: n * (i + 1)]))

        # then get FASTA-file for current chunk!
        get_fasta(",".join(acc[n * i : n * (i + 1)]))

        # if it's the final chunk:
        if i == round(len(acc) / n) - 1:
            print("LAST ONE!")
            get_fasta(",".join(acc[n * i :]))

        print(
            f"\nfetching FASTA file #{i} containing accession codes {n * i } -> {n * (i + 1)}, (length: {len(acc[n * i : n * (i + 1)])}) seqs. \n\n"
        )
