def find_subarr(arr, s):
    n = len(arr)
    if n == 0:
        return Exception('array is empty')
    i = 0
    j = 0
    cur_sum = arr[0]
    while j < n and i <= j:
        if cur_sum == s:
            return arr[i:j+1]
        elif j < n - 1 and (cur_sum < s or i == j):
            j += 1
            cur_sum += arr[j]
        else:
            cur_sum -= arr[i]
            i += 1

    return None

arr = [1, 4, 20, 3, 10, 5]
s = 33
print(find_subarr(arr, s))

arr = [1, 4, 0, 0, 3, 10, 5]
s = 7
print(find_subarr(arr, s))

arr = [1, 4]
s = 0
print(find_subarr(arr, s))
