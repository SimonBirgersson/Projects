# percent identity matrix plot from ClustalOmega 220317
import os

import pandas as pd
import seaborn as sns

os.system("clear")
PATH = "/Users/simon/OneDrive - Lund University/Fungal GH5 order/GH5_7 FASTA/percent_identity_matrix.txt"

with open(
    PATH,
    "r",
    encoding="utf-8",
) as f:

    values = []
    for line in f:  # splits on ',' as per your question example
        line = line.split(" ")
        values.append(line)

values[:] = [x for x in values if x == ""]
for line in values:
    print(str(line).strip())


"""
ax = sns.heatmap(data.to_numpy())

# prints the dataframe
# print(data)

ax.set_title(
    f"Predicted Aligned Error (PAE) for {NAME}"
    if NAME != 0
    else f"Predicted Aligned Error (PAE)"
)
ax.set_xlabel("Aligned AA-sequence")
ax.set_ylabel("Scored AA-sequence")

plt.show()
"""
