

# To consolidate our knowledge of the map() function, we are going to use it to implement 
# our own custom zip() function. The zip() function is a function that takes a number of 
# iterables and then creates a tuple containing each of the elements in the iterables.
# -------------------------------------
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [1, 2, 3, 4, 5]
# results = list(zip(my_strings, my_numbers))
# print(results)
# print(type(results[1]))
# -------------------------------------
# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)