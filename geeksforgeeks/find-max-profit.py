def find_max_profit(arr):
    n = len(arr)

    smallest = arr[0]
    max_profit = 0

    for i in range(1, n):
        if smallest < arr[i]:
            profit = arr[i] - smallest
            if max_profit < profit:
                max_profit = profit
        else:
            smallest = arr[i]

    return max_profit


arr = [21, 18, 14, 2, 11, 3, 17, 19, 21, 3, 8]
print(find_max_profit(arr))
