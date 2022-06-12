import math


class Node:
    def __init__(self, k: int = None, p=None):
        self.k = k
        self.p = p
        self.c = []

    def combine(self, u):
        # preserves order in array (small to big nodes)
        assert len(self.c) == len(u.c)
        if self.k <= u.k:
            self.c.append(u)
            u.p = self
            return self
        else:
            u.c.append(self)
            self.p = u
            return u

    def __str__(self):
        return f"Node({self.k}, {[str(x) for x in self.c]})"


class BinomialHeap:
    def __init__(self, u: Node = None):
        # should have really just used a fake parent node smh
        self.arr = [u]
        self.n = 0 if u is None else 1

    def push(self, u: Node):
        assert len(u.c) == 0  # add only leaf nodes
        self.merge(BinomialHeap(u))

    def decrease_key(self, u: Node, k):
        u.k = k
        curr = u
        par = u.p
        while par is not None:
            if par.k > curr.k:
                curr.k, par.k = par.k, curr.k
                curr = par
                par = curr.p
            else:
                break

    def delete(self, u: Node):
        self.decrease_key(u, -math.inf)
        self.extract_min()

    def extract_min(self):
        smallest = math.inf
        ptr = None
        idx = -1
        for i, u in enumerate(self.arr):
            if u is not None and u.k < smallest:
                smallest = u.k
                ptr = u
                idx = i

        bh = BinomialHeap()
        bh.arr = ptr.c
        self.arr[idx] = None
        self.merge(bh)
        while True:
            if len(self.arr) == 0: break
            if self.arr[-1] is None:
                self.arr = self.arr[:-1]
            else:
                break
        return ptr

    def merge(self, h):
        h1_arr, h2_arr = self.arr, h.arr
        h1_n, h2_n = self.n, h.n
        self.n = h1_n + h2_n
        self.arr = [None] * math.ceil(math.log(self.n + 1, 2))

        h1_n, h2_n = len(h1_arr), len(h2_arr)
        carry = None
        for i in range(len(self.arr)):
            if i >= h1_n and i >= h2_n:
                self.arr[i] = carry
            elif h1_n <= i < h2_n:
                if carry is None:
                    self.arr[i] = h2_arr[i]
                elif h2_arr[i] is None:
                    self.arr[i] = carry
                    carry = None
                else:
                    carry = h2_arr[i].combine(carry)
            elif h1_n > i >= h2_n:
                if carry is None:
                    self.arr[i] = h1_arr[i]
                elif h1_arr[i] is None:
                    self.arr[i] = carry
                    carry = None
                else:
                    carry = h1_arr[i].combine(carry)
            elif h1_arr[i] is None and h2_arr[i] is None:
                self.arr[i] = carry
                carry = None
            elif h1_arr[i] is None and h2_arr[i] is not None:
                if carry is None:
                    self.arr[i] = h2_arr[i]
                else:
                    carry = carry.combine(h2_arr[i])
            elif h1_arr[i] is not None and h2_arr[i] is None:
                if carry is None:
                    self.arr[i] = h1_arr[i]
                else:
                    carry = carry.combine(h1_arr[i])
            else:
                if carry is not None:
                    self.arr[i] = carry
                carry = h1_arr[i].combine(h2_arr[i])

    def __str__(self):
        return f"{[str(x) for x in self.arr]}"


bh = BinomialHeap()
nodes = []
amt = 150
for i in range(amt):
    n = Node(k=i)
    nodes.append(n)
    bh.push(n)
print(bh)
for i in range(amt):
    u = bh.extract_min()
    print(u.k)
print(bh)
