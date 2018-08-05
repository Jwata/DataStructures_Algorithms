#!/bin/python3

import math
import os
import random
import re
import sys

def dfs(node, city_map, covered, uncovered, c_road):
    # traverse from the city
    cost = 0
    nodes = [node]
    while len(nodes) > 0:
        city = nodes.pop()
        neighbors = city_map[city]
        for neighbor in neighbors:
            if neighbor in covered:
                continue
            cost += c_road
            uncovered.remove(neighbor)
            covered.add(neighbor)
            nodes.append(neighbor)
    return cost, covered, uncovered

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    city_map = {i: [] for i in range(1, n+1)}

    for road in cities:
        city_map[road[0]].append(road[1])
        city_map[road[1]].append(road[0])

    cost = 0
    covered = set()
    uncovered = set(range(1, n+1))

    while len(covered) < n:
        city = uncovered.pop()

        # build library in the city
        cost += c_lib
        covered.add(city)

        if c_lib > c_road:
            sub_cost, covered, uncovered = \
                    dfs(city, city_map, covered, uncovered, c_road)
            cost += sub_cost

    return cost


if __name__ == '__main__':
    inputs = open('data/torque_and_development.inputs2.txt')
    outputs = open('data/torque_and_development.outputs2.txt').readlines()
    q = int(inputs.readline().split('\n')[0])
    for q_itr in range(q):
        nmC_libC_road = inputs.readline().split(' ')

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        output = int(outputs[q_itr].split('\n')[0])

        for _ in range(m):
            cities.append(list(map(int, inputs.readline().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
        assert result == output
