#!/usr/bin/env python
# Script that downloads all fasta sequences for a given Cazy family

# Written by Simon Birgersson 20200604

import re

# Importing some libraries of commands here
import urllib.request  # allows to access internet pages
import webbrowser  # allows manipulation of standard web browser
from datetime import date  # allows for time and day

today = str(date.today())

url = "http://www.cazy.org/GH5_7_bacteria.html?debut_TAXO=300#pagination_TAXO"  # enter you url here, only works for cazy!
u = urllib.request.urlopen(url).read()  # Download the HTML-code for the given url
soup = re.findall(
    "<a((.|\s)+?)</a>", str(u)
)  # Finds all elements surrounded by <a>, i.e links etc. in cazy

# Divides the results into lines for visibility / handling
str1 = ""
for ele in soup:  # generates lists of text in "soup"
    str1 += str(ele)

str2 = str1.split(")(")  # divides list wherever ")(" appears

# Searches for genbank accesion codes in the links for protein entries
start = "protein&val="  # the characteristics is like this: protein&val="CODE GOES HERE" target=_link>
end = " target=_link>"
code = []
for line in str2:  # Saves the accession codes in "code"
    if re.match("(.*)protein&val=(.*)", line):
        results = re.search("%s(.*)%s" % (start, end), line)

        code.append(results.group(1) + ",")  # uniprot codes in a list


############################################################################
output = "".join(code)  # converts to str, unsure if optimal
text_file = open(
    "genbank_Acc_codes_" + today, "w"
)  # names and creates a file to be saved in local directory
text_file.write(output)  # fills the file with all the genbank codes
text_file.close()

# opens your standard webrowser and opens a page that prompts a download of all of the desired fasta sequences
webbrowser.open(
    "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=fasta&retmode=text&id="
    + output,
    new=2,
)

# new feautures:
# want to fetch refseq if possible
