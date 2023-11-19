def ins_sort(xs: list) -> None:
    for i in range(1, len(xs)):
        v = xs[i]
        j: int = i - 1
        while j >= 0:
            if xs[j] > v:
                xs[j + 1] = xs[j]
                j -= 1
            else:
                break
        xs[j + 1] = v


# implementation for v in [0 to 0.9999999999]
def bucket_sort(xs: list, n: int) -> None:
    buckets = [[] for _ in range(n)]
    for v in xs:
        v2 = int(v * n)
        buckets[v2].append(v)
    print(buckets)
    ans = []
    for vs in buckets:
        ins_sort(vs)
        ans = ans + vs
    for i, v in enumerate(ans):
        xs[i] = v


args = [4, 5, 3, 2, 6, 7]
ins_sort(args)
args = [0.45, 0.76, 0.32, 0.11, 0.69, 0.45]
bucket_sort(args, 2)
print(args)