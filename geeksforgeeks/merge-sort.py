def merge_sort(arr):
    n = len(arr)
    return merge_sort_helper(arr, 0, n-1)

def merge_sort_helper(arr, i, j):
    if i == j:
        return [arr[i]]

    mid = (i + j) // 2
    a = merge_sort_helper(arr, i, mid)
    b = merge_sort_helper(arr, mid+1, j)

    merged = []
    while len(a) > 0 or len(b) > 0:
        if len(a) > 0 and len(b) > 0:
            if a[0] < b[0]:
                merged.append(a.pop(0))
            else:
                merged.append(b.pop(0))
        elif len(a) > 0:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))

    return merged

arr = [12,11,13,5,6,7]
print(merge_sort(arr))
