
NUM_BITS = 32
def sum_bit_diffs(arr):
    s = 0

    n = len(arr)
    for i in range(NUM_BITS):
        n_ones = 0
        n_zeros = 0
        for x in arr:
            if x & (1 << i) > 0:
                n_ones += 1
            else:
                n_zeros += 1

        s += (n_ones * n_zeros) * 2

    return s

arr = [1, 3, 5] # [0b001, 0b011, 0b101]
print(sum_bit_diffs(arr))
