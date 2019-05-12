def interporation_search(arr, x):
    n = len(arr)
    i = 0
    j = n-1

    if n == 0:
        return None
    elif x < arr[0] or x > arr[n-1]:
        return None

    while i <= j:
        if arr[i] == x:
            return i
        elif arr[j] == x:
            return j

        pos = i + (x  - arr[i]) / (arr[j] - arr[i]) * (j - i)
        pos = int(pos)
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            i = pos+1
        else:
            j = pos-1

    return None


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 18
print(interporation_search(arr, x))
