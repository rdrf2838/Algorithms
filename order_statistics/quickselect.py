import random
import math


def random_partition(arr: list, l: int, r: int):
    p: int = random.randrange(l, r)  # random from l to r - 1
    arr[p], arr[r - 1] = arr[r - 1], arr[p]
    p, r = r - 1, r - 2
    while r + 1 != l:
        if arr[l] <= arr[p]:
            l += 1
        elif arr[r] >= arr[p]:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
    arr[l], arr[p] = arr[p], arr[l]
    return l


def quick_select(arr: list, i: int, l: int, r: int):
    if r - l == 1: return arr[l]
    p = random_partition(arr, l, r)
    if p == i:
        return arr[i]
    elif p > i:
        return quick_select(arr, i, l, p)
    else:
        return quick_select(arr, i, p + 1, r)


def k_smallest(arr: list, k: int, l: int, r: int):
    if r - l == k:
        return arr[l:r]
    p = random_partition(arr, l, r)
    if p - l == k:
        return arr[l:p]
    elif p - l > k:
        return k_smallest(arr, k, l, p)
    else:
        return arr[l:p + 1] + k_smallest(arr, k - (p + 1 - l), p + 1, r)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def natural_selection(arr: list):
    n: int = 2 ** (2 + int(math.log(len(arr) - 1, 2))) - 1
    arena = [-math.inf] * n
    i = n // 2
    while len(arr) > 0:
        top = arr.pop()
        arena[i] = top
        i += 2
        if i >= n:
            i = n // 2 + 1

    i = n - 1
    j = i - 1
    while j >= 0:
        arena[parent(i)] = max(arena[i], arena[j])
        i -= 2
        j -= 2
    best = arena[0]
    snd_best = -math.inf
    i = 0
    while i < n // 2:
        j = left(i)
        k = right(i)
        if arena[i] == arena[j]:
            i = j
            snd_best = max(snd_best, arena[k])
        else:
            i = k
            snd_best = max(snd_best, arena[j])
    return best, snd_best


x = [1, 7, 6, 5, 4, 8, 9, 2, 3, 0]
# x = [1, 7, 6, 5, 4, 8, 9, 2]
# print(x)
# print(quick_select(x, 9, 0, len(x)))
# print(k_smallest(x, 7, 0, len(x)))

print(natural_selection(x))
