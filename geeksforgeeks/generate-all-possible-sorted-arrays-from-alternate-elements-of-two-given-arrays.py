# def sorted_arrays(a, b):
#     na = len(a)
#     nb = len(b)
# 
#     sorted_arrays = []
#     for s in range(na):
#         i = s
#         j = -1
#         turn_a = False
#         sorted_array = [a[i]]
# 
#         while i < na and j < nb:
#             if turn_a:
#                 i = find_grater_than(a, i+1, sorted_array[-1])
#                 if i is None:
#                     sorted_arrays.append(sorted_array)
#                     break
#                 sorted_array.append(a[i])
#             else:
#                 j = find_grater_than(b, j+1, sorted_array[-1])
#                 if j is None:
#                     break
#                 sorted_array.append(b[j])
#             turn_a ^= True
# 
#     return sorted_arrays
# 
# def find_grater_than(arr, s, k):
#     for i in range(s, len(arr)):
#         if arr[i] > k:
#             return i
#     return None

def sorted_arrays(a, b):
    n = len(a)
    m = len(b)
    c = []
    return sorted_arrays_helper(a, b, n, m, 0, -1, c, True)


def sorted_arrays_helper(a, b, n, m, i, j, c, turn_a):
    if turn_a:
        arrays = []
        if len(c) > 0 :
            arrays.append(c.copy())

        for k in range(i, n):
            if len(c) == 0 or a[k] > c[-1]:
                tmp = c.copy()
                tmp.append(a[k])
                arrays += sorted_arrays_helper(a, b, n, m, k, j+1, tmp, False)
        return arrays
    else:
        if j >= m:
            return []
        arrays = []
        for k in range(j, m):
            if b[k] > c[-1]:
                tmp = c.copy()
                tmp.append(b[k])
                arrays += sorted_arrays_helper(a, b, n, m, i+1, k, tmp, True)
        return arrays

a = [10, 15, 25]
b = [1, 5, 20, 30]
print(sorted_arrays(a, b))
