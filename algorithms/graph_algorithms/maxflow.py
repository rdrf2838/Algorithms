import math


# import csv
# with open('flownetwork_02.csv') as f:
#     rows = [row for row in csv.reader(f)][1:]
# capacity = {(u, v): int(c) for u, v, c in rows}

def get_cut_set(f, s):
    q = [s]
    vis = set()
    while len(q) != 0:
        u = q.pop(0)
        vis.add(u)
        for v in f[u]:
            if f[u][v] == 0 or v in vis: continue
            q.append(v)
    return vis


def find_path(f, s, t):
    q = [s]
    p = {s: -1}
    vis = set()
    while len(q) != 0:
        u = q.pop(0)
        vis.add(u)
        for v in f[u]:
            if f[u][v] == 0 or v in vis: continue
            p[v] = u
            if v == t:
                return p
            q.append(v)
    return None


def augment(f, p, s, t):
    v = t
    min_flow = math.inf
    while p[v] != -1:
        u = p[v]
        min_flow = min(min_flow, f[u][v])
        v = u
    v = t
    while p[v] != -1:
        u = p[v]
        f[u][v] -= min_flow
        f[v][u] += min_flow
        v = u
    return min_flow


def compute_max_flow(capacity, s, t):
    f = {}
    for (u, v) in capacity:
        if u in f:
            f[u][v] = 0
        else:
            f[u] = {v: 0}
        if v in f:
            f[v][u] = 0
        else:
            f[v] = {u: 0}
    for edge in capacity:
        (u, v) = edge
        w = capacity[edge]
        f[u][v] = w

    tot_flow = 0
    while True:
        p = find_path(f, s, t)
        if p is None: break
        tot_flow += augment(f, p, s, t)

    for edge in capacity:
        (u, v) = edge
        if f[u][v] > capacity[edge]:
            capacity[edge] = 0
        else:
            capacity[edge] -= f[u][v]

    cut_set = get_cut_set(f, s)
    return tot_flow, capacity, cut_set


# capacity = {('0', '1'): 46, ('0', '2'): 73, ('0', '3'): 33, ('0', '4'): 20, ('1', '2'): 35, ('1', '3'): 15,
#             ('1', '4'): 86, ('2', '1'): 51, ('2', '3'): 93, ('2', '4'): 35, ('3', '1'): 100, ('3', '2'): 91,
#             ('3', '4'): 11}
# v, flows, cut_set = compute_max_flow(capacity, '0', '4')
# print(flows)
