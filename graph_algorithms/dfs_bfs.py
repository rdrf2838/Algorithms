graph = {0: {1, 2, 3}, 1: {2, 3}, 2: {3}, 3: {2}}

vis = [-1] * len(graph)
VISITING = 1
VISITED = 2
UNVISITED = -1

def dfs(u):
    print(f'visiting: {u}')
    vis[u] = 1
    for v in graph[u]:
        if vis[v] != -1: continue
        dfs(v)
    print(f'visited: {u}')


def iterative_dfs(u):
    stack = [u]
    while len(stack) != 0:
        u = stack.pop()
        if vis[u] == VISITED: continue
        elif vis[u] == VISITING:
            print(f'visited: {u}')
            vis[u] = VISITED
            continue

        print(f'visiting: {u}')
        stack.append(u)
        vis[u] = VISITING
        for v in graph[u]:
            # if vis[v] == VISITING: continue
            if vis[v] != UNVISITED: continue
            stack.append(v)

def all_paths(s, t):
    ans = []
    queue = [[s]]
    while len(queue) != 0:
        path = queue.pop(0)
        u = path[-1]
        if u == t:
            ans.append(path)
            continue
        if vis[u] == VISITED: continue
        vis[u] = VISITED
        for v in graph[u]:
            p2 = path[:]
            p2.append(v)
            queue.append(p2)
    return ans

# iterative_dfs(0)
ans = all_paths(0, 3)
print(ans)