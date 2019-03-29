NUM_BITS = 32

def float_to_bits(v):
    if v > 1:
        raise Exception("invalid argument")

    a = 1
    bits = "."

    for i in range(NUM_BITS):
        a /= 2
        if v >= a:
            bits += "1"
            v -= a
        else:
            bits += "0"

        if v == 0:
            return bits

    raise Exception("Error")

def float_to_bits2(v):
    if v > 1:
        raise Exception("invalid argument")

    a = 1
    bits = "."

    for i in range(NUM_BITS):
        v  = 2 * v
        if v >= 1:
            bits += "1"
            v -= a
        else:
            bits += "0"

        if v == 0:
            return bits

    raise Exception("Error")

print(float_to_bits(0.5))
print(float_to_bits(0.75))
print(float_to_bits(0.25))
print(float_to_bits(0.375))
print(float_to_bits(1/3))
