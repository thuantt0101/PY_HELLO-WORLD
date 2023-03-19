
# Every function in Python receives a predefined number of arguments, if declared normally, like this
def myfunction(first, second, third):
    s = first + second + third
    print(s)

# It is possible to declare functions which receive a variable number of arguments,
# using the following syntax.
#---------------------------------------
# def foo(first, second, third, *therest):
#     print("First: %s" %first)
#     print("Second: %s" %second)
#     print("Third: %s" %third)
#     print("And all the rest...%s" %list(therest))

# foo("First name", "Second name", "Third name", "Fourth name", "Five")
# foo(1, 2, 3, 4, 5)
#---------------------------------------

# it is also possible to send functions arguments by keyword, so that the order of the argument dost not matter.
# using the following syntax. The following code yeilds the following output: The sum is  : 6 Result 1
#---------------------------------------
# def bar(first, second, third, **options):
#     if options.get("action") == "sum":
#         print("The sum is: %d" %(first + second + third))
    
#     if options.get("number") == "first":
#         return first
    
# result = bar(1, 2, 3, action = "sum", number = "first")
# print("Result: %d" %result)
#---------------------------------------

# Exersise
# Fill in the foo and bar functions so they can receive a 
# variable amount of arguments (3 or more) The foo function must return the amount of extra arguments received. 
# The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.
#---------------------------------------
def foo(a, b, c, *options):
    return len(options)

def bar(a, b, c , **options):
    return options.get("magicnumber") == 7

#test code
if foo(1, 2, 3, 4) ==1:
    print("Good.")
if foo(1, 2, 3, 4, 5) ==2:
    print("Better.")
if bar(1, 2, 3, magicnumber = 6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber = 7) ==True:
    print("Awesome.")
#---------------------------------------
 




