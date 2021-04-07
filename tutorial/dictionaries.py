# dictionaries 20210326

# A dictionary is a data type similar to arrays, but works with keys and values instead of indices.
# So, it's essentially an array accessible via keys instead of indices

# Example:
phonebook = {}
phonebook["John"] = 235971349761
phonebook["Jack"] = 349172394761
phonebook["Jill"] = 124168408557
print(phonebook)

# Another way of entering a dictionary:
phonebook = {
    "John" : 235971349761,
    "Jack" : 349172394761,
    "Jill" : 124168408557
}
print(phonebook)

# Dictionaries can be iterated over in similar way to arrays
for name, number in phonebook.items():
    print("Phone number of %s is %d"  % (name, number))

# removing a value from a dictionary
del phonebook["John"]
print(phonebook)

# another way, using "pop"
phonebook.pop("Jack")
print(phonebook)

# EXCERCISE
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
# your code goes here
phonebook["Jake"] = 938273443

phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
