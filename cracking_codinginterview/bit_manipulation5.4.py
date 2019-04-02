# Next Number
import math

# Debug
# 13 (1101) -> 14 (1110) next largest
# 13 (1101) -> 11 (1011) next smallest

def next_largest(a):
    n = int(math.log2(a)) + 1

    n_zeros = 0

    for i in range(n):
        if a & (1 << i):
            if not a & (1 << (i+1)):
                break
        else:
            n_zeros += 1

    a ^= (1 << i) # 1 to 0
    a ^= (1 << (i+1)) # 0 to 1

    right_mask = 2 ** i - 1
    right = a & right_mask
    right >>= n_zeros

    left_mask = 2 ** (n+1) - 1
    left_mask <<= i
    left = a & left_mask

    return left | right

def next_smallest(a):
    n = int(math.log2(a)) + 1

    prev_zero = None

    i = 0
    for i in range(n):
        if a & (1 << i):
            if prev_zero:
                break
        else:
            prev_zero = i

    if prev_zero:
        a ^= (1 << i) # 1 to 0
        a ^= (1 << prev_zero) # 0 to 1

        # TODO: modify to shift ones to left
        return a

# 13(1101)
print(next_largest(13)) # 14(1110)
print(next_smallest(13)) # 11(1011)

# 3(11)
print(next_largest(3)) # 5(101)
print(next_smallest(3)) # None

# 44(101100)
print(next_largest(44)) # 49(110001)
print(next_smallest(44)) # 42(101010)

# 13948(11011001111100)
v = 13948
print('{}({:b})'.format(v, v))
l = next_largest(v)
print('next: {}({:b})'.format(l, l))
s = next_smallest(v)
print('prev: {}({:b})'.format(s, s))

# 10115(10011110000011)
v = 10115
print('{}({:b})'.format(v, v))
l = next_largest(v)
print('next: {}({:b})'.format(l, l))
s = next_smallest(v)
print('prev: {}({:b})'.format(s, s))
