#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from collections import defaultdict
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


def kruskal_mst(g_nodes, edges):
    mst = MST()

    while len(mst.edges) < g_nodes - 1:
        w, u, v = heapq.heappop(edges)
        if will_have_cycle(mst, (u, v)):
            continue
        mst.add_edge(u, v, w)

    return mst.total_cost()


if __name__ == '__main__':
    input_file = open('data/kruskal_mst.input03.txt')
    output_file = open('data/kruskal_mst.output03.txt')
    output = int(output_file.readline())

    g_nodes, g_edges = map(int, input_file.readline().split())

    edges = []

    for i in range(g_edges):
        u, v, w = map(int, input_file.readline().split())
        heapq.heappush(edges, (w, u, v))

    result = kruskal_mst(g_nodes, edges)
    print(result)
    assert result == output, output
