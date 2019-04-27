from random import randint

# O(n)
def shuffle_iter(d):
    n = len(d)
    i = 0
    while i < n: 
        x = randint(i, n-1) # pick number ranonmly
        d[i], d[x] = d[x], d[i] # flip
        i += 1
    return d

# O(n)
def shuffle_recur(d):
    n = len(d)
    i = 0
    shuffle_recur_helper(d, i, n-1)
    return d

def shuffle_recur_helper(d, i, j):
    if i >= j:
        return
    shuffle_recur_helper(d, i+1, j)
    x = randint(i+1, j)
    d[i], d[x] = d[x], d[i] # flip

d = [i for i in range(0, 52)]

print(shuffle_recur(d))
