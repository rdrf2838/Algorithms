import random

BLACK = 0
RED = 1


class Node:
    def __init__(self, k=None, p=None, l=None, r=None, c=None):
        self.k = k
        self.p = p
        self.l = l
        self.r = r
        self.c = c

    def to_str(self):
        COL = "BLACK" if self.c == 0 else "RED"
        return f"Node(k: {self.k}, c: {COL}, p: {self.p}, l: {self.l}, r: {self.r})"

    def __str__(self):
        COL = "BLACK" if self.c == 0 else "RED"
        return f"Node({self.k}, c: {COL}, {str(self.l)}, {str(self.r)})"


class RedBlackTree:

    def __init__(self):
        self.NIL = Node(c=BLACK)
        self.head = self.NIL

    def left_rotate(self, x: Node):
        assert x.r is not self.NIL  # cannot rotate about nothing
        y = x.r
        self.rb_transplant(x, y)
        x.r = y.l
        if y.l is not self.NIL:
            y.l.p = x
        y.l = x
        x.p = y

    def right_rotate(self, x: Node):
        assert x.l is not self.NIL
        y = x.l
        self.rb_transplant(x, y)
        x.l = y.r
        if y.r is not self.NIL:
            y.r.p = x
        y.r = x
        x.p = y

    def insert(self, x: Node):
        prev = self.NIL
        curr = self.head

        while curr is not self.NIL:
            prev = curr
            if x.k < curr.k:
                curr = curr.l
            else:
                curr = curr.r

        x.p = prev
        if prev is self.NIL:
            self.head = x
        elif x.k < prev.k:
            prev.l = x
        else:
            prev.r = x

        x.l = self.NIL
        x.r = self.NIL
        x.c = RED
        self.rb_insert_fixup(x)

    def rb_insert_fixup(self, x: Node):
        while x.p.c == RED:
            if x.p.p.l == x.p:
                y = x.p.p.r
                if y.c == RED:
                    x.p.c = BLACK
                    y.c = BLACK
                    x.p.p.c = RED
                    x = x.p.p
                else:
                    if x == x.p.r:
                        x = x.p
                        self.left_rotate(x)
                    x.p.c = BLACK
                    x.p.p.c = RED
                    self.right_rotate(x.p.p)
            else:
                y = x.p.p.l
                if y.c == RED:
                    x.p.c = BLACK
                    y.c = BLACK
                    x.p.p.c = RED
                    x = x.p.p
                else:
                    if x == x.p.l:
                        x = x.p
                        self.right_rotate(x)
                    x.p.c = BLACK
                    x.p.p.c = RED
                    self.left_rotate(x.p.p)

        self.head.c = BLACK

    def rb_transplant(self, u: Node, v: Node):
        assert u is not self.NIL
        if u.p is self.NIL:
            self.head = v
        elif u.p.l == u:
            u.p.l = v
        else:
            u.p.r = v
        v.p = u.p

    def rb_delete(self, z: Node):
        y = z
        y_org_c = y.c


    # def delete(self, x: Node):
    #     assert x is not self.NIL
    #     # case 1: x has 0 or 1 child
    #     if x.l is self.NIL:
    #         self.rb_transplant(x, x.r)
    #
    #     elif x.r is self.NIL:
    #         self.rb_transplant(x, x.l)
    #
    #     else:
    #         succ = self.succ(x)
    #         # case 2: succ is x's right child
    #         if x.r == succ:
    #             self.rb_transplant(x, succ)
    #             succ.l = x.l
    #             succ.l.p = succ
    #
    #         # case 3: succ is not x's right child
    #         else:
    #             if succ.r is not self.NIL:
    #                 self.rb_transplant(succ, succ.r)
    #             else:
    #                 succ.p.l = self.NIL
    #             succ.r = x.r
    #             x.r.p = succ
    #             self.rb_transplant(x, succ)
    #             succ.l = x.l
    #             x.l.p = succ

    def get_min(self):
        prev = self.NIL
        curr = self.head
        while curr is not self.NIL:
            prev = curr
            curr = curr.l

        assert prev is not self.NIL
        return prev.k

    def get_max(self):
        prev = self.NIL
        curr = self.head
        while curr is not self.NIL:
            prev = curr
            curr = curr.r

        assert prev is not self.NIL
        return prev.k

    def search(self, key):
        curr = self.head
        while curr is not self.NIL:
            if curr.k == key:
                return True
            elif key < curr.k:
                curr = curr.l
            else:
                curr = curr.r
        return False

    def get(self, key):
        curr = self.head
        while curr is not self.NIL:
            if curr.k == key:
                return curr
            elif key < curr.k:
                curr = curr.l
            else:
                curr = curr.r
        return self.NIL

    def succ(self, x: Node) -> Node:
        if x.r is not self.NIL:
            par = self.NIL
            curr = x.r
            while curr is not self.NIL:
                par = curr
                curr = curr.l
            return par
        else:
            curr = x
            while curr.p is not self.NIL:
                if curr == curr.p.l:
                    return curr.p
                else:
                    curr = curr.p
            return self.NIL

    def pred(self, x: Node) -> Node:
        if x.l is not self.NIL:
            par = x
            curr = x.l
            while curr is not self.NIL:
                par = curr
                curr = curr.r
            return par
        else:
            curr = x
            par = x.p
            while par is not self.NIL:
                if par.r == curr:
                    return par
                else:
                    curr = par
                    par = par.p
            return self.NIL

        # if x has a right child, go right then left
        # else if x does not have a right child, go left up until right up

    def height(self):
        return self._height(self.head)

    def _height(self, x: Node):
        if x == self.NIL:
            return 0
        return 1 + max(self._height(x.l), self._height(x.r))

    def size(self):
        ctr = 0
        stack = [self.head]
        while len(stack) != 0:
            top = stack.pop()
            if top is self.NIL: continue
            ctr += 1
            stack.append(top.l)
            stack.append(top.r)
        return ctr

    def __str__(self):
        return str(self.head)


rbt = RedBlackTree()

nodes = [Node(k=random.randint(0, 10)) for v in range(10000)]

for node in nodes:
    rbt.insert(node)

# print(rbt)
print(rbt.height())
