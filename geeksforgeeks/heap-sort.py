def heapify(arr, n, i):
    largest = i
    l = i * 2 + 1
    r = l + 1

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r]  > arr[largest]:
        largest = r

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heap_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n):
        swap(arr, 0, n-1-i)
        heapify(arr, n-1-i, 0)


arr = [4, 10, 3, 5, 15]
heap_sort(arr)
print(arr)

# heapify: O(log n)
# build heap: O(n)
# heap sort: Σlog k <= nlog n = O(n log n)
