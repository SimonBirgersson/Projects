#!/usr/bin/env python
# Script that downloads all fasta sequences for a given Cazy family

# Written by Simon Birgersson 040220

# Importing some libraries of commands here
import urllib.request
import pickle
from bs4 import BeautifulSoup
from datetime import date
import os
import re
import requests
today=str(date.today())

# Prompt that asks for an url
#site=input("Hello! please type your URL and this command will download the FASTA sequences into 1 handy .txt-file for MSA \n")
#print(site)

url="http://www.cazy.org/GH113_bacteria.html"
u=urllib.request.urlopen(url).read() # Download the HTML-code for the given url
soup=re.findall('<a((.|\s)+?)</a>', str(u)) # Finds all elements surrounded by <a>, i.e links etc.

# Divides the results into lines for visibility / handling
str1=""
for ele in soup:
    str1+=str(ele)

str2=str1.split(")(")

# Searches for uniprot codes in the links for protein entries
start='href="http://www.uniprot.org/uniprot/'
end='" target="_link">'
code=[]
for line in str2:
    if re.match('(.*)href="http://www.uniprot.org/uniprot/(.*)',line):
        results=re.search('%s(.*)%s' % (start, end), line)
        code.append(results.group(1)) # uniprot codes in a list

# Generates FASTA-sequence links for uniprot codes
def prepend(list,str): # creating a quick function for adding str to beginning of ele in list
    str += '{0}'
    list=[str.format(i) for i in list]
    return(list)

mylist=prepend(code,"https://www.uniprot.org/uniprot/") # using the new func

mynewlist=[x+".fasta" for x in mylist] # appending str to every ele in list


############################################################################

# Downloads the FASTA and genereates the text file
response=[]
for x in mynewlist:
    response.append(urllib.request.urlopen(x).read())
response1=str(response[1:])
output=response1.replace('[','')
output=output.replace(']','')
output=output.replace('b\'','')
output=output.replace('\n','')
output=output.replace('\'','')
output=output.replace(' \>','>')
output=output.replace(', ','')
# Saves it to the local directory as "FAST_MSA_mmddyyyy"
text_file=open("FASTA "+today,"w")
text_file.write(output)
#text_file=open("FASTA "+today,"a+",newline="\n")
text_file.close()
