def find_max_value(items, W, N):
    M = {}

    for n in range(N+1):
        if not n in M:
            M[n] = {}
        nth_value, nth_weight = items[n-1]
        for w in range(W+1):
            if n == 0 or w == 0:
                M[n][w] = 0
            elif nth_weight <= w:
                value_include_nth = nth_value + M[n-1][w-nth_weight]
                M[n][w] = max([value_include_nth, M[n-1][w]])
            else:
                M[n][w] = M[n-1][w]
    return M[N][W]


items = [(60, 10), (100, 20), (120, 30)]
W = 50
N = len(items)

max_value = find_max_value(items, W, N)
print('Max Value', max_value)
