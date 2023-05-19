
# Ý tưởng
# Xét 1 mảng gồm n số nguyên
# với các sắp xếp không giảm từ trái sang phải,mục đích của chúng ta là đưa dần các số 
# lớn nhất về cuối dãy(ngoài cùng bên phải)

# Bắt đầu từ vị trí số 1, xét lần lượt từng cặp 2 phần tử, nếu phần tử bên phải nhỏ hơn phân
# tủ bên trái thì swap  2 phần tử này với nhau.
# với cách làm như thế thì phần tử nhỏ hơn sẽ "nổi" lên , còn phần tử lớn hơn sẽ "chìm" dần về bên phải.

def bubbleSort(array):
    
    n = len(array)
   
    # optimize code, so if the array is already sorted, it does not need
    # to go through the entire process
    swapped = False
    
    # Traverse through all array elements   
    for i in range(n-1):

        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # last i elements are alreadt in place
        for j in  range(0 , n-1-i):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        
        if not swapped: 
            # if we have not needed to make a single swap, we
            # can just exit the main loop           
            return 

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)


                




