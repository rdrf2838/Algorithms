args = []


def sel_sort(x):
    for i in range(len(x) - 1):
        min_val = x[i]
        min_idx = i
        for j in range(i + 1, len(x)):
            if x[j] < min_val:
                min_idx = j
                min_val = x[j]
        x[i], x[min_idx] = x[min_idx], x[i]
    return x


def ins_sort(x):
    for i in range(1, len(x)):
        j = i - 1
        v = x[i]
        while (j >= 0):
            if (v < x[j]):
                x[j + 1] = x[j]
                j -= 1
            else:
                break
        x[j + 1] = v
    return x


def bin_search(v, x, l, r):
    # trying out different indexing method
    # this bin_search is not stable!
    if l == r: return l
    i = (r + l) // 2
    if v == x[i]:
        return i
    elif v < x[i]:
        return bin_search(v, x, l, i)
    else:
        return bin_search(v, x, i + 1, r)


def bin_ins_sort(x):
    for i in range(1, len(x)):
        idx = bin_search(x[i], x, 0, i)
        v = x[i]
        for j in range(i, idx, -1):
            x[j] = x[j - 1]
        x[idx] = v
    return x


def merge_sort(a):
    if len(a) < 2:
        return a
    h = len(a) // 2
    a1 = merge_sort(a[:h])
    a2 = merge_sort(a[h:])
    a3 = [None] * len(a)
    i1 = 0
    i2 = 0
    i3 = 0

    while i1 < len(a1) or i2 < len(a2):
        if i1 >= len(a1):
            a3[i3] = a2[i2]
            i2 += 1
        elif i2 >= len(a2):
            a3[i3] = a1[i1]
            i1 += 1
        else:
            if a1[i1] < a2[i2]:
                a3[i3] = a1[i1]
                i1 += 1
            else:
                a3[i3] = a2[i2]
                i2 += 1
        i3 = i3 + 1
    return a3


def partition(x: list, l: int, r: int) -> int:
    p: int = r - 1
    l_idx: int = l
    r_idx: int = r - 2
    while r_idx >= l_idx:
        if x[l_idx] >= x[p]:
            l_idx += 1
        elif x[r_idx] <= x[p]:
            r_idx -= 1
        else:
            x[l_idx], x[r_idx] = x[r_idx], x[l_idx]
    x[l_idx], x[p] = x[p], x[l_idx]
    return l_idx


def quicksort(x: list, l: int, r: int) -> None:
    if r - l <= 1: return
    p: int = partition(x, l, r)
    quicksort(x, l, p)
    quicksort(x, p + 1, r)


def run():
    print(args)
    quicksort(args, 0, len(args))
    print(args)
    # print(ins_sort(args))
    # print(bin_search(9, args, 0, len(ins_sort(args))))
    # print(push(sorted, 8))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # args = list(map(int, input().split(' ')))
    args = [5, 6, 3, 2, 8, 9, 1, 4, 6]
    # args = [8, 6]
    run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
