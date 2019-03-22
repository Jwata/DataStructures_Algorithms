def pick_optimal_helper(i, j, arr, dp):
    if dp[i][j]:
        return dp[i][j]

    s1 = arr[i] + \
        min(pick_optimal_helper(i+2, j, arr, dp),
            pick_optimal_helper(i+1, j-1, arr, dp))
    s2 = arr[j] + \
        min(pick_optimal_helper(i, j-2, arr, dp),
            pick_optimal_helper(i+1, j-1, arr, dp))
    dp[i][j] = max(s1, s2)
    return dp[i][j]


def pick_optimal(arr):
    n = len(arr)
    dp = []
    for i in range(n):
        dp.append([])
        for j in range(n):
            if i == j:
                dp[i].append(arr[i])
            elif i+1 == j:
                dp[i].append(max(arr[i], arr[j]))
            else:
                dp[i].append(None)

    return pick_optimal_helper(0, n-1, arr, dp)

arr = [5, 3, 7, 10]
print(pick_optimal(arr))

arr = [8, 15, 3, 7]
print(pick_optimal(arr))

arr = [2, 2, 2, 2]
print(pick_optimal(arr))

arr = [20, 30, 2, 2, 2, 10] 
print(pick_optimal(arr))
