def search_rotated_array(arr, target):
    l = 0 
    r = len(arr) - 1 

    while l <= r:
        if arr[l] == target:
            return l
        elif arr[r] == target:
            return r
        elif target < arr[l] and target > arr[r]:
            return None

        p = (l + r) / 2
        if target == arr[p]:
            return p
        elif target < arr[p]:
            if target < arr[l]:
                l = p+1
                r -= 1
            else:
                l += 1
                r = p-1
        else:
            if target > arr[r]:
                l += 1
                r = p-1
            else:
                l = p+1
                r -= 1

    return None

arr = [5,6,7,8,9,10,1,2,3]
print(search_rotated_array(arr, 3)) # 8
print(search_rotated_array(arr, 30)) # None

arr = [30, 40, 50, 10, 20]
print(search_rotated_array(arr, 10)) # 3

