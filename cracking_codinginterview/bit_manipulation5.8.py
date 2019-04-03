NUM_BITS = 8

def draw_line(screen, w, x1, x2, y):
    byte_index = None
    b = None
    for i in range(x1, x2+1):
        pixel_at = get_byte_index(w, i, y)
        if not byte_index or pixel_at != byte_index:
            b = screen[pixel_at]

        bit = get_bit_from_byte(b, i % 8)
        print(bit, end="")

def get_byte_index(w, x, y):
    return (w * y + x) // NUM_BITS

def get_bit_from_byte(b, x):
    if b & (1 << (NUM_BITS - x - 1)):
        return 1
    else:
        return 0


# 10101011 | 10101100
# 11010111 | 11011101
screen = bytearray()
screen.append(int('10101011', 2))
screen.append(int('10101100', 2))
screen.append(int('11010111', 2))
screen.append(int('11011101', 2))

draw_line(screen, 16, 3, 12, 1)
