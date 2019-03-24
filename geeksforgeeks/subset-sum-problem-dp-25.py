def subset_sum(arr, k):
    n = len(arr)
    dp = [[None for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(1, k+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(k+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[n][k]


arr = [3, 34, 4, 12, 5, 2]
k = 9

print(subset_sum(arr, k))

