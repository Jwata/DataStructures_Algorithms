# Next Number
import math

# Debug
# 13 (1101) -> 14 (1110) next largest
# 13 (1101) -> 11 (1011) next smallest

def next_largest(a):
    n = int(math.log2(a)) + 1

    n_zeros = 0

    i = 0
    for i in range(n):
        if a & (1 << i):
            if not a & (1 << (i+1)):
                a ^= (1 << i) # 1 to 0 a ^= (1 << (i+1)) # 0 to 1

                right_mask = 2 ** i - 1
                right = a & right_mask
                right >>= n_zeros

                left_mask = 2 ** (n+1) - 1
                left_mask <<= i
                left = a & left_mask

                return left ^ right
        else:
            n_zeros += 1

    # error

def next_smallest(a):
    n = int(math.log2(a)) + 1

    prev_zero = None

    i = 0
    for i in range(n):
        if a & (1 << i):
            if prev_zero:
                a ^= (1 << i) # 1 to 0
                a ^= (1 << prev_zero) # 0 to 1
                return a
        else:
            prev_zero = i

    # error

# 13(1101)
print(next_largest(13)) # 14(1110)
print(next_smallest(13)) # 11(1011)

# 3(11)
print(next_largest(3)) # 5(101)
print(next_smallest(3)) # None

# 44(101100)
print(next_largest(44)) # 49(110001)
print(next_smallest(44)) # 42(101010)

101110
11011
