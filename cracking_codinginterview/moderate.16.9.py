def subtract(a, b):
    s = -1 if b > 0 else 1

    while b != 0:
        a += s
        b += s

    return a

def multiply(a, b):
    x = 0

    while b != 0:
        if b > 0:
            x += a
            b += -1
        else:
            x = subtract(x, a)
            b += 1

    return x

def divide(a, b):
    if b < 0:
        b_ = multiply(b, -1)

    x = 0
    p = 0
    while p + b_ < a:
        p += b_
        x += 1

    if b < 0:
        x = multiply(x, -1)

    return x

x = divide(10, -3)
print(x)
