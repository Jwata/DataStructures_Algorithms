def binary_search(arr, v):
    n = len(arr)

    left = 0
    right = n - 1

    while left <= right:
        i = (right + left) // 2
        if arr[i] == v:
            return i
        elif arr[i] > v:
            right = i - 1
        else:
            left = i + 1

    return None


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(binary_search(arr, 23))  # should be 5
print(binary_search(arr, 2))  # should be 2
print(binary_search(arr, 56))  # should be 7
print(binary_search(arr, 100))  # should be None
print(binary_search(arr, 0))  # should be None

# O(log n)
