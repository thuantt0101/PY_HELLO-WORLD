
# Python là một ngôn ngữ rất mạnh mẽ, một trong những phần quan trọng nhất của Python đó decorator. 
# Trong ngữ cảnh của design pattern, ta có thể hiểu decorator là những functions thay đổi tính năng của một function, 
# method hay class một cách dynamic, mà không phải sử dụng subclass. Nó rất tiện lợi khi bạn muốn mở rộng 
# tính năng của một function mà bạn không muốn thay đổi nó. Chúng ta có thể implement decorator pattern bất nơi nào,
#  nhưng Python tạo điều kiện cho việc đó bằng cách cung cấp nhưng tính năng và cú pháp vô cùng tiện ích.

# Mọi thứ trong Python đều là object

# def a_new_decorator(a_func):

#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")

#         a_func()

#         print("I am doing some boring work after executing a_func()")

#     return wrapTheFunction

# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")

# a_function_requiring_decoration()
# #outputs: "I am the function which needs some decoration to remove my foul smell"

# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# #a_function_requiring_decoration được wrap bởi wrapTheFunction

# a_function_requiring_decoration()
# #outputs:I am doing some boring work before executing a_func()
# #        I am the function which needs some decoration to remove my foul smell
# #        I am doing some boring work after executing a_func()

# Decorators allow you to make simple modifications to callable objects like functions, methods, or classes. 
# We shall deal with functions for this tutorial. The syntax

# Synctax
# Syntax----------------------------------
# @decorator
# def functions(arg):
#     return "value"
# End Syntax----------------------------------

# Is equivalent to:
# def function(arg):
#     return "value"
# function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions

# example 1
# ---------------------------------------
# def show_text(info):
#     return 'This is a first infomation: {}'.format(info)

# def deco_func(func):
#     def wrapper(info):
#         return 'Item add to func: {}'.format(func(info))
#     return wrapper

# x = deco_func(show_text)
# print(x('ersvn'))
# end example 1---------------------------------------

# example 2
# ---------------------------------------
# def deco_func(func):
#     def wrapper(info):
#         return 'Item add to func: {}'.format(func(info))
#     return wrapper

# @deco_func
# def show_text(info):
#     return 'This is a first infomation: {}'.format(info)

# print(show_text('ersvn'))
# end ---------------------------------------

# example 3
# Make a decorator factory which returns a decorator that decorates functions with one argument. 
# The factory should take one argument, a type, and then returns a decorator that makes function should
# check if the input is the correct type. If it is wrong, it should print("Bad Type")
# (In reality, it should raise an error, but error raising isn't in this tutorial).
# Using isinstance(object, type_of_object) or type(object) might help.
# ---------------------------------------
def type_check(correct_type):
    def check(old_function): 
        def new_function(arg):
            if(isinstance(arg, correct_type)):  # (object, classinfo)
                return old_function(arg)
            else:
                print('Bad Type')
        return new_function
    return check

x = type_check(int)
print(help(x)) # check(old_function)

def times2(num):
    return num*2

y = x(times2)
print(help(y))

z = y(2)
print(type(z))
print(z)

# This is equivalent bellow
# @type_check(int) 
# def times2(num):
#     return num*2

# x = type_check(times2)
# print(x(2))
# print(times2(2)) # 2 is int type
# times2('Not A Number')

# @type_check(str)
# def first_letter(word):
#     return word[0]

# print(first_letter('Hello World'))
# first_letter(['Not', 'A', 'String'])
# end ---------------------------------------