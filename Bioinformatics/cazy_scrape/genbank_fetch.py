# getting FASTA files from genbank accession codes
import webbrowser

from utils.timer import countdown, timer


@timer
def get_fasta(acc_codes: str):
    """
    Short function that opens new tab in web browser to dowload accession codes in "acc_codes", which is a comma seperated string of all desired accession codes.

    CAUTION: need to be read before inputted, do not input the path to the file. Be careful not to include to many seqs here, might be difficult to fetch more than ~360.
    """
    webbrowser.open(
        "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=fasta&retmode=text&id="
        + acc_codes,
        new=2,
    )


@timer
def get_fasta_in_chunks(
    acc_codes_path: str, wait_time: int = 5, size_of_chunks: int = 360
):
    """
    if you file of accession codes is to big (>~400 sequences), this function divides the file in chunks and submits each chunk to genbank API, getting several FASTA files in your downloads folder
    """
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

    print(
        f"Fetching sequences in chunks with {n} seqs each, which should yield {round(len(acc) / n)} files with remaining {len(acc)-(round(len(acc) / n)*n)} seqs in final chunk."
    )

    # for the least amount of nth sized chunks + 1 remainder
    if round(len(acc) / n) == 0:
        print("Too few sequences for chunking! try 'get_fasta' function instead.")
    for i in range(round(len(acc) / n)):
        print(i)
        # if API-query limit is reached i.e every three iterations, wait for t seconds
        if i % 3 == 0 and i != 0:
            t = 5
            print(f"API query limit reached, sleeping for {t}s to wait...")
            countdown(wait_time)

        # if its the first file:
        if i == 0:
            print(
                f"\nfetching the first FASTA file #{i} containing accession codes {0} -> {n * (i + 1)}, (length: {len(acc[: n * (i + 1)])})\n\n"
            )

            # get fasta for first chunk
            get_fasta(",".join(acc[: n * (i + 1)]))

        # if it's the final chunk:
        elif i == round(len(acc) / n) - 1:
            print(
                f"\nfetching the last FASTA file #{i} containing accession codes {n * i } -> {len(acc)}, (length: {len(acc[n * i : ])})\n\n"
            )

            # get final remainder of sequences
            get_fasta(",".join(acc[n * i :]))

        # if neither first nor last chunk:
        elif i != 0 and i != round(len(acc) / n) - 1:
            print(
                f"\nfetching FASTA file #{i} containing accession codes {n * i } -> {n * (i + 1)}, (length: {len(acc[n * i : n * (i + 1)])})\n\n"
            )
            # then get FASTA-file for current chunk
            get_fasta(",".join(acc[n * i : n * (i + 1)]))

    print("Finished! Files should be in your downloads folder.\n")
