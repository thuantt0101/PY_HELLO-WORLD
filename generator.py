# def plain_old_func():
#     my_list = [1, 2, 3]
#     for i in my_list:
#         return i*2    
# print(plain_old_func()) # 2


# 2-generator
def fancy_generator():
    my_list = [1, 2, 3]
    for i in my_list:
        yield i * 2

mygen = fancy_generator() 
print(mygen) # <generator object fancy_generator at 0x000001EBDE9E9D60>
for x in fancy_generator():
    print(x) # 2, 4, 6

# 1 1 2 3 5 ...
# 3-fibonacy
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
# import types
# if type(fib()) == types.GeneratorType:
#     print("Good, The fib function is a generator.")

#     counter = 0
#     for n in fib():
#         print(n)
#         counter +=1
#         if counter ==10:
#             break
