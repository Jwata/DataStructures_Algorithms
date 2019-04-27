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

def random_set_recur(a, m):
    n = len(a)
    if m > n:
        raise Exception("m is too big")
    if m == 0:
        return []
    x = randint(0, n-1)
    ax = a[x]
    a[n-1], a[x] = a[x], a[n-1]
    return [ax] + random_set_recur(a[:-1], m-1)



a = [i for i in range(0, 100)]
m = 3
s = random_set_recur(a, m)
print(s)
