"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    min_index = 0
    max_index = len(input_array)
    middle = int((max_index - 1) / 2)
    
    for i in range(max_index - 1):
        if value < input_array[middle]:
            max_index = middle
            middle = int((max_index - 1) / 2)
        
        if value > input_array[middle]:
            min_index = middle + 1
            middle = int((min_index + max_index) / 2)

        if value == input_array[middle]:
            return middle
    
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 15
test_val2 = 11
test_val3 = 1
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val3))