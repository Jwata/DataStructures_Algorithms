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

arr = [4, 10, 3, 5, 15]
n = len(arr)

for i in range(n-1, -1, -1):
    heapify(arr, n, i)
print(arr)
