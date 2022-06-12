import math


class Node:
    def __init__(self,
                 key=None,
                 value=None,
                 parent=None,
                 left=None,
                 right=None,
                 children=None,
                 degree=0,
                 mark=False
                 ):
        self.key = key
        self.parent = parent
        self.left = left if left is not None else self
        self.right = right if right is not None else self
        self.children = children
        self.degree = degree
        self.mark = mark

    def __str__(self):
        child_str = ""
        if self.children is not None:
            curr = self.children
            while True:
                child_str += str(curr)
                curr = curr.right
                if curr == self.children:
                    break
        return f"Node({self.key}, {child_str})"


class FibonacciHeap:
    def __init__(self):
        self.n = 0
        self.minimum = None

    def concatenate(self, a, x):
        b = a.left
        y = x.left
        a.left = y
        y.right = a
        b.right = x
        x.left = b

    def remove(self, x):
        l = x.left
        r = x.right
        l.right = r
        r.left = l

    def insert(self, x: Node):
        self.n += 1
        if self.minimum is None:
            self.minimum = x
        else:
            self.concatenate(self.minimum, x)
            if x.key < self.minimum.key:
                self.minimum = x

    def get_min(self):
        return self.minimum

    def linked_list_to_list(self, x):
        nodes = []
        curr = x
        while True:
            y = curr
            curr = curr.right
            y.left = y
            y.right = y
            nodes.append(y)
            if curr == x:
                break
        return nodes

    def extract_min(self):
        z = self.minimum
        assert z is not None
        if z.children is not None:
            nodes = self.linked_list_to_list(z.children)
            for child in nodes:
                self.concatenate(child, z)
                child.parent = None
        self.remove(z)
        if z == z.right:
            self.minimum = None
        else:
            self.minimum = z.right
            self.consolidate()
        return z

    def union(self, h):
        h1_min, h2_min = self.minimum, h.minimum
        h1_n, h2_n = self.n, h.n
        self.concatenate(h1_min, h2_min)
        if h1_min is None or (h2_min is not None and h1_min.key > h2_min.key):
            self.minimum = h2_min
        self.n = h1_n + h2_n

    def link(self, y, x):
        self.remove(y)
        x.degree += 1
        y.mark = False
        y.parent = x
        if x.children is None:
            x.children = y
        else:
            self.concatenate(x.children, y)

    def consolidate(self):
        D = int(math.log(self.n, (1 + 5 ** (1 / 2)) / 2))
        arr = [None] * (D + 1)

        nodes = self.linked_list_to_list(self.minimum)
        for x in nodes:
            d = x.degree
            while arr[d] is not None:
                y = arr[d]
                if x.key > y.key:
                    x, y = y, x
                self.link(y, x)
                arr[d] = None
                d += 1
            arr[d] = x
        self.minimum = None
        for i in range(D):
            if arr[i] is not None:
                if self.minimum is None:
                    self.minimum = arr[i]
                else:
                    self.concatenate(self.minimum, arr[i])
                    if arr[i].key < self.minimum.key:
                        self.minimum = arr[i]

    def cut(self, x, y):
        self.remove(x)
        y.degree -= 1
        self.concatenate(x, self.minimum)
        x.parent = None
        x.mark = False

    def cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def decrease_key(self, x, k):
        assert x.key >= k
        x.key = k
        y = x.parent
        if y is not None and y.key > x.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.key < self.minimum.key:
            self.minimum = x

    def delete(self, x):
        self.decrease_key(x, -math.inf)
        self.extract_min()

    def __str__(self):
        return str(Node(key="Fib_Heap", children=self.minimum))


fh = FibonacciHeap()
sz = 30
nodes = []
for i in range(sz):
    n = Node(key=i)
    nodes.append(n)
    fh.insert(n)

for n in nodes:
    fh.delete(n)
