# Just unlikely merge Sort, QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

# Always pick the first element as a pivot
# Always pick the last element as a pivot
# Pick a random element as a pivot
# Pick median as a pivot

# Here we will be picking the last element as a pivot. The key process in quickSort is partition(). 
# Target of partitions is, given an array and an element ‘x’ of array as a pivot, 
# put x at its correct position in a sorted array and put all smaller elements (smaller than x) 
# before x, and put all greater elements (greater than x) after x. All this should be done in linear time. 

# Function to find the partition position
def partition(array, low, high):
    
    # Choose the rightmost elements as pivot
    pivot = array[high]
    print("pivot is : {}".format(pivot))
    
    # pointer for greather element
    i = low - 1
    print("pointer to greater element : {}".format(array[i]))

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            print("i = i + 1 : {}".format(i))
            print("j : {}".format(j))

            # Swapping element at i with element at j
            ( array[i], array[j] ) = (array[j], array[i] )
            print(array)
            
    # Swapping the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the position from where partition is done
    # Position that specify value greater than pivot
    print("i : {}".format(i))
    print(array)
    return i + 1

# Function to perform quick sort
def quickSort(array, low, high):
    print('--------------------------------')
    if low < high:
        
        print("[low : high ] :  [ {} : {} ]".format(low, high))

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        # pi is partition index
        pi = partition(array, low, high)
        print("pi: {}".format(pi))
                
        # Recusive call on the left of the pivot
        # Before pi 
        quickSort(array, low, pi-1)
        
        # Recusive call on the rifht of the pivot
        # After pi    
        quickSort(array, pi + 1, high)

data = [1, 7, 4, 10, 5, 8, 9]
size = len(data)
quickSort(data, 0, size-1)
print(data)


    







