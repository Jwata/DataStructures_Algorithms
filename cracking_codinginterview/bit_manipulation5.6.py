def flip_count(a, b):
    c = a ^ b

    cnt = 0
    step = 0
    while c > 0:
        step += 1
        print("step %s" % step)
        if c & 1:
            cnt += 1
        c >>= 1

    return cnt

def flip_count_better(a, b):
    c = a ^ b

    cnt = 0
    step = 0
    while c > 0:
        step += 1
        print("step %s" % step)
        cnt += 1
        c &= c - 1

    return cnt

print(flip_count(29, 15))
print(flip_count_better(29, 15))
