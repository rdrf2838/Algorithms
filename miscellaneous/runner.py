import math
import random


def insert_sort(xs):
    for i in range(1, len(xs)):
        while i >= 1 and xs[i] < xs[i-1]:
            xs[i], xs[i-1] = xs[i-1], xs[i]
            i -= 1


def select_sort(xs):
    for i in range(len(xs)-1):
        low_idx = i
        for j in range(i+1, len(xs)):
            if xs[j] < xs[low_idx]:
                low_idx = j
        xs[i], xs[low_idx] = xs[low_idx], xs[i]


def binary_search(xs, v):
    xs2 = [-math.inf] + xs + [math.inf]
    l = 0
    r = len(xs2) - 1
    while r - l > 1:
        m = (l+r)//2
        if xs2[m] > v:
            r = m
        else:
            l = m
    res = l if xs2[l] == v else r
    return res - 1


def merge_sort(xs):
    n = math.ceil(math.log2(len(xs)))
    tot_num = 2**n
    xs2 = xs + (tot_num - len(xs)) * [math.inf]
    for i in range(1, n+1):
        width = 2**i
        for j in range(0, tot_num, width):
            l_idx = j
            l_end = j + width//2
            r_idx = l_end
            r_end = j + width
            tmp = [None] * width
            tmp_idx = 0
            while l_idx < l_end or r_idx < r_end:
                if l_idx < l_end and r_idx < r_end:
                    l_val = xs2[l_idx]
                    r_val = xs2[r_idx]
                    if l_val < r_val:
                        tmp[tmp_idx] = l_val
                        l_idx += 1
                    else:
                        tmp[tmp_idx] = r_val
                        r_idx += 1
                elif l_idx < l_end:
                    tmp[tmp_idx] = xs2[l_idx]
                    l_idx += 1
                elif r_idx < r_end:
                    tmp[tmp_idx] = xs2[r_idx]
                    r_idx += 1
                tmp_idx += 1
            xs2[j:j+width] = tmp
    xs[:] = xs2[:len(xs)]


def parent(n):
    return (n-1)//2


def left(n):
    return 2*n+1


def right(n):
    return 2*n+2


def heapify(xs, end, i):
    l_val, r_val = map(lambda c: xs[c(i)] if c(
        i) < end else -math.inf, [left, right])
    j = left(i) if l_val > r_val else right(i)
    j_val = max(l_val, r_val)
    if j_val > xs[i]:
        xs[j], xs[i] = xs[i], xs[j]
        heapify(xs, end, j)


def heap_sort(xs):
    n = len(xs)
    num_leaves = (n+1)//2
    for i in reversed(range(n-num_leaves)):
        heapify(xs, n, i)

    for i in reversed(range(1, n)):
        xs[0], xs[i] = xs[i], xs[0]
        heapify(xs, i, 0)


def counting_sort(xs):
    lo, hi = min(xs), max(xs)
    cs = [0] * (hi-lo+1)
    for v in xs:
        cs[v-lo] += 1
    for i in range(1, len(cs)):
        cs[i] += cs[i-1]
    xs2 = [None] * len(xs)
    for v in reversed(xs):
        cs[v-lo] -= 1
        xs2[cs[v-lo]] = v
    xs[:] = xs2


box = 0, 100
t = [random.randint(*box) for _ in range(*box)]
# insert_sort(t)
# select_sort(t)
# merge_sort(t)
# heap_sort(t)
counting_sort(t)
print(t)
# print(t)
# for i in range(10):
#     ans = binary_search(t, i)
#     print((i, ans))
