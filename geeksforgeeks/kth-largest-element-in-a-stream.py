import heapq

stream = [10, 20, 11, 70, 50, 40, 100, 5]

k = 3
buf = []
for v in stream:
    if len(buf) >= k:
        if v > buf[0]:
            heapq.heappop(buf)
            heapq.heappush(buf, v)
    else:
        heapq.heappush(buf, v)

    if len(buf) == k:
        print(buf[0])
    else:
        print(None)
