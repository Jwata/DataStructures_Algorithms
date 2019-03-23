def zig_zag(arr, up=True):
    n = len(arr)

    for i in range(n-1):
        if up:
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
        else:
            if arr[i] < arr[i+1]:
                swap(arr, i, i+1)
        up ^= True

    return arr

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [4, 3, 7, 8, 6, 2, 1]
print(zig_zag(arr))
