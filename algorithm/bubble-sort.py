
def partition(array, low, high):
        
    if low < high:
        for i in range(low, high):
            if i < high:
                if array[i] > array[i+1]:
                    # swapping 
                    array[i], array[i+1] = array[ i+1 ], array[i]
              
def bubbleSort(array, low, high):        
    if low < high:
        partition(array, low, high)
        high -= 1
        bubbleSort(array, low, high)
        
data = [5, 3, 8, 4, 6, 100, 100]
low = 0
high = len(data) -1
bubbleSort(data, low, high)
print(data)
    
    




        

        
    
        
