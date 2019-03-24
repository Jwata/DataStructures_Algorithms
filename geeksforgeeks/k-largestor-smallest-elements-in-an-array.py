from heapq import heappush, heappop

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

arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(find_largest_k(arr, k))
