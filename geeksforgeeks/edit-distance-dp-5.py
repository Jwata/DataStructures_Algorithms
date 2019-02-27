def lcs(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[None] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

def min_num_edit(str1, str2):
    ll = lcs(str1, str2)

    if len(str1) <= len(str2):
        return len(str2) - ll
    else:
        return len(str2) - ll + len(str1) - len(str2)


str1 = "sunday"
str2 = "saturday"
print(min_num_edit(str1, str2)) # should be 3

str1 = "saturday"
str2 = "sunday"
print(min_num_edit(str1, str2)) # should be 3
