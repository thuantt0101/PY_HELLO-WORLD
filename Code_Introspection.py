# Code introspection is the ability to examine classes, functions and keywords to know what they are, 
# what they do and what they know.
# Python provides several functions and utilities for code introspection.

# help()
# dir() 
# hasattr() 
# id() 
# type() 
# repr() 
# callable() 
# issubclass() 
# isinstance() 
# __doc__ 
# __name__

# Use the help function to see what each function does.
# Delete this when you are done.
# help(dir)
# help(hasattr)
# help(id)

# Exercise
# Print all list of attributes of the given Vehicle object
# Define the vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value =100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
# Print a list of all attributes of the Vehicle class.
# Your code goes here

print(dir(Vehicle))
