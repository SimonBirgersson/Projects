# tutorial #5: basic string operations
#strings are bits of text, they can be defined as anything between ""
astring = "Hello World!"
astring2 = 'Hello World'

# "" are the stricter separator, allows for use of '' inside the string
print("single quotes '' can be used within double quotes")
print(len(astring)) # new command, prints amount of characters in string

print(astring.index("o")) # this finds the index of the first "o" character, starts at zero

print(astring.count("l")) # instead retursn the amount of instances of the character


print(astring[3:7]) # prints the 4th through 8th characters in the string, a "slice"
print(astring[3])   # just the one character
print(astring[:7])  # start of the string to index 7
print(astring[3:])  # index 3 to the end
print(astring[3:-3])# index 3 to 3 fromt the end
print(astring[3:7:2]) # skipping one character, extended slice syntax, in general terms [start:stop:step]
print(astring[3:7:1]) # this is the same as print(astring[3:7])

# in C, "strrev" reverses the order of a string, but in python you can do
print(astring[::-1])   # i.e "start to end while stepping in reverse"

print(astring.upper()) # these make new strings with all upper/lower case
print(astring.lower())

print(astring.startswith("Hello"))     # this returns "true" if the string starts with "Hello"
print(astring.endswith("asdfasdfasdf"))# this returns "false" if the string doesn't  ends with "asdfasdfasdf"

afewwords = astring.split(" ") # this splits the string into a list of strings with the split in this case, being the space

# excercise: fix the string s so that the statements are true
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
