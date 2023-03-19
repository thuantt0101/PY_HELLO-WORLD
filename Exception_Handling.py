import re

# example 1
# def do_stuff_with_number(n):
#     print(n)

# def catch_this():
#     the_list = [1, 2, 3, 4, 5]

#     for i in range(20):
#         try:
#             do_stuff_with_number(the_list[i])
#         except IndexError:
#             do_stuff_with_number(0)

# catch_this()
# end example 1

# example 2
actor = {
    "name" : "John Cleese"
    , "rank" : "awesome"
}

def get_last_name(dic):        
    try:
        return dic["name"].split()[1]
    except:
        return "nothing found"
    
# test function
print(get_last_name(actor))
# end example 2