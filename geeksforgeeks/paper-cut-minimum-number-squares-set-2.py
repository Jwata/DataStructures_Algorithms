MAX_INT = 2 ** 32

def min_squares_wrapper(n, m):
    dp = [[None for _ in range(m)] for _ in range(n)]
    return min_squares(n, m, dp)

def min_squares(n, m, dp):
    if dp[n-1][m-1]:
        return dp[n-1][m-1]

    if n == m:
        dp[n-1][m-1] = 1
        return 1

    min_horizontal = MAX_INT
    for i in range(1, n//2+1):
        min_horizontal = min(min_horizontal,
            min_squares(i, m, dp) + min_squares(n-i, m, dp))

    min_vertical = MAX_INT
    for j in range(1, m//2+1):
        min_vertical = min(min_vertical,
            min_squares(n, j, dp) + min_squares(n, m-j, dp))

    dp[n-1][m-1] = min(min_horizontal, min_vertical)
    return dp[n-1][m-1]

print(min_squares_wrapper(1, 5))
print(min_squares_wrapper(4, 5))
print(min_squares_wrapper(30, 36))
