t_start = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
t_end = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]


def greedy(s: list, t: list) -> list:
    curr_end: int = 0
    ans: list = []
    for i in range(len(s)):
        if s[i] >= curr_end:
            ans.append(i)
            curr_end = t[i]
    return ans


ans = greedy(t_start, t_end)
print(ans)
