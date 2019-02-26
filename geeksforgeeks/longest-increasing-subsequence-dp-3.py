def LIS(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(n):
        for j in range(0, i):
            if arr[j] <= arr[i]: # TODO ask later
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(LIS(arr)) # should be 6

arr = [10, 22, 9, 33, 21, 50, 41, 80, 30]
print(LIS(arr)) # should be 5

# Time Complexity: O(n^2)
