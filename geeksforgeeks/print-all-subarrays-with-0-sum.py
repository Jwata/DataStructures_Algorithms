from collections import defaultdict

def all_sum_zero_subarrays(arr):
    n = len(arr)
    arrs = []

    s = 0
    sum_map = defaultdict(list)
    for i in range(n):
        s  += arr[i]

        if s == 0:
            arrs.append((0, i))

        if s in sum_map:
            for j in sum_map[s]:
                arrs.append((j+1, i))

        sum_map[s].append(i)

    return arrs

arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print(all_sum_zero_subarrays(arr))
