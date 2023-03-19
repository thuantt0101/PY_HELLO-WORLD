# Partial functions allow one to derive a function with x parameters to a function with 
# fewer parameters and fixed values set for the more limited function.

# example 1
# -----------------------------------
# from functools import partial
# def multiply(x, y):
#     return x*y
# dbl = partial(multiply, 2)
# print(dbl(4))
# end example 1-----------------------------------
# An important note: the default values will start replacing variables from the left. 
# The 2 will replace x. y will equal 4 when dbl(4) is called. It does not make a difference in this example, 
# but it does in the example below.


from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
dbl = partial(func, 10, 5, 2)
print(dbl(1))