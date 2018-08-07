#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the bfs function below.
def bfs(n, m, M, s):
    nodes = [(s, 0)]
    visited = set()
    distances = [-1]*n
    distances[s-1] = 0

    while nodes and len(visited) < n:
        current, distance = nodes.pop(0)
        if current in visited:
            continue
        visited.add(current)
        for ngbr in M[current]:
            if not ngbr in visited:
                ngbr_dist = distance+6
                if distances[ngbr-1] == -1 or distances[ngbr-1] > ngbr_dist:
                    distances[ngbr-1] = ngbr_dist
                    nodes.append((ngbr, ngbr_dist))

    return [d for d in distances if d != 0]

                             
if __name__ == '__main__':
    inputs = open('data/bfs_shortest_path.input01.txt')
    outputs = open('data/bfs_shortest_path.output01.txt')

    q = int(inputs.readline())

    for q_itr in range(q):
        nm = inputs.readline().split()

        n = int(nm[0])

        m = int(nm[1])

        output = list(map(int, outputs.readline().rstrip().split()))

        M = defaultdict(set)

        for _ in range(m):
            u, v = list(map(int, inputs.readline().rstrip().split()))
            M[u].add(v)
            M[v].add(u)

        s = int(inputs.readline())

        result = bfs(n, m, M, s)
        print(result)

        assert result == output, output
