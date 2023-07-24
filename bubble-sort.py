# WRONG NOT FINISHED
# import time
# def bubble_sort(arr):
#     start = time.time()
#     for i in range(len(arr) - 1):
#         for j in range(len(arr)):
#             if arr[j] > arr[i+1]:
#                 temp = arr[j]
#                 arr[j] = arr[i+1]
#                 arr[i+1] = temp
#     end = time.time()
#     print(end-start)
#     return arr

import time
def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
    end = time.time()
    print(end-start)
    return arr

print(bubble_sort([5, 34, 3, 52, 1, 5, 64, 3, 2, 1, 53, 4, 3, 2, 15, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 74, 3, 2, 1, 5, 4, 3, 2, 71, 5, 4, 3, 82, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]))
