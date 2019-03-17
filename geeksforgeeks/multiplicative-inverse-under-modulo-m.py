def mod_inverse(a, m):
    if a == m:
        raise Exception("Modular inverse doesn't exist")

    a_inv = mod_power(a, m-2, m)
    return a_inv

def mod_power(a, b, m):
    if b == 0:
        return 1

    p = mod_power(a, b // 2, m) % m
    p = (p * p) % m

    if b % 2 == 0:
        return p
    else:
        return (a * p) % m

print(mod_inverse(3, 11)) # 4
