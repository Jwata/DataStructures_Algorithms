def count_triplets_smaller_than(arr, s):
    arr.sort() # O(n log n)

    n = len(arr)
    cnt = 0
    for i in range(n-2):
        j = i + 1
        k = n - 1
        while j<k:
            if arr[i] + arr[j] + arr[k] >= s:
                k -= 1
            else:
                cnt += k - j
                j += 1
    return     cnt


arr = [-2, 0, 1, 3]
s = 2

print(count_triplets_smaller_than(arr, s)) # 2
