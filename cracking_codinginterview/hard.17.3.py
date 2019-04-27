# random set
from random import randint

def random_set(a, m):
    n = len(a)
    if m > n:
        raise Exception("m is too big")
    s = set()
    k = n-1
    while len(s) < m:
        x = randint(0, k)
        s.add(a[x])
        a[k], a[x] = a[x], a[k]
        k -= 1

    return s

a = [i for i in range(0, 100)]
m = 3
s = random_set(a, m)
print(s)
