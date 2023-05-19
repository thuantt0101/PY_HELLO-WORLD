# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023
@author: Thuan-Tran
@Numpy : 1.21.6

"""

import numpy as np

# NumPy arrays can be defined using Python sequences such as lists and tuples. 
# Lists and tuples are defined using [...] and (...), respectively. Lists and tuples can define ndarray creation:

# |_ a list of numbers will create a 1D array
# |_ a list of lists will create a 2D array
# |_ further  nested will create higher-dimensional arrays. In general, any array object is called an ndarray in Numpy.

a1D = np.array([1, 2, 3, 4])
a2D = np.array([ [1, 2], [3, 4]])
a3D = np.array([ [ [1, 2], [3, 4] ], [ [5, 6], [7 ,8 ] ] ])
print('--------------1D-------------------')
print(a1D)
print('--------------2D-------------------')
print(a2D)
print('--------------3D-------------------')
print(a3D)

print('---------------------------------')
# An 8-bit signed integer represents integers from -128 to 127
a= np.array([127, 128, 129], dtype=np.int8)
print(a)
# [ 127 -128 -127] wrong

a = np.array([127, 128, 129], dtype=np.int32)
print(a)
# [127 128 129]


# example 1
a = np.array([2, 3, 4], dtype=np.uint32)
b = np.array([5, 6, 7], dtype=np.uint32)
c_unsigned32 = a - b
print('unsigned c: ', c_unsigned32, c_unsigned32.dtype) 
# unsigned c:  [4294967293 4294967293 4294967293] uint32


# Notice when you perform operations with two arrays of the same dtype: uint32, 
# the resulting array is the same type. When you perform operations with different dtype, 
# NumPy will assign a new type that satisfies all of the array elements involved in the computation, here uint32 and int32 can both be represented in as int64.
c_signed32  = a - b.astype(np.int32)
print('signed c: ', c_signed32, c_signed32.dtype) 
# signed c:  [-3 -3 -3] int64






