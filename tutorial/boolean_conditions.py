# Coniditions using Boolean logic 20210225
# python can use logic statements to direct the code. conditions are evaluated using Boolean logic.

x = 2
print(x==2) # prints out true
print(x==3) # prints out false
print(x<3) # prints out true

# must be == for equals, != is not equal.
# several statements can be combined using "and"/"or"
name = "John"
age  = 23
if name == "John" and age == 23:
    print("Your name is %s, and you are also %d." % (name,age))
if name == "John" or name == "Rick":
    print("your name is either John or Rick")

# the "in" operator can be used to check if a specified object exists within an iterable object container, such as a list
name = "John"
if name in ["John","Rick"]: # checks if name appears in list ["John","Rick"]
    print("Your name is either John or Rick")

# Python uses indentation to define code blocks, standard python indent is 4 spaces, but any works as long as it is consistent
statement = False
another_statement = True
if statement is True:
    # do something
    pass # does nothing, but is a placeholder for future operations
elif another_statement is True: # this is else if
    # do something else
    pass
else:
    # do another thing
    pass

x = 2
if x == 2
    print("x equals two!") # indented
else:
    print("x does not equal two...")


# "is" can be used to check if two variables contain the same instances
x=[1,2,3]
y=[1,2,3]
print(x==y) # this will be true
print(x is y) # this will be false

# not operator is the inversion of is
print(not False)
print((not False)==(False))


# Excercise - change this code so they are True.
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
    

