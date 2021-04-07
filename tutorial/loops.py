# Loops
# there are two types of loops, for- and while- loops

# for loops iterate over a given sequence
primes = [2,3,5,7]   # a list
for prime in primes: # prime here iterates over primes
    print(prime)

# xrange and range functions can be used to define the lengths of for-loops
for x in range(5): # range(x) will generate a list [0 to x-1]
    print(x)

for x in range(3,6): # prints out 3 4 5
    print(x)

for x in range(3,8,2): # prints out 3,5,7 i.e ever other number between 3 and 8
    print(x)

# While-loops repeat as long as a certain boolean condition is met.
count = 0
while count < 5:
    print(count)
    count += 1 # this is the same as count=count+1
    
# break and continue statements 
# break exits the current loop
# continue skips the current block and returns to the loop statement

count = 0
while True: # will loop as long as the statement is true
    print(count)
    count += 1
    if count >= 5: # is count reaches 5
        break # ends the loop

for x in range(10):
    # check if x is even
    if x %2 == 0: # is x evenly divisible by 2? i.e even
        continue # if this statement is true, return to the loop statement
    print(x)

# Else can be used in loop statements as well
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):  # if i reaches 5, then the loop is ended and the else statement starts
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# Excercise print all even number up until 237.
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]
for x in numbers: # iterate through each value in numbers
    if x==237: # stops the loop if we reach 237
        break
    if x % 2 == 1: # if the value is uneven, return to the loop statement
        continue
    print(x) # if none of these are true, then print the value.
        
