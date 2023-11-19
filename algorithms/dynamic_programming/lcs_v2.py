import string

n: int = 20
memo = [[None] * n for _ in range(n)]


def lcs(s1: string, s2: string) -> int:
    l1 = len(s1)
    l2 = len(s2)
    if memo[l1][l2] is not None: return memo[l1][l2]
    if l1 == 0 or l2 == 0: return 0
    if s1[0] == s2[0]:
        memo[l1][l2] = 1 + lcs(s1[1:], s2[1:])
    else:
        memo[l1][l2] = max(lcs(s1, s2[1:]), lcs(s1[1:], s2))
    return memo[l1][l2]


s1 = 'amputation'
s2 = 'sprain'
ans = lcs(s1, s2)
print(ans)
for m in memo:
    print(m)


def print_ans(i: int, j: int) -> None:
    if memo[i][j] is None:
        return
    if memo[i][j - 1] is not None:
        if memo[i][j] == memo[i][j - 1] + 1:
            print(s2[-j])
        print_ans(i, j - 1)
    elif memo[i - 1][j] is not None:
        if memo[i][j] == memo[i - 1][j] + 1:
            print(s1[-i])
        print_ans(i - 1, j)
    else:
        print(s2[-j])


print_ans(len(s1), len(s2))
