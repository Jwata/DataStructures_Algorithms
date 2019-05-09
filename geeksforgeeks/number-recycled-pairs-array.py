import math
from collections import defaultdict

# O(n)
def find_recycled_pairs(arr):
    rot_map = defaultdict(lambda: [])
    pairs = []
    for x in arr:
        # find pairs
        if x in rot_map:
            for y in rot_map[x]:
                pairs.append((x, y))

        # insert rotations
        x_rot = rotate(x)
        while x_rot != x:
            rot_map[x_rot].append(x)
            x_rot = rotate(x_rot)
    return pairs

def rotate(x):
    d = int(math.log10(x) + 1) # num of digits
    x_rot = x
    x_rot += (x % 10) * (10 ** d)
    x_rot = x_rot // 10
    return x_rot

arr = [32, 42, 13, 23, 9, 5, 31]
print(find_recycled_pairs(arr))

arr = [1212, 2121]
print(find_recycled_pairs(arr))

