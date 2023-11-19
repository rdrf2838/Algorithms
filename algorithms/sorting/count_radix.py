args = [5, 6, 3, 2, 8, 9, 1, 4, 6]
k = 10


def count_sort(x: list, base: int) -> None:
    ct: list = [0] * base
    for v in x:
        ct[v] += 1
    ct[0] -= 1
    for i in range(1, base):
        ct[i] = ct[i - 1] + ct[i]
    x2: list = [None] * len(x)
    for v in x:
        x2[ct[v]] = v
        ct[v] -= 1
    for i, v in enumerate(x2): x[i] = v


# indexing from 0
def nth(v: int, idx: int, base: int) -> int:
    return int((v % base ** (1 + idx)) // (base ** (idx)))


def digit_len(v: int, base: int) -> int:
    ctr = 0
    while v > 0:
        v = v // base
        ctr += 1
    return ctr


def augmented_count_sort(x: list, idx: int, base: int) -> None:
    count: list = [0] * base
    for v in x:
        count[nth(v, idx, base)] += 1
    count[0] -= 1
    for i in range(1, base):
        count[i] += count[i - 1]
    x2 = [None] * len(x)
    for v in x:
        x2[count[nth(v, idx, base)]] = v
        count[nth(v, idx, base)] -= 1
    for i, v in enumerate(x2):
        x[i] = v


def radix_sort(x: list, base: int) -> None:
    l: int = digit_len(max(x), base)
    for i in range(l):
        augmented_count_sort(x, i, base)


args = [123, 678, 456, 0, 234, 890]
radix_sort(args, 10)
