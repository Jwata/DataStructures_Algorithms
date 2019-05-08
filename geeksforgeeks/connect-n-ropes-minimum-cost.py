import heapq

def connect_with_min_cost(ropes):
    n = len(ropes)

    heapq.heapify(ropes) # O(n log n)

    cost = 0
    while len(ropes) > 1:
        l1 = heapq.heappop(ropes)
        l2 = heapq.heappop(ropes)
        l_con = l1 + l2
        cost += l_con

        heapq.heappush(ropes, l_con)

    return cost, ropes[0]

ropes = [4, 3, 2, 6]
print(connect_with_min_cost(ropes))

