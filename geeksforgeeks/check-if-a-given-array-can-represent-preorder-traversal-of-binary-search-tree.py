def check_preorder(arr):
    buf = [arr[0]]
    min_v = None

    for i in range(1, len(arr)):
        v = arr[i]

        if min_v is not None and v < min_v:
            return False

        while len(buf) > 0 and buf[-1] < v:
            min_v = buf[-1]
            buf.pop()

        buf.append(v)

    return True

pre = [2, 4, 3]
print(check_preorder(pre))

pre = [40, 30, 35, 80, 100]
print(check_preorder(pre))

pre = [40, 30, 35, 20, 80, 100]
print(check_preorder(pre))
