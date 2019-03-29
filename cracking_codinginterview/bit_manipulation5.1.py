NUM_BITS = 32

def insert_bit(n, m, i, j):
    # mask = 0
    # num_n = int(math.log2(n)) + 1
    # for k in range(num_n):
    #     if k in range(i, j+1):
    #         continue
    #     mask |= (1 << k)
    left_mask = (1 << NUM_BITS) - 1
    left_mask <<= j
    right_mask = 1 << i
    mask = left_mask | right_mask

    print('mask: {:b}'.format(mask))

    n &= mask
    n |= (m << i)

    return n

n = 1 << 10 # 10000000000
m = 19 # 10011
i = 2
j = 6

n = insert_bit(n, m, i, j)
print('out: {:b}'.format(n))
