# Numpy arrays
# Great alternative to python lists, allows for matrix operations.

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# use numpy to calculate BMI
bmi = np_weight / np_height ** 2
print(bmi)

# Allows subsetting of matrices as well. For a boolean response:
bmi > 23

# Print only those observations above 23:
bmi[bmi > 23]

# EXCERCISE Convert The following lists to pounds.
# scalar conversion of 2.2lbs per kg to make my conversion

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)
