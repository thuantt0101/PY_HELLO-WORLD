# Python programming provides us with a built-in @property 
# decorator which makes usage of getter and setters much easier in Object-Oriented Programming.


# class without Getters and Setters
class Celsius:
    def __init__(self, temperature  = 0 ):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
# Create a new object
# human = Celsius()

# Set the temperature
# human.temperature = 37

# Get the temperature attribute
# print(human.temperature)

# Get the to_fahrenheit method
# print(human.to_fahrenheit())

# So, whenever we assign or retrieve any object attribute like temperature as shown above, 
# Python searches it in the object's built-in __dict__ dictionary attribute as
# print(human.__dict__)



# Using Getters and Setters
class Celsius1:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

     # getter method
    def get_temperature(self):
        return self._temperature
    
    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value 

    # An underscore _ at the beginning is used to denote private variables in Python.

# Create a new object, set_temperature() internally called by __init__
# human1 = Celsius1(37)

# Get the temperature attribute via a getter
# print(human1.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
# print(human1.to_fahrenheit())

# new constraint implementation
# human1.set_temperature(-300)

# Get the to_fahreheit method
# print(human1.to_fahrenheit())


# However, the bigger problem with the above update is that all the programs that 
# implemented our previous class have to modify their code from obj.temperature to obj.get_temperature() 
# and all expressions like obj.temperature = val to obj.set_temperature(val).

# This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.

# All in all, our new update was not backwards compatible. This is where @property comes to rescue.


# The property Class
# using property class
class Celsius2:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)

# We added the print() function inside get_temperature() and set_temperature() to clearly observe that they are being executed.
# The last line of the code makes a property object temperature.
# Simply put, property attaches some code (get_temperature and set_temperature) to the member attribute accesses (temperature).

# human2 = Celsius2(37)

# print(human2.temperature)

# print(human2.to_fahrenheit())

# human2.temperature = -300

# Setting value...
# Getting value...
# 37
# Getting value...
# 98.60000000000001
# Setting value...
# Traceback (most recent call last):
#   File "<string>", line 31, in <module>
#   File "<string>", line 18, in set_temperature
# ValueError: Temperature below -273 is not possible

# As we can see, any code that retrieves the value of temperature will
# automatically call get_temperature() instead of a dictionary (__dict__) look-up.

# Similarly, any code that assigns a value to temperature will automatically call set_temperature().

# We can even see above that set_temperature() was called even when we created an object.

# human = Celsius(37) # prints Setting value..
# Can you guess why?

# The reason is that when an object is created, the __init__() method gets called. 
# This method has the line self.temperature = temperature. This expression automatically calls set_temperature().

# Similarly, any access like c.temperature automatically calls get_temperature(). This is what property does.

# By using property, we can see that no modification is required in the implementation of the value constraint.
# Thus, our implementation is backward compatible.

# Note: The actual temperature value is stored in the private _temperature variable. The temperature attribute 
# is a property object which provides an interface to this private variable.


# The @property Decorator
# In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:
# property(fget=None, fset=None, fdel=None, doc=None)

# Here,

# fget is function to get value of the attribute
# fset is function to set value of the attribute
# fdel is function to delete the attribute
# doc is a string (like a comment)

# As seen from the implementation, these function arguments are optional.

# A property object has three methods, getter(), setter(), and deleter() to specify fget, 
# fset and fdel at a later point. This means, the line:
# temperature = property(get_temperature,set_temperature)


# Using @property decorator
class Celsius3:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human3 = Celsius3(37)

print(human3.temperature)

print(human3.to_fahrenheit())

coldest_thing = Celsius3(-300)

# Setting value...
# Getting value...
# 37
# Getting value...
# 98.60000000000001
# Setting value...
# Traceback (most recent call last):
#   File ".\property_decorator.py", line 191, in <module>
#     coldest_thing = Celsius3(-300)
#   File ".\property_decorator.py", line 166, in __init__
#     self.temperature = temperature
#   File ".\property_decorator.py", line 180, in temperature
#     raise ValueError("Temperature below -273 is not possible")
# ValueError: Temperature below -273 is not possible