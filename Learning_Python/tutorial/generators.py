# generators 20210326
# are used to create iterators, but more complicated

# example
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

# EXCERCISE - manke a generator that generates the fibonacci sequence
# fill in this function
def fib():
    a, b = 1, 1 # intial conditions
    # pass #this is a null statement which does nothing when executed, useful as a placeholder.
    while 1: # loops infinitely
        yield a # the number i pops out is a I thnk
        a, b = b, a + b # a is previous iterations b, b is the sum of current a and b


# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 100:
            break
