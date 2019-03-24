def stock_span(arr):
    n = len(arr)
    buf = []
    spans = []

    for i in range(n):
        while len(buf) > 0 and arr[buf[-1]] <= arr[i]:
            buf.pop()

        if len(buf) > 0:
            span = i - buf[-1]
        else:
            span = i + 1

        buf.append(i)
        spans.append(span)

    return spans

# i = 6
# buf = [0, 6]
# spans = [1, 1, 1, 2, 1, 4, 6]

arr = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(arr))
