# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

# Firstly, a Nested Function is a function defined inside another function
# It's very important to note that the nested functions can access the variables of the enclosing scope.
# However, at least in python, they are only readonly.
# However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.

# example 1
# -----------------------------------
# def transmit_to_space(message):
#     # "This is the enclosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message)

#     data_transmitter()

# print(transmit_to_space("Test message"))
# end example 1-----------------------------------

# example 2
# -----------------------------------
# def print_msg(number):
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number=3
#         print(number) # 3
#     printer() # 3

#     print(number)

# print_msg(9)
# end example 2-----------------------------------

# example 3
# Now, how about we return the function object rather than calling the nested function within. 
# (Remember that even functions are objects. (It's Python.))
# -----------------------------------
# def transmit_to_space(message):
#     "This is the enclosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message)
#     return data_transmitter

# # call function
# fun2 = transmit_to_space("Burn the Sun!")
# fun2()
# end example 3-----------------------------------


# exercise 
# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. 
# That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.

# your code goes here
# -----------------------------------
def multiplier_of(n):

    def data_transmitter(number):
        return number * n
    
    return data_transmitter

multiplywith5 = multiplier_of(5)
print(multiplywith5(9)) # 45
# -----------------------------------
