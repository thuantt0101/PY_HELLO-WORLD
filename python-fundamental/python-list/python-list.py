"""

@author : Thuan-Tran

"""

# What is a list?
#  |_ A list is an ordered collection of items
#  |_ Python uses the square brackets ( [] ) to indicate a list.
#  |_ Access list using idex : list[index] Lists are zero-based index
#  |_ Modifying elements in a list : list[index] = replaced_value
#  |_ Adding elements to the list to the end of the list : list.append(adding_value)
#  |_ Insert value in any position of the list : list.insert(index, value)
#  |_ Removing elements from a list : del list[index]
#  |_ Removing last element in a list and return this element : last = list.pop()
#  |_ Removing spcific elements and return the removed element : removedElement = list.pop(index)
#  |_ To remove an element by value, you use the remove()
#  |_ List can contain other lists
#  |_ The negative index allows you to access elements starting from the end of the list


empty = []

todos = ['learn python list', 'how to manage list elements']

print("value of 0 position :  {0}".format(todos[0]))

coordinates = [ [0,0], [100, 100], [ 200, 200]]
print(coordinates)


numbers = [ 1, 3, 2, 7, 9 , 4]
print(numbers[-1])
print(numbers[-2])
# 4

numbers[-2] = 3
print(numbers[-2])
# 3

numbers.append(10)
print(numbers)
# [1, 3, 2, 7, 3, 4, 10]

numbers.insert(2,100)
print(numbers)
# [1, 3, 100, 2, 7, 3, 4, 10]

del numbers[0]
print(numbers)
# [3, 100, 2, 7, 3, 4, 10]

last = numbers.pop()
print(numbers)
print("this is removed elements : {0}".format(last))

removedElement = numbers.pop(1)


# remove by value
numbers.remove(3)
print(numbers)
# [2, 7, 3, 4]


