#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
import time
from collections import defaultdict

# Complete the shortestReach function below.
def shortestReach(n, edge_map, s):
    distances = [-1 for _ in range(n)]
    distances[s-1] = 0

    nodes = [(0, s)]
    while len(nodes) > 0:
        cost, node = heapq.heappop(nodes)
        if distances[node-1] == -1 or distances[node-1] == cost:
            distances[node-1] = cost
            for neighbor, weight in edge_map[node].items():
                if distances[neighbor-1] == -1 or distances[neighbor-1] > cost+weight:
                    distances[neighbor-1] = cost+weight
                    heapq.heappush(nodes, (cost+weight, neighbor))

    return distances[:s-1] + distances[s:]

if __name__ == '__main__':
    inputs = open('data/dijkstrashortreach.inputs01.txt')
    outputs = open('data/dijkstrashortreach.outputs01.txt').readlines()

    t = int(inputs.readline().rstrip())

    for t_itr in range(t):
        nm = inputs.readline().rstrip().split(' ')

        n = int(nm[0])

        m = int(nm[1])

        W = defaultdict(dict)
        for i in range(m):
            u, v, w = map(int, inputs.readline().rstrip().split())
            W[u][v] = W[v][u] = min(w, W[u].get(v, 10**5))

        s = int(inputs.readline().rstrip())

        result = shortestReach(n, W, s)
        output = list(map(int, outputs[t_itr].rstrip().split(' ')))
        print(result)
        print(output)

        assert result == output
