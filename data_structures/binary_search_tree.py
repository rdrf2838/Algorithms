class Node:
    def __init__(self, k=None, p=None, l=None, r=None):
        self.k = k
        self.p = p
        self.l = l
        self.r = r

    def __str__(self):
        return f"Node({self.k}, {str(self.l)}, {str(self.r)})"


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, x: Node):
        prev = None
        curr = self.head

        while curr is not None:
            prev = curr
            if x.k < curr.k:
                curr = curr.l
            else:
                curr = curr.r

        x.p = prev
        if prev is None:
            self.head = x
        elif x.k < prev.k:
            prev.l = x
        else:
            prev.r = x

    def transplant(self, u: Node, v: Node):
        assert u is not None
        if u.p is None:
            self.head = v
        elif u.p.l == u:
            u.p.l = v
        else:
            u.p.r = v
        if v is not None:
            v.p = u.p

    def left_rotate(self, x: Node):
        a = x.r
        b = a.l if a is not None else None
        if a is not None:
            self.transplant(a, b)
        self.transplant(x, a)
        a.l = x
        x.p = a

    def right_rotate(self, x: Node):
        a = x.l
        b = a.r if a is not None else None
        if a is not None:
            self.transplant(a, b)
        self.transplant(x, a)
        a.r = x
        x.p = a

    def delete(self, x: Node):
        assert x is not None
        # case 1: x has 0 or 1 child
        if x.l is None:
            self.transplant(x, x.r)

        elif x.r is None:
            self.transplant(x, x.l)

        else:
            succ = self.succ(x)
            # case 2: succ is x's right child
            if x.r == succ:
                self.transplant(x, succ)
                succ.l = x.l
                succ.l.p = succ

            # case 3: succ is not x's right child
            else:
                if succ.r is not None:
                    self.transplant(succ, succ.r)
                else:
                    succ.p.l = None
                succ.r = x.r
                x.r.p = succ
                self.transplant(x, succ)
                succ.l = x.l
                x.l.p = succ

    def get_min(self):
        prev = None
        curr = self.head
        while curr is not None:
            prev = curr
            curr = curr.l

        assert prev is not None
        return prev.k

    def get_max(self):
        prev = None
        curr = self.head
        while curr is not None:
            prev = curr
            curr = curr.r

        assert prev is not None
        return prev.k

    def search(self, key):
        curr = self.head
        while curr is not None:
            if curr.k == key:
                return True
            elif key < curr.k:
                curr = curr.l
            else:
                curr = curr.r
        return False

    def get(self, key):
        curr = self.head
        while curr is not None:
            if curr.k == key:
                return curr
            elif key < curr.k:
                curr = curr.l
            else:
                curr = curr.r
        return None

    def succ(self, x: Node) -> Node:
        if x.r is not None:
            par = None
            curr = x.r
            while curr is not None:
                par = curr
                curr = curr.l
            return par
        else:
            curr = x
            while curr.p is not None:
                if curr == curr.p.l:
                    return curr.p
                else:
                    curr = curr.p
            return None

    def pred(self, x: Node) -> Node:
        if x.l is not None:
            par = x
            curr = x.l
            while curr is not None:
                par = curr
                curr = curr.r
            return par
        else:
            curr = x
            par = x.p
            while par is not None:
                if par.r == curr:
                    return par
                else:
                    curr = par
                    par = par.p
            return None

    # if x has a right child, go right then left
    # else if x does not have a right child, go left up until right up

    def size(self):
        ctr = 0
        stack = [self.head]
        while len(stack) != 0:
            top = stack.pop()
            if top is None: continue
            ctr += 1
            stack.append(top.l)
            stack.append(top.r)
        return ctr

    def __str__(self):
        return str(self.head)


bst = BinarySearchTree()
for i in [3, 7, 6, 5, 8]:
    bst.insert(Node(k=i))
print(bst)
h = bst.head


# bst.right_rotate(h.r)
# print(bst)

def select(x, i):
    def find(x, i):
        j = 0

        def dfs(y):
            nonlocal j
            if y is None: return None
            tmp = dfs(y.r)
            if tmp is not None: return tmp
            j += 1
            if j == i:
                return y
            tmp = dfs(y.l)
            if tmp is not None: return tmp

        return dfs(x)

    u = find(x, i)
    while u.p is not None:
        if u.p.r == u:
            bst.left_rotate(u.p)
        else:
            bst.right_rotate(u.p)
    return u


print(select(h, 3))

# bst = BinarySearchTree()
# nodelist = []
# for i in range(1000):
#     x = Node(k=random.randint(0, 100))
#     nodelist.append(x)
#     bst.insert(x)
# print(bst)
# prev = bst.size()
# for x in nodelist:
#     # print("deleting: " + str(x))
#     bst.delete(x)
#     # print(bst)
#     assert bst.size() == prev - 1
#     prev = bst.size()
