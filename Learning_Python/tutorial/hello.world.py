# Tutorial #1: variables and types
print("Hello, World!") # print commands prints to shell

x=1
if x==1:
    # blocks are divided by indents, four spaces or 1 tab
    print ("X is 1")


    
myinteger = 7 # integer are written like this
print(myinteger)

myfloat = 7.0 # if a number has decimals, it is called a "float". decimal signs are denoted as "."
print(myfloat)

myfloat=float(7) # converts integer to floated value
print(myfloat)

mystring = 'hello' # strings are written either with '' or ""
print(mystring)
mystring = "hello" # these are equivalent
print(mystring)

mystring="But if you're using apostraphes, you might want to use the quote sign."

# operators can be executed on strings and numbers
one = 1
two = 2
three = one + two
print(three)

hello="hello"
world="world"
helloworld=hello+' '+world
print(helloworld)

print(hello+' '+world) # operators can be executed within commands

# More than one variable can be assigned at the same time
a,b = 3,4

print(a,b)

# Mixing operators between numbers and strings is NOT supported
one = 1
two = 2
hello = "hello"

# print(one + two + hello) # does not work

# EXCERCISE: make 1 string, 1 float, and 1 integer
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code, checks what the variables are, only prints if correct.
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)










