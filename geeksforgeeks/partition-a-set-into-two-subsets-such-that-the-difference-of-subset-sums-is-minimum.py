import heapq

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

arr = [1, 6, 11, 5]

print(partition(arr)) # 1
