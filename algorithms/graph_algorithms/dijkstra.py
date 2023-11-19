import math
from queue import PriorityQueue

graph = {
    0: {(1, 10), (2, 5)},
    1: {(3, 1), (2, 2)},
    2: {(1, 3), (4, 2)},
    3: {(4, 4)},
    4: {(3, 6), (0, 7)}
}

dist = [math.inf] * len(graph)
s = 0
dist[s] = 0
pq = PriorityQueue()
pq.put((dist[s], s))
while not pq.empty():
    d, u = pq.get()
    if d > dist[u]: continue
    for (v, w) in graph[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            pq.put((dist[v], v))

print(dist)