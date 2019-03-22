def quick_sort(arr, i, j):
    if i > j:
        return

    p = partition(arr, i, j)
    quick_sort(arr, i, p-1)
    quick_sort(arr, p+1, j)

def partition(arr, i, j):
    pivot = arr[j]

    left = i-1

    for k in range(i, j+1):
        if arr[k] <= pivot:
            left += 1
            swap(arr, k, left)

    return left

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [10, 80, 30, 90, 40, 50, 70]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)
