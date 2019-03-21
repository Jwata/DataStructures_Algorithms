def longest_path_from(i, j, m, dp, n):
    if dp[i][j] is not None:
        return dp[i][j]

    if  i+1 < n and m[i+1][j] == m[i][j] + 1:
        dp[i][j] = 1 + longest_path_from(i+1, j, m, dp, n)
    elif i-1 >= 0 and m[i-1][j] == m[i][j] + 1:
        dp[i][j] = 1 + longest_path_from(i-1, j, m, dp, n)
    elif j+1 < n and m[i][j+1] == m[i][j] + 1:
        dp[i][j] = 1 + longest_path_from(i, j+1, m, dp, n)
    elif j-1 >= 0 and m[i][j-1] == m[i][j] + 1:
        dp[i][j] = 1 + longest_path_from(i, j+1, m, dp, n)
    else:
        dp[i][j] = 1

    return dp[i][j]


def longest_path(m, n):
    dp = [[None for _ in range(n)] for _ in range(n)]
    longest = 1

    for i in range(n):
        for j in range(n):
            p = longest_path_from(i, j, m, dp, n)
            longest = max(longest, p)

    return longest

n = 3
m = [[1, 2, 9],\
     [5, 3, 8],\
     [4, 6, 7]]

print(longest_path(m, n))
