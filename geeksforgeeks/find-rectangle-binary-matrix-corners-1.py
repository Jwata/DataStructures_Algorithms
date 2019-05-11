from collections import defaultdict

def find_rectangle(M, n, m):
    T = defaultdict(lambda: defaultdict(lambda: False))

    for i in range(n):
        # find pairs in a row
        for j in range(m-1):
            if M[i][j] == 0:
                continue
            for k in range(j+1, m):
                if M[i][k] == 0:
                    continue
                if T[j][k]:
                    return True
                T[j][k] = True

    return False

M = [ \
 [1, 0, 0, 1, 0], \
 [0, 0, 1, 0, 1], \
 [0, 0, 0, 1, 0], \
 [1, 0, 1, 0, 1], \
]
n = 4
m = 5
print(find_rectangle(M, n, m))

M = [ \
 [1, 0, 0], \
 [0, 0, 1], \
 [0, 0, 0], \
 [1, 0, 1], \
]
n = 4
m = 3
print(find_rectangle(M, n, m))
