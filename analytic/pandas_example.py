# Padas have 3 data type
#     1. Series - 1 chiều 
#         padas.Series(data=None, index = None, copy = None)
#             data: có thể là list, dictionary, hoặc hằng số
#             index : tập các giá trị chỉ mục duy nhất có thể băm, và dộ dài len(index) = len(data)
#             dtype : là kiểu dữ liệu của đối số data
#             copy : có giá trị True/False, mặc định là False, copy input data
#     2. dataframe - 2 chiêu & chứa Series
#     3. panel - 3 chiều & chứa dataframe

import pandas as pd
import numpy as np

#     1. Series - 1 chiều 
# ------------------------------------------------------
#         padas.Series(data=None, index = None, copy = None)
#             data: có thể là list, dictionary, hoặc hằng số
#             index : tập các giá trị chỉ mục duy nhất có thể băm, và dộ dài len(index) = len(data)
#             dtype : là kiểu dữ liệu của đối số data
#             copy : có giá trị True/False, mặc định là False, copy input data

# Create an instance serial
def createSeriesInstance():
    S = pd.Series(np.random.randint(100,size=5))
    S_index  = S.index
    S_value = S.values
    print("S_index : {0} and S_index date type: {1}".format(S_index, type(S_index)))
    # S_index : RangeIndex(start=0, stop=5, step=1) and S_index date type: <class 'pandas.core.indexes.range.RangeIndex'>
    print("S_value : {0} and S_value date type: {1}".format(S_value, type(S_value)))
    # S_value : [55  0 88 74 34] and S_value date type: <class 'numpy.ndarray'>

def createSeriesInstanceAndAssignIndex():
    phones = ['Iphone',"Samsung Note","Samsung S","Nokia"]
    quantities = [10,12,30,100]
    S = pd.Series(data=quantities, index= phones)
    print(S)

createSeriesInstanceAndAssignIndex()


