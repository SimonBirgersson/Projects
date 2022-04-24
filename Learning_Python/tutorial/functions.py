# functions
# functions allow us to divide our code in useful blocks, makes the ocde more readable and saves more space.

def my_function(): # def generates a function with the following name.
        print("Hello from my function!") #the functions promts is written indented
def my_function_with_args(username,greeting): # arguments are parenthesized
    print("Hello, %s , from my functions! I wish you %s" % (username, greeting))
def sum_two_numbers(a,b):
    return a + b # return is what the function returns, obv

# calling on these functions
my_function()

my_function_with_args("John","a great year!")
x= sum_two_numbers(1,2)
print(x)

# excercise
#In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
#Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
#Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
#Run and see all the functions work together!

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
