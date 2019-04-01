def bit_diff(a, b):
    x = a ^ b
    
    s = 0
    while x > 0:
        s += x & 1
        x >>= 1

    return s

def sum_bit_diffs(arr):
    n = len(arr)

    s = 0
    for i in range(n):
        a = arr[i]
        for j in range(n):
            b = arr[j]
            s += bit_diff(a, b)

    return s


NUM_BITS = 5

def sum_bit_diffs_optimal(arr):
    n = len(arr)

    s = 0
    for i in range(NUM_BITS):
        cnt = 0
        b = 1 << i
        for j in range(n):
            if arr[j] & b:
                cnt += 1

        s += cnt * (n-cnt) * 2

    return s

# print(bit_diff(1, 1)) # 0
# print(bit_diff(1, 2)) # 2
# print(bit_diff(1, 3)) # 1
# print(bit_diff(1, 5)) # 1
# print(bit_diff(3, 5)) # 2

# arr = [1, 2]
# print(sum_bit_diffs(arr))
# 
# arr = [1, 3, 5]
# print(sum_bit_diffs(arr))

arr = [1, 3, 5]
print(sum_bit_diffs_optimal(arr))
