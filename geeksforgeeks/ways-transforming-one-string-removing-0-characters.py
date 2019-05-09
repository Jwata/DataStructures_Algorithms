def find_trans_ways(A, B):
    n = len(A)
    m = len(B)

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # base cases
    for i in range(n+1):
        dp[i][0] = 1

    for j in range(1, m+1):
        for i in range(1, n+1):
            dp[i][j] += dp[i-1][j]
            if A[i-1] == B[j-1]:
               dp[i][j] += dp[i-1][j-1]

    return dp[n][m]

A = 'aabba'
B = 'ab'
print(find_trans_ways(A, B))

A = 'abcccdf'
B = 'abccdf'
print(find_trans_ways(A, B))
