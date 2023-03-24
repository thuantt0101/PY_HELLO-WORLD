
# The map() function in python has the following syntax:
# map(func, *iterables)

# Where func is the function on which each element in iterables (as many as they are) would be applied on. 
# Notice the asterisk(*) on iterables? It means there can be as many iterables as possible
# in so far func has that exact number as required input arguments. 
# Before we move on to an example, it's important that you note the following:
# ----------------------------------
# 1/
# In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object
# which is a generator object. To get the result as a list, the built-in list() 
# function can be called on the map object. i.e. list(map(func, *iterables))
# 2/
# The number of arguments to func must be the number of iterables listed.
# ----------------------------------

# example 1
# Say I have a list (iterable) of my favourite pet names, all in lower case and I need them in uppercase. 
# Traditonally, in normal pythoning, I would do something like this:

# ----------------------------------------------
# my_pets = ['alfred', 'tabitha', 'william', 'arla']
# uppered_pets = []

# for pet in my_pets:
#     pet_ = pet.upper()
#     uppered_pets.append(pet_)

# print(uppered_pets)
# ----------------------------------------------

# With map() functions, it's not only easier, but it's also much more flexible. I simply do this:
# ----------------------------------------------
# my_pets = ['alfred', 'tabitha', 'william', 'arla']
# uppered_pets = list(map(str.upper, my_pets))
# print(uppered_pets)
# ----------------------------------------------

# Which would also output the same result. Note that using the defined map() syntax above, 
# func in this case is str.upper and iterables is the my_pets list 
# -- just one iterable. Also note that we did not call the str.upper 
# function (doing this: str.upper()), as the map function does that for us on each element in the my_pets list.

# What's more important to note is that the str.upper function requires only one argument 
# by definition and so we passed just one iterable to it. 
# So, if the function you're passing requires two, or three, 
# or n arguments, then you need to pass in two, three or n iterables to it. 
# Let me clarify this with another example.


# Say I have a list of circle areas that I calculated somewhere, all in five decimal places.
# And I need to round each element in the list up to its position decimal places, 
# meaning that I have to round up the first element in the list to one decimal place,
# the second element in the list to two decimal places, the third element in the list to three decimal places,
# etc. With map() this is a piece of cake. Let's see how.


# Python already blesses us with the round() built-in function that takes two arguments 
# -- the number to round up and the number of decimal places to round the number up to. So, 
# since the function requires two arguments, we need to pass in two iterables.
# ----------------------------------------------
# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
# result = list(map(round, circle_areas, range(1, 7)))
# print(result)
# ----------------------------------------------

# ----------------------------------------------
# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
# result = list(map(round, circle_areas, range(1, 3))) # [3.6, 5.58]
# print(result)
# ----------------------------------------------

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 999))) 
print(result) # [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]

