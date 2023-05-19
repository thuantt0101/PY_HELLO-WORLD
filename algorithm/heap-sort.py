# Heapsort is a comparison-based sorting technique based on a 
# Binary Heap data structure. It is similar to selection sort 
# where we first find the maximum element and place the maximum 
# element at the end. We repeat the same process for the remaining element.


# 1. xây dựng 1 heap tối đa từ dữ liệu đầu vào
# 2. Tại thời điểm này, mục lớn nhất được lưu ở gốc của heap. Thay thế nó bằng mục cuối của heap,
#  sau đó giảm kích thước của heap đi 1. Cuối cùng, ta có 1 gốc heap.

# 3. Lặp lại bước 2 trong khi kích thước của heap lớn hơn 1.

# Làm sao để xây dựng được 1 heap?
# Thủ tục heap chỉ có thể được áp dụng cho 1 nút nếu các nút con của nó đã được chất đống.
# Vì vậy việc chất đống phải được thực hiện theo thứ tự từ dưới lên.

# data = [4, 10, 3, 5, 1]

# 4(0) , 10 (1), 3(2), 5(3), 1(4)
# các số trong ngoặc đại diện cho các chỉ số(index) trong mảng

# áp dụng quy trình chất đóng ( heap ) cho index 1:
# 4(0)
# 10(1) 3(2)
# 5(3) 1(4)

# áp dụng quy trình chất đống cho chỉ mục 0:
# 10(0)
# 5(1) 3(2)
# 4(3) 1(4)

# Thủ tục chất đống tự gọi đệ quy để xây dựng heap theo cách từ trên xuống.

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2 # right = 2*i + 2
    # See if left child of root exists nad is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
    
        # Heapify the root
        heapify(arr, n, largest)
    
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


data = [12, 11, 13, 5, 6, 7, ]
