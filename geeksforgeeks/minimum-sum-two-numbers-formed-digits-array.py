from heapq import heapify, heappop

def min_sum_numbers(arr):
    n = len(arr)
    heapify(arr) # O(n)

    if n % 2 == 0:
        a = n // 2
        b = n // 2
    else:
        a = n // 2 + 1
        b = n // 2

    min_sum = 0
    while len(arr) > 0:
        d = heappop(arr) # O(log n)

        if a >= b:
            min_sum += d * (10 ** (a-1))
            a -= 1
        else:
            min_sum += d * (10 ** (b-1))
            b -= 1

    return min_sum

arr = [6, 8, 4, 5, 2, 3]
print(min_sum_numbers(arr))

arr = [5, 3, 0, 7, 4]
print(min_sum_numbers(arr))
