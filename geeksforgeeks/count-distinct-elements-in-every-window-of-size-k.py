from collections import defaultdict

def count_distinct_for_each_window(arr, k):
    n = len(arr)
    if n < k:
        raise Exception("k is larger than array size")

    m = defaultdict(list)
    for i in range(k):
        m[arr[i]].append(i)
    s = len(m)
    sizes = [s]

    if k == n:
        return sizes

    for i in range(1, n-k+1): # range(1, 4)
        j = i + k - 1
        m[arr[j]].append(j)
        m[arr[i-1]].pop(0) # pop head

        # delete key if it's empty
        if len(m[arr[i-1]]) == 0:
            del(m[arr[i-1]])

        sizes.append(len(m))

    return sizes

arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(count_distinct_for_each_window(arr, k))
