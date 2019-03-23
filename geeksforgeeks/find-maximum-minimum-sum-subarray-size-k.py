def find_max_sum(arr, k):
    n = len(arr)
    if n < k:
        raise Exception("Invalid")

    s = 0
    for i in range(k):
        s += arr[i]
    
    if k == n:
        return s

    max_sum = s  
    for i in range(1, n-k+1):
        j = i + k - 1
        s = s + arr[j] - arr[i-1]
        max_sum = max(max_sum, s)

    return max_sum

arr = [100, 200, 300, 400]
k = 2
print(find_max_sum(arr, k))

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(find_max_sum(arr, k))

arr = [2, 3]
k = 3
print(find_max_sum(arr, k))
