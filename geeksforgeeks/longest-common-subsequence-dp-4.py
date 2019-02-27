def L(seq1, seq2):
    if len(seq1) == 0 or len(seq2) == 0:
        return 0

    if seq1[-1] == seq2[-1]:
        return 1 + L(seq1[0:-1], seq2[0:-1])
    else:
        return max(L(seq1[0:-1], seq2), L(seq1, seq2[0:-1]))


print(L("ABCDGH", "AEDFHE"))
print(L("AGGTAB", "GXTXAYB"))


def L_dp(x, y):
    n = len(x)
    m = len(y)

    dp = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


print(L_dp("ABCDGH", "AEDFHE"))
print(L_dp("AGGTAB", "GXTXAYB"))


def L_dp2(str1, str2, i, j, dp):
    if dp[i][j] is not None:
        return dp[i][j]

    if i == 0  or j == 0:
        dp[i][j] = 0
    elif str1[i-1] == str2[j-1]:
        dp[i][j] = L_dp2(str1, str2, i - 1, j - 1, dp) + 1
    else:
        dp[i][j] = max(
            L_dp2(str1, str2, i - 1, j, dp), L_dp2(str1, str2, i, j - 1, dp))

    return dp[i][j]


dp = [[None] * 7 for _ in range(7)]
print(L_dp2("ABCDGH", "AEDFHE", 6, 6, dp))
dp = [[None] * 8 for _ in range(7)]
print(L_dp2("AGGTAB", "GXTXAYB", 6, 7, dp))
