
# Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph.
# print( set("my name is Eric and Eric is my name".split()) ) #{'my', 'Eric', 'is', 'and', 'name'}

# example 2
# To find out which members attended both events, you may use the "intersection" method:
# ----------------------------------------
# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.intersection(b)) #{'John'}
# print(b.intersection(a)) #{'John'}
# end example 2----------------------------------------

# example 3
# To find out which members attended only one of the events, use the "symmetric_difference" method:
# ----------------------------------------
# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.symmetric_difference(b)) #{'Jake', 'Jill', 'Eric'}
# print(b.symmetric_difference(a)) #{'Jake', 'Jill', 'Eric'}
# end example 3----------------------------------------

# example 4
# To find out which members attended only one event and not the other, use the "difference" method:
# ----------------------------------------
# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.difference(b)) #{'Jake', 'Eric'}
# print(b.difference(a)) #{'Jill'}
# end of example 4----------------------------------------

# example 5
# To receive a list of all participants, use "union" method:
# ----------------------------------------
# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])
# print(a.union(b))
# end example 5----------------------------------------

# exersise
# use the given event lists to print out a set containing all the participants from event A which not attend event B.
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
print( set(a).difference(set(b)) )



