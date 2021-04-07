# Classes and objects 20210326

# "Objects" are encapsulations of variables and functions into a single entitiy
# they get these variables and functions from "classes"

# A basic class:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside of the Class.")

# Assigning the class "MyClass" to an object:
myObjectx = MyClass() # This variable now contains an object of the class "MyClass"

# Accessing these variable now:
print(myObjectx.variable) # Outputs "blah"

myObjectx.function() # performs the function within the class, in this case prints message.

# EXCERCISE
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name  = "Fer"
car1.kind  = "Convertible"
car1.color = "red"
car1.value = 60000


car2 = Vehicle()
car2.name  = "Jump"
car2.kind  = "Van"
car2.color = "Blue"
car2.value = 10000


# test code
print(car1.description())
print(car2.description())
