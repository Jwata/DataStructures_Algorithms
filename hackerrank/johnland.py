#!/bin/python3

import os
import sys
from collections import defaultdict 
import heapq

def shortestReach(n, W, s):
    distances = [-1 for _ in range(n)]
    distances[s-1] = 0

    nodes = [(0, s)]
    while len(nodes) > 0:
        cost, node = heapq.heappop(nodes)
        if distances[node-1] == -1 or distances[node-1] == cost:
            for neighbor, weight in W[node].items():
                if distances[neighbor-1] == -1 or distances[neighbor-1] > cost | (1 << weight):
                    distances[neighbor-1] = cost | (1 << weight)
                    heapq.heappush(nodes, (cost | (1 << weight), neighbor))

    sum_d = 0
    for d in distances:
        if d > 0:
            sum_d += d
    return sum_d


def roadsInHackerland(n, W):
    total = 0
    for s in range(1, n+1):
        total += shortestReach(n, W, s)
    return bin(total/2)[2:]


if __name__ == '__main__':
    inputs = open('data/johnland.input20.txt')
    output = open('data/johnland.output20.txt').readline().rstrip()

    nm = inputs.readline().rstrip().split(' ')

    n = int(nm[0])

    m = int(nm[1])

    W = defaultdict(dict)
    for i in range(m):
        u, v, w = map(int, inputs.readline().rstrip().split())
        W[u][v] = W[v][u] = min(w, W[u].get(v, 2*10**5))

    result = roadsInHackerland(n, W)
    print(result)

    assert result == output

