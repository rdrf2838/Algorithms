# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, S):
    memo = [0] * len(A)
    memo[0] = A[0] - S
    d = dict()
    for i in range(len(A)):
        A[i] -= S
        if i != 0:
            memo[i] = memo[i - 1] + A[i]
        d[memo[i]] = d.get(memo[i], 0) + 1
    ans = 0
    for k, v in d.items():
        if k == 0:
            v += 1
        if v > 1:
            ans += (v * (v - 1)) // 2
            if ans > 1000000000:
                return 1000000000
    return ans

# a = solution([2,1,3], 2)
# print(a)