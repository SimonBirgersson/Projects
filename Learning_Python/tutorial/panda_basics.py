# pandas basic
# high-level data manipulation tool based on Numpy

# can store tables in "Dataframe", with a column of a dictionary of variables of and rows of observations.

dict = {"country":   ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital":    ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area":       [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict) # generates dataframe of the dictionary
brics.index = ["BR", "RU", "IN", "CH", "SA"] # changes indices from 0 - 4 to nation two letter codes
print(brics)

# can also read csv files via pd.read_csv


# indexing is done via square brackets
print(brics['country']) # prints a panda series

print(brics[['country']]) # Double brackets prints country column as dataframe

print(brics[['country','area']]) # this prints both columns

# You can also use data selection loc and iloc
print(brics.iloc[3]) # prints information for china in this case

print(brics.loc[['BR','SA']]) # prints out according to the indices
 
