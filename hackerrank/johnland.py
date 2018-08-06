#!/bin/python3

import os
import sys
from collections import defaultdict
import heapq
from functools import reduce
from operator import add


def will_have_cycle(mst, edge):
    u, v = edge
    visited = set()

    nodes = [u]
    while nodes:
        current = nodes.pop()
        if current == v:
            return True
        visited.add(current)
        neighbors = mst.get_neighbors_from(current)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            nodes.append(neighbor)

    return False

class MST:
    def __init__(self):
        self.edges = set()
        self.nodes = set()
        self.M = defaultdict(list)

    def get_neighbors_from(self, node):
        return self.M[node]

    def add_edge(self, u, v, w):
        self.M[u].append(v)
        self.M[v].append(u)
        self.nodes.update([u, v])
        self.edges.add((u, v, w))

    def total_cost(self):
        return reduce(add, [w for _, _, w in self.edges])


def roadsInHackerland(g_nodes, edges):
    mst = MST()

    step = 0
    while len(mst.edges) < g_nodes - 1:
        step += 1
        w, u, v = heapq.heappop(edges)
        if will_have_cycle(mst, (u, v)):
            continue
        mst.add_edge(u, v, w)

    # TODO: count use of edges
    # https://www.hackerrank.com/challenges/johnland/forum/comments/162420
    return mst.total_cost()


if __name__ == '__main__':
    inputs = open('data/johnland.input05.txt')
    output = open('data/johnland.output05.txt').readline().rstrip()

    nm = inputs.readline().rstrip().split(' ')

    n = int(nm[0])

    m = int(nm[1])

    # W = defaultdict(dict)
    # for i in range(m):
    #     u, v, w = map(int, inputs.readline().rstrip().split())
    #     W[u][v] = W[v][u] = min(w, W[u].get(v, 2*10**5))

    edges = []
    for i in range(m):
        u, v, w = map(int, inputs.readline().split())
        heapq.heappush(edges, (w, u, v))

    result = roadsInHackerland(n, edges)
    print(result)

    assert result == output, output
