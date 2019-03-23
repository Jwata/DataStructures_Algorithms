def find_largest_subarray(arr):
    n = len(arr)
    cnt = 0 
    cnt_map = {} 
    largest_size = 0
    largest_subarrays = []

    for i in range(n): # O(n)
        if arr[i] == 1:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0 or cnt in cnt_map:
            if cnt == 0:
                b = 0
            else:
                b = cnt_map[cnt] + 1

            size = i - b + 1
            if size == largest_size:
                largest_subarrays.append((b, i))
            elif size > largest_size:
                largest_subarrays = [(b, i)]
                largest_size = size

        if not cnt in cnt_map:
            cnt_map[cnt] = i
    return largest_subarrays

arr = [1, 0, 1, 1, 1, 0, 0]
print(find_largest_subarray(arr))

arr = [1, 1, 1, 1]
print(find_largest_subarray(arr))

arr = [0, 0, 1, 1, 0]
print(find_largest_subarray(arr))
