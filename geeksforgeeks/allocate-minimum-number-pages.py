from pprint import pprint

MAX_INT = 2 ** 32

def alloc(pages, m):
    n = len(pages)
    S = construct_sum_map(pages)
    M = [[None for _ in range(n)] for _ in range(m)]
    min_pages = alloc_helper(n, m, S, M, 0)
    pprint(M)
    return min_pages

def alloc_helper(n, m, S, M, start):
    if m == 1:
        return S[start][n-1]
    if M[m-1][start]:
        return M[m-1][start]

    min_max_pages = MAX_INT
    for end in range(start, n-m+1):
        max_pages = max(S[start][end], alloc_helper(n, m-1, S, M, end+1))
        min_max_pages = min(max_pages, min_max_pages)

    M[m-1][start] = min_max_pages
    return min_max_pages


def construct_sum_map(pages):
    n = len(pages)
    curr_sum = 0
    S = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        curr_sum += pages[i]
        S[0][i] = curr_sum
    for i in range(1, n):
        for j in range(i, n):
            S[i][j] = S[0][j] - S[0][i-1]
    return S

pages = [1, 2, 3, 4, 5, 6, 7]
m = 4
min_pages = alloc(pages, m)
print(min_pages)
