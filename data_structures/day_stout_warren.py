import math


class Node:
    def __init__(self, k=None, p=None, l=None, r=None):
        self.k = k
        self.p = p
        self.l = l
        self.r = r

    def to_str(self):
        return f"Node(k: {self.k}, p: {self.p}, l: {self.l}, r: {self.r})"

    def __str__(self):
        return f"Node({self.k}, {str(self.l)}, {str(self.r)})"


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def balance(self):
        u = self.head

        # converts binary search tree into a vine
        while True:
            while u.l is not None:
                self.right_rotate(u)
                u = u.p
            if u.r is None:
                break
            u = u.r

        # calculate number of leaf nodes
        ct = 0
        u = self.head
        while u is not None:
            ct += 1
            u = u.r
        leaves: int = ct + 1 - 2 ** int(math.log(ct + 1, 2))

        # rotate the leaf nodes into place
        u = self.head
        for _ in range(leaves):
            self.left_rotate(u)
            u = u.p.r
        ct = ct - leaves
        while ct > 1:
            ct = ct // 2
            u = self.head
            for _ in range(ct):
                self.left_rotate(u)
                # if u.p.r is not None:
                u = u.p.r
                # else:
                #     break

    def left_rotate(self, x: Node):
        assert x.r is not None  # cannot rotate about nothing
        y = x.r
        self.transplant(x, y)
        x.r = y.l
        if y.l is not None:
            y.l.p = x
        y.l = x
        x.p = y

    def right_rotate(self, x: Node):
        assert x.l is not None
        y = x.l
        self.transplant(x, y)
        x.l = y.r
        if y.r is not None:
            y.r.p = x
        y.r = x
        x.p = y

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
nodelist = []
# for i in [4, 3, 2, 6, 1, 5, 8, 9, 7]:
for i in [4, 3, 2, 6, 1, 5, 8, 9, 7, 11, 21, 13, 15, 14]:
    n = Node(k=i)
    nodelist.append(n)
    bst.insert(n)
print(bst)
bst.balance()
print(bst)
