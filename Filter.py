# syntax
# filter(func, iterable)

# The following points are to be noted regarding filter():

# 1/ Unlike map(), only one iterable is required.
# 2/ The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
# 3/ filter passes each element in the iterable through func and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".

# let's see some examples

# The following is a list (iterable) of the scores of 10 students in a Chemistry exam. 
# Let's filter out those who passed with scores more than 75...using filter.

# --------------------------------------
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# def is_A_student(score):
#     return score > 75

# over_75 =  list(filter(is_A_student, scores))
# print(over_75)

# --------------------------------------

# double colon :: ==> word[::-1] nothing for the first ==> reverse word 
# Python 3
# --------------------------------------
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word : word == word[::-1], dromes))
print(palindromes) # ['madam', 'anutforajaroftuna']
# --------------------------------------
