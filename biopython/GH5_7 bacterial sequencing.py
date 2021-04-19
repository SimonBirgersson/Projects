# biopython - GH5_7 bacterial sequence phylogeny
import Bio              # biopython
from Bio import SeqIO   # sequence handling
from Bio import AlignIO # Alignment handling
from Bio import Phylo   # Phylogeny handling

import matplotlib as plt # figure handling

from fasta_cleaner import sequence_cleaner # own script that removes duplicate sequences from fasta files

sequence_cleaner("/Users/SimonsFolder/Projects/biopython/FASTA_GH5_7_bact_20200617.fasta")

list_fasta = SeqIO.parse("/Users/SimonsFolder/Projects/cleaned.fasta","fasta") # reads a .fasta file with several entries

with open("/Users/SimonsFolder/Projects/biopython/MSA_GH5_7_b_20210415.aln","r") as aln:
  alignment = AlignIO.read(aln,"clustal") # reads a clustal alignment file
#print(type(alignment))

# Open and initiate the distance calculator using the 'identity' model
from Bio.Phylo.TreeConstruction import DistanceCalculator # this is used for distance calculation
calculator = DistanceCalculator('identity') # this is one of the available models used for disttance calculations

# write the distance matrix
distance_matrix = calculator.get_distance(alignment) 

# open and initiate the Tree constructor
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor # this is used for tree construction
constructor = DistanceTreeConstructor(calculator)

# Build the Tree
tree = constructor.build_tree(alignment)
tree.rooted= True

# save the new tree file in working directory
# Phylo.write(tree,"GH5_7_b_tree_20210415.xml","phyloxml")
tree = Phylo.read("/Users/SimonsFolder/Projects/GH5_7_b_tree_20210415.xml","phyloxml")

# now for plotting

import matplotlib
import matplotlib.pyplot as plt

# generate quick tree in terminal using ASCII representation: 
# Phylo.draw_ascii(tree) 

# simple code block for making the figure pretty
fig = plt.figure(figsize=(13, 5), dpi=100) # create figure & set the size 
matplotlib.rc('font', size=12)             # fontsize of the leaf and node labels 
matplotlib.rc('xtick', labelsize=10)       # fontsize of the tick labels
matplotlib.rc('ytick', labelsize=10)       # fontsize of the tick labels
#turtle_tree.ladderize()		   # optional way to reformat your tree 
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=axes)
#fig.savefig("tree_cladogram")




