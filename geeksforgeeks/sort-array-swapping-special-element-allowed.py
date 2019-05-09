GAP = 999
def special_swap_sort(arr, n):
    # first move the gap to the end
    for i in range(n+1):
        if arr[i] == GAP:
            swap(arr, i, n)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap_wrapper(arr, j-1, j)
            j -= 1
    return arr

def swap_wrapper(arr, i, j):
    l = len(arr) - 1
    swap(arr, i, l)
    swap(arr, j, i)
    swap(arr, j, l)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [1, 5, 4, 999, 3, 2]
n = 5

print(special_swap_sort(arr, n))
