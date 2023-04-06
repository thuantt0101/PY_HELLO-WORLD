# reduce applies a function of two arguments cumulatively 
# to the elements of an iterable, optionally starting with an initial argument. 
# It has the following syntax:

# reduce(func, iterable[, initial])

# ----------------------------------
# from functools import reduce

# numbers = [3, 4, 6, 9, 34, 12]

# def custom_sum(first, second):
#     return first + second

# result = reduce(custom_sum, numbers)
# print(result)
# ----------------------------------
# As usual, it's all about iterations: reduce takes the first and second elements 
# in numbers and passes them to custom_sum respectively. custom_sum computes their sum and returns it to reduce.
#  reduce then takes that result and applies it as the first element to custom_sum and takes the next element 4
# (third) in numbers as the second element to custom_sum.
#  It does this continuously (cumulatively) until numbers is exhausted.

# Python 3
# -------------------------------
# from functools import reduce

# numbers = [3, 4, 6, 9, 34, 12]

# def custom_sum(first, second):
#     return first + second

# result = reduce(custom_sum, numbers, 10)
# print(result) # 78
# -------------------------------
#### Map

# exercises
from functools import reduce 

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda x: round(x **2, 3) ,my_floats))
filter_result = list(filter(lambda name : len(name) <=7 , my_names ))
reduce_result = reduce(lambda num1 , num2 : num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)