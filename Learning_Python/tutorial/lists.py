# Tutorial #2: lists

# Lists are like arrays or vectors, they can contain any type of variable.
# They are also iterated very easily

mylist= [] # an empty list, uses []
mylist.append(1) # .append adds one variable to the list, in this case, "1"
mylist.append(2)
mylist.append(3)

# mylist[x] calls variable x from the list, first variable is indexed 0
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3

for x in mylist: # first for loop! iterates through all elements in mylist
    print(x) # will return each element in mylist, in for-loops, they are called using "()"

mylist=[1,2,3] # another way to fill lists
# print(mylist[10]) # doesn't work, cannot access indices beyond those defined

# EXCERCISE: add number and strings to the correct lists using "append"
numbers = [1,2,3]
strings = ['hello','world']
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1] # this is how you call variables in lists, using "[]"


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name) # %s will enter the string included after %
