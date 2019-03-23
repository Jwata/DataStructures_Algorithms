def largest_contigous_subarray(arr):
    n = len(arr)
    longest = 1
    for i in range(n):
        min_elem = arr[i]
        max_elem = arr[i]
        for j in range(i, n):
            min_elem = min(min_elem, arr[j])
            max_elem = max(max_elem, arr[j])

            if max_elem - min_elem == j - i:
                length = j - i + 1
                longest = max(longest, length)

    return longest

arr = [10, 11, 12]
print(largest_contigous_subarray(arr))

arr = [14, 10, 11, 20]
print(largest_contigous_subarray(arr))

arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
print(largest_contigous_subarray(arr))
