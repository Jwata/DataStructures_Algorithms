def find_pythagorean_triplet(arr):
    n = len(arr)

    for i in range(n):
        arr[i] = arr[i] ** 2

    arr.sort() # O(n log n)

    for i in range(n-2): # range(3)
        k = n-1-i
        if find_pair(arr, k, arr[k]): # O(k)
            return True

    return False

def find_pair(arr, n, s):
    i = 0
    j = n-1

    while i < j: # O(n)
        if arr[i] + arr[j] == s:
            return True
        elif arr[i] + arr[j] < s:
            i += 1
        else:
            j -= 1

    return False

arr = [3, 1, 4, 6, 5]
print(find_pythagorean_triplet(arr))

arr = [10, 4, 6, 12, 5]
print(find_pythagorean_triplet(arr))
