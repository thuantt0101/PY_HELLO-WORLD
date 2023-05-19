
# -------------------------define--------------------------------
# Now instead of defining the function somewhere and calling it, we can use python's lambda functions
# which are inline functions defined at the same place we use it. 
# So we don't need to declare a function somewhere and revisit the code just for a single time use.
# They dont need to have a name, so they also called anonymous funtions.
# whe define lambda function using the keyword lambda.
# --------------------------------------------------------------

# syntax : your_function_name = lambda inputs : output

# example 1
a = 1
b = 2
sum = lambda x, y : x + y
c = sum(a, b)
print(c)

# example 2
# Write a program using lambda function to check if a number in the given list is odd. 
# print True if the number is odd, or False if not for each element.
l = [2,4,7,3,14,19]
for i in l:
    lambda_func = lambda x : (x%2)==1
    print(lambda_func(i))


print('----------------------last one-------------------------------')
l  = [1, 2]
lam = (lambda x: str(x), l)
print(lam)

