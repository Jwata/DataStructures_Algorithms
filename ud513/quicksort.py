"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    if len(array) <= 1:
        return array
        
    pivot = array[0]
    left_array = []
    right_array = []
    
    for i in range(1, len(array)):
        value = array[i]
        if value <= pivot:
            left_array.append(value)
        else:
            right_array.append(value)
            
    return quicksort(left_array) + [pivot] + quicksort(right_array)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
