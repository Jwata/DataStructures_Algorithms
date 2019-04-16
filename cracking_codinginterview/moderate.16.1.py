def swap_numbers(a, b):
    a = a - b
    b = b + a
    a = b - a
    return a, b

def swap_numbers_bit(a, b):
    a = a ^ b
    b = a ^ b

a = 2
b = 3

a, b = swap_numbers(a, b)
print(a, b)

# a ^ b = a'
# 1 ^ 1 = 0 
# 0 ^ 0 = 0 
# 1 ^ 0 = 1 
# 0 ^ 1 = 1 
# 
# b ^ (a') = b' == a
# 1 ^ (1 ^ 1) = 1
# 0 ^ (0 ^ 0) = 0
# 1 ^ (0 ^ 1) = 0
# 0 ^ (1 ^ 0) = 1
# 
# a' ^ b'
