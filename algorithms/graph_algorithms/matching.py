from maxflow import *


def max_matching(weights):
    m = len(weights)
    n = len(weights[0])
    capacity = {}
    edges = set()
    s = 0
    t = m + n + 1
    for i in range(m):
        capacity[(s, i + 1)] = 1
    for j in range(n):
        capacity[(j + m + 1, t)] = 1
    for i in range(m):
        for j in range(n):
            if weights[i][j] != 0:
                capacity[(i + 1, j + m + 1)] = 1
                edges.add((i, j))
    compute_max_flow(capacity, s, t)
    ans = [-1] * m
    for (i, j) in edges:
        if capacity.get((i + 1, j + m + 1), -1) == 1:
            ans[i] = j
    return ans


def find_paths(f, s, t):
    ans = []
    q = [[s]]
    vis = set()
    while len(q) != 0:
        path = q.pop(0)
        u = path[-1]
        if u == t:
            ans.append(path)
            continue
        vis.add(u)
        for v in f[u]:
            if f[u][v] == 0 or v in vis: continue
            p2 = path[:]
            p2.append(v)
            q.append(p2)
    return ans


def greedy_augment(f, paths, s, t, weights):
    m = len(weights)
    n = len(weights[0])
    best_val = -math.inf
    best_path = None
    for path in paths:
        curr_val = 0
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            if u == s or v == t: continue
            if u in range(1, m + 1) and v in range(m + 1, m + n + 1):
                curr_val += weights[u - 1][v - m - 1]
            else:
                curr_val -= weights[v - 1][u - m - 1]
        if best_val < curr_val:
            best_val = curr_val
            best_path = path
    min_flow = math.inf
    for i in range(len(best_path) - 1):
        u = best_path[i]
        v = best_path[i + 1]
        min_flow = min(min_flow, f[u][v])
    for i in range(len(best_path) - 1):
        u = best_path[i]
        v = best_path[i + 1]
        f[u][v] -= min_flow
        f[v][u] += min_flow
    return min_flow


def greedy_compute_max_flow(capacity, s, t, weights):
    f = {}
    for edge in capacity:
        (u, v) = edge
        w = capacity[edge]
        if v in f:
            f[v][u] = 0
        else:
            f[v] = {u: 0}
        if u in f:
            f[u][v] = w
        else:
            f[u] = {v: w}
    tot_flow = 0
    while True:
        paths = find_paths(f, s, t)
        if len(paths) == 0: break
        tot_flow += greedy_augment(f, paths, s, t, weights)

    for edge in capacity:
        (u, v) = edge
        capacity[edge] -= f[u][v]

    cut_set = get_cut_set(f, s)
    return tot_flow, capacity, cut_set


def greedy_matching(weights):
    m = len(weights)
    n = len(weights[0])
    capacity = {}
    edges = set()
    s = 0
    t = m + n + 1
    for i in range(m):
        capacity[(s, i + 1)] = 1
        # capacity[(i + 1, s)] = 0
    for j in range(n):
        capacity[(j + m + 1, t)] = 1
        # capacity[(t, j + m + 1)] = 0
    for i in range(m):
        for j in range(n):
            if weights[i][j] != 0:
                capacity[(i + 1, j + m + 1)] = 1
                # capacity[(j + m + 1, i + 1)] = 0
                edges.add((i, j))
    greedy_compute_max_flow(capacity, s, t, weights)
    print(capacity)
    ans = [-1] * m
    for (i, j) in edges:
        if capacity.get((i + 1, j + m + 1), -1) == 1:
            ans[i] = j
    return ans


# m, n = 5, 4
# weights = [[0] * n for _ in range(m)]
# pairs = [(0, 0), (0, 1), (1, 2), (1, 3), (2, 2)]
# for i,(u, v) in enumerate(pairs):
#     weights[u][v] = i+1
# for row in weights:
#     print(row)

# weights = [
#     [10, 4, 5],
#     [6, 8, 3],
#     [5, 4, 0]
# ]
#
# ans = greedy_matching(weights)
# print(ans)
