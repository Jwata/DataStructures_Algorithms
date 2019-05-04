# O(nW)
def max_value(values, weights, W):
    n = len(values) # number of items
    dp = [[None for _ in range(n+1)] for _ in range(W+1)]

    # initialization
    for i in range(n+1):
        dp[0][i] = 0
    for j in range(W+1):
        dp[j][0] = 0

    for i in range(1, n+1):
        v = values[i-1]
        w = weights[i-1]

        for j in range(1, W+1):
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
            if j >= w:
                dp[j][i] = max(dp[j][i], dp[j-w][i-1]+v)

    return dp[W][n]


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

max_v = max_value(values, weights, W)
print(max_v)
