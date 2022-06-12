import math

# graph = {
#     0: {(1, 10), (2, 5)},
#     1: {(3, 1), (2, 2)},
#     2: {(1, 3), (4, 2)},
#     3: {(4, 4)},
#     4: {(3, 6), (0, 7)}
# }
graph = {
    0: {(1, 1)},
    1: {(2, 2)},
    2: {(3, 3)},
    3: {(1, -6)}
}

dist = [math.inf] * len(graph)
s = 0
dist[s] = 0

for _ in range(len(graph) - 1):
    for u in graph:
        for (v, w) in graph[u]:
            dist[v] = min(dist[v], dist[u] + w)

for u in graph:
    for (v, w) in graph[u]:
        if dist[v] > dist[u] + w:
            raise Exception("-ve cycle detected")