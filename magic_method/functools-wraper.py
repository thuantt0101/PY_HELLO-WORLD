# functools is a standard Python module for higher-order functions (functions that act on or return other functions). 
# wraps() is a decorator that is applied to the wrapper function of a decorator.

# It updates the wrapper function to look like wrapped function by copying attributes
# such as __name__, __doc__ (the docstring), etc.


# Example 1: Without functools.wraps()

# def a_decorator(func):
#     def wrapper(*args, ** kwargs):
#         """A wrapper function"""
#         # Extend some capabilities of func
#         func()

#     return wrapper

# @a_decorator
# def first_function():
#     """This is docstring for first function"""
#     print("first function")

# def second_function(a):
#     "This is docstring for second function"
#     print("second function")

# print(first_function.__name__)
# print(first_function.__doc__)
# print(second_function.__name__)
# print(second_function.__doc__)

# print("First Function")
# help(first_function)

# Result
# wrapper(*args, **kwargs)
#     A wrapper function

# While the above code will work logically fine, but consider this if you 
# are writing an API or a library and someone want to know what your 
# function does and it’s name or simply type help(yourFunction), 
# it will always show wrapper function’s name and docstring. 
# This gets more confusing if you have used the same wrapper function for
# different functions, as it will show the same details for each one of them. 

# Ideally it should show the name and docstring of wrapped function 
# instead of wrapping function. Manual solution would be to assign 
# __name__, __doc__ attributes in the wrapping function before returning it.


# def a_decorator(func):
#     def wrapper(*args, **kwargs):
#         "A Wrapper function"
#         func()
    
#     wrapper.__name__=func.__name__
#     wrapper.__doc__ =func.__doc__
#     return wrapper

# @a_decorator
# def first_function():
#     "This is  docstring for first function"
#     print("first function")

# @a_decorator
# def second_function(a):
#     "This is docstring for second function"
#     print("Second function")

# print(first_function.__name__)
# print(first_function.__doc__)
# print(second_function.__name__)
# print(second_function.__doc__)

# help(second_function)
# Result : still have an issue
# second_function(*args, **kwargs)
#     This is docstring for second function


# As you can see it still has an issue, i.e. the signature of the function,
# it is showing signature used by wrapper function (here, generic signature) for each of them.
#  Also if you are implementing many decorators, then you have to write these lines for each one of them. 
# So to save time and increase readability, we could use functools.wraps() as decorator to wrapper function.
# Example (with functools.wraps()) 

from functools import wraps
def a_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        func()
    return wrapper

@a_decorator
def first_function():
    """This is docstring for first function"""
    print("This is first function")

@a_decorator
def second_function(a):
    """This is second function"""
    print("This is second function")


print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)

help(first_function)
# Help on function first_function in module __main__:

# first_function()
#     This is docstring for first function
help(second_function)
        










# Using function tool










