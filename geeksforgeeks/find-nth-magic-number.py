def find_magic_number(n):
    p = 1
    m = 0
    while n:
        p = p * 5
        if n & 1:
            m += p
        n = n >> 1

    return m

print(find_magic_number(5))
