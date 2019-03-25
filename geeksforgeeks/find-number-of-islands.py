def count_island(mat, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0 or visited[i][j]:
                continue
            dfs(mat, n, m, i, j,visited)
            cnt += 1
    return cnt

def dfs(mat, n, m, i, j, visited):
    if visited[i][j]:
        return

    visited[i][j] = True
    for k in range(i-1, i+2):
        if k < 0 or k >= n:
            continue
        for l in range(j-1, j+2):
            if l < 0 or l >= m:
                continue
            if mat[k][l] == 0 or visited[k][l]:
                continue
            dfs(mat, n, m, k, l, visited)

mat = [[1,1,0,0,0], \
       [0,1,0,0,1], \
       [1,0,0,1,1], \
       [0,0,0,0,0], \
       [1,0,1,0,1]]
n = 5
m = 5

print(count_island(mat, n, m))
