import math


def dist(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def brute(p: list) -> float:
    n: int = len(p)
    best: float = math.inf
    for i in range(n - 1):
        for j in range(i + 1, n):
            best = min(best, dist(p[i], p[j]))
    return best


def closest(px: list, py: list) -> float:
    n: int = len(px)

    if n <= 3:
        return brute(px)

    mid: int = n // 2
    px_left = px[:mid]
    px_right = px[mid:]

    mid_x, mid_y = px[mid]
    py_left = []
    py_right = []
    for (x, y) in py:
        if x <= mid_x:
            py_left.append((x, y))
        else:
            py_right.append((x, y))

    closest_left: float = closest(px_left, py_left)
    closest_right: float = closest(px_right, py_right)
    closest_best = min(closest_right, closest_left)

    centre: list = []
    for (x, y) in py:
        if abs(x - mid_x) < closest_best:
            centre.append((x, y))

    for i in range(len(centre)-7):
        for j in range(i+1, i+7):
            closest_best = min(closest_best, dist(centre[i], centre[j]))
    return closest_best

xs = [(1,1), (3,3), (4,5), (6, 7)]
ys = [(1,1), (3,3), (4,5), (6, 7)]
print(closest(xs, ys))