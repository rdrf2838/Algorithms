import string

n = 20
memo = [[None] * n for _ in range(n)]


def dp(s1: string, s2: string) -> (int, string):
    if memo[len(s1)][len(s2)] is not None: return memo[len(s1)][len(s2)]
    if len(s1) == 0 or len(s2) == 0: return 0, ""
    if s1[0] == s2[0]:
        v, a = dp(s1[1:], s2[1:])
        memo[len(s1)][len(s2)] = v + 1, s1[0] + a
        return memo[len(s1)][len(s2)]
    memo[len(s1)][len(s2)] = max(dp(s1, s2[1:]), dp(s1[1:], s2))
    return memo[len(s1)][len(s2)]


ans = dp("amputation", "sprain")
for v in memo:
    print(v)
memo[10][6] = (0, "hi")
for v in memo:
    print(v)
