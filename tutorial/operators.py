# TUTORIAL #3: BASIC OPERATORS
# Just as all programming languages, basic math operators work as expected.
number = 1 + 2 * 3 / 4.0 # follows mathmatic order of operators
print(number)

# another operator is the modulo (%) operator, which returns the integer remainder of division.
remainder = 11 % 3
print(remainder)

# Using **, you get ^
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# Python supports concatenating strings using the addition operator
helloworld = 'hello' + ' ' + 'world'
print(helloworld)

# you can also multiply a string to form a repeating sequence.
lotsofhellos = "hello" * 10
print(lotsofhellos)

# operators can be used with lists for addition and multiplication as well.
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers) # prints the list in order

print([1,2,3]*3) # prints the list repeating

# EXCERCISE: create two lists, x_list and y_list
# should contain 10 instances of the variables x and y respectively.
# Also create a list called big_list, which contain both lists.
x = object() # empty objects to put in lists
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
