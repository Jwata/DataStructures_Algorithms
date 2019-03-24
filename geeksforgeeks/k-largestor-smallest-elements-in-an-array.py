from heapq import heappush, heappop, heapify

def find_largest_k(arr, k):
    n = len(arr)
    heap = []
    for i in range(n):
        if len(heap) < k:
            heappush(heap, arr[i])
        else:
            if heap[0] < arr[i]:
                heappop(heap)
                heappush(heap, arr[i])

    largest_k = []
    while len(heap) > 0:
        largest_k = [heappop(heap)] + largest_k

    return largest_k

def find_largest_k_with_maxheap(arr, k):
    n = len(arr)
    for i in range(n):
        arr[i] = -1 * arr[i]

    heapify(arr)

    largest_k = []
    for i in range(k):
        largest_k.append(-1 * heappop(arr))

    return largest_k

arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(find_largest_k(arr, k))
print(find_largest_k_with_maxheap(arr, k))
