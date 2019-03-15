import heapq

# wrong answer
def partition(arr):
    sub1 = []
    sum1 = 0
    sub2 = []
    sum2 = 0

    while len(arr) > 0:
        v = arr.pop()
    if abs(sum1+v-sum2) < abs(sum1-(sum2+v)):
        heapq.heappush(sub1, v)
        sum1 += v
    else:
        heapq.heappush(sub2, v)
        sum2 += v

    while True:
        if len(sub1) > 0 and abs(sum1-sub1[0]-(sum2+sub1[0])) < abs(sum1-sum2):
            sum1 -= sub1[0]
            sum2 += sub1[0]
            heapq.heappush(sub2, heapq.heappop(sub1))
        elif len(sub2) > 0 and abs(sum1+sub2[0]-(sum2-sub2[0])) < abs(sum1-sum2):
            sum1 += sub2[0]
            sum2 -= sub2[0]
            heapq.heappush(sub1, heapq.heappop(sub2))
        else:
            break

    return abs(sum1 - sum2)

def find_min_diff(arr):
    n = len(arr)
    s = sum(arr)

    dp = [[None for _ in range(s+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for j in range(1,s+1):
        dp[0][j] = False

    for i in range(1, n+1):
        for j in range(1,s+1):
            dp[i][j] = dp[i-1][j]

            if j >= arr[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]

    # # for debuging
    # print(arr)
    # for i in range(n+1):
    #     print(dp[i])

    j = s//2
    while j >= 0:
        if dp[n][j]:
            diff = (s - j) - j
            break
        j -= 1

    return diff

# arr = [1, 6, 11, 5]
arr = [3, 1, 4, 2, 2, 1]

print(find_min_diff(arr)) # 1
