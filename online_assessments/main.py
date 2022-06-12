g = {
    0: [1, 5],
    1: [2, 4],
    2: [3],
    3: [4],
    4: [],
    5: [0, 6],
    6: [5],
}
UNVISITED = 0
VISITING = 1
VISITED = 2
vis = [UNVISITED] * len(g)


def dfs(u, p):
    vis[u] = VISITING
    for v in g[u]:
        if v != p:
            if vis[v] == UNVISITED:
                dfs(v, u)
            elif vis[v] == VISITING:
                print(f'back edge {u} -> {v} detected')
            elif vis[v] == VISITED:
                print(f'forward edge {u} -> {v} detected')
    vis[u] = VISITED


dfs(0, -1)
