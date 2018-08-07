import heapq
from collections import defaultdict

# dijkstra
def find_shortest_route(n, road_map, s):
    distances = [-1]*n
    distances[s-1] = 0
    prevs = [None]*n

    nodes = [(0, s)]
    while len(nodes) > 0:
        cost, node = heapq.heappop(nodes)
        if distances[node-1] == -1 or distances[node-1] == cost:
            for neighbor, weight in road_map[node]:
                if distances[neighbor-1] == -1 or distances[neighbor-1] > cost+weight:
                    distances[neighbor-1] = cost+weight
                    prevs[neighbor-1] = node
                    heapq.heappush(nodes, (cost+weight, neighbor))

    return distances, prevs


def retrive_route(prevs, s, g):
    current = g
    shortest_route = [g]
    while True:
        if current == s:
            break
        shortest_route = [prevs[current-1]] + shortest_route
        current = prevs[current-1]

    return shortest_route


def sync_shopping(n, k, loc_to_fishes, fish_to_locs, road_map):
    fishes = set()
    fishes.update(loc_to_fishes[1]) # fishes at start
    fishes.update(loc_to_fishes[n]) # fishes at goal

    distances, prevs = find_shortest_route(n, road_map, 1)
    shortest_route = retrive_route(prevs, 1, n)

    for i in shortest_route:
        fishes.update(loc_to_fishes[i]) # fishes at the i-th

    if len(fishes) == k:
        return distances[n-1]
    else:
        stopping_by = set()
        for f in range(1, k+1):
            if not f in fishes:
                locs = fish_to_locs[f]
                tmp_loc = locs.pop()
                tmp_dist = distances[tmp_loc-1]
                for loc in locs:
                    if tmp_dist >= distances[loc-1]:
                        tmp_loc = loc
                        tmp_dist = distances[loc-1]
                stopping_by.add(tmp_loc)

        total_distance = 0
        while stopping_by:
            dest = stopping_by.pop()
            route_to_dest = retrive_route(prevs, 1, dest)
            total_distance += distances[dest-1]

            distances_to_goal, _prevs = find_shortest_route(n, road_map, dest)
            route_to_goal = retrive_route(_prevs, dest, n)
            total_distance += distances_to_goal[n-1]

            for loc in stopping_by:
                if loc in route_to_dest:
                    stopping_by.remove(loc)
                if loc in route_to_goal:
                    stopping_by.remove(loc)
        return total_distance


if __name__ == '__main__':
    input_path = 'data/synchronous_shopping.input02.txt'
    output_path = 'data/synchronous_shopping.output02.txt'

    input_file = open(input_path)
    output_file = open(output_path)
    output = int(output_file.readline())

    nmk = list(map(int, input_file.readline().rstrip().split()))
    n = nmk[0]
    m = nmk[1]
    k = nmk[2]

    loc_to_fishes = defaultdict(list)
    fish_to_locs = defaultdict(list)
    for i in range(1, n+1):
        fishes_at_i = list(map(int, input_file.readline().rstrip().split()))
        loc_to_fishes[i] = fishes_at_i[1:]
        for f in fishes_at_i[1:]:
            fish_to_locs[f].append(i)

    road_map = defaultdict(list)
    for _ in range(m):
        u, v, w = list(map(int, input_file.readline().rstrip().split()))
        road_map[u].append((v, w))
        road_map[v].append((u, w))

    result = sync_shopping(n, k, loc_to_fishes, fish_to_locs, road_map)
    print(result)

    assert result == output, output
