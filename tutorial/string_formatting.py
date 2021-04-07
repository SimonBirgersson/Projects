# TUTORIAL #4: string formatting

# Python uses the same string formatting as C.
# the % operator is used to format "tuples" (a fixed size list)
# together with a format string, which contains argument specifiers like %s and %d

# this will print "Hello, John!"
name = "John"
print("Hello, %s!" % name) # formats the string using another string (%s)

age = 23
print("%s is %d years old." % (name, age)) # here the tuple is (name, age)

# This will print out: A list: [1,2,3]
mylist = [1,2,3]
print("A list: %s" % mylist) # works for lists as well

# basic argument specifiers:
# %s specifies string
# %d integers
# %f floating numbers
# %.<num. digits>f amount of significant decimals in float
# %x/%X integers in hex representation

# Excercise: write a string that formats using the follwing syntax:
# "Hello John Doe. Your current balance is $53.44."

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s, your current balance is $%s."
# thought you could do %2f for the dollar count, returns 53.4400000 instead?

print(format_string % data)
