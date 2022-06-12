xs = [30, 35, 15, 5, 10, 20]
ys = [35, 15, 5, 10, 20, 25]

memo = [[None] * (len(xs) + 1) for _ in range(len(xs) + 1)]
s = [[None] * (len(xs) + 1) for _ in range(len(xs) + 1)]


def dp(l: int, r: int, xs: list, ys: list) -> int:
    if memo[l][r] is not None: return memo[l][r]
    if r - l == 1: return 0
    best = 2 << 30
    for i in range(l + 1, r):
        curr = dp(l, i, xs, ys) + dp(i, r, xs, ys) + xs[l] * xs[i] * ys[r - 1]
        if curr < best:
            best = curr
            s[l][r] = i
    memo[l][r] = best
    return best


def printer(l: int, r: int):
    if r-l==1:
        print(str(xs[l])+" " + str(ys[l]))
    else:
        print("(")
        printer(l, s[l][r])
        printer(s[l][r], r)
        print(")")


# def bottom_up(xs: list, ys: list) -> int:
#     n = len(xs)
#     memo = [[None] * n for _ in range(n)]
#     for i in range(n):
#         memo[0][i] = 0
#     for i in range(1, n):
#         for j in range(n - i):
#             memo[i][j] = min(
#                 memo[i - 1][j] + xs[j] * xs[i + j] * ys[i + j],
#                 memo[i - 1][j + 1] + xs[i] * ys[i] * ys[i + j]
#             )
#     print(memo)
#     return memo[5][0]
#
#
# bottom_up(xs, ys)

print(dp(0, len(xs), xs, ys))
print(s)
printer(0,6)
