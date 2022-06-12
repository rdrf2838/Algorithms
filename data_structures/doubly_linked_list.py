class Node:
    def __init__(self,
                 value=None,
                 left=None,
                 right=None
                 ):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node(value: {self.value})"


class DoubleLinkList:
    def __init__(self):
        self.NIL = Node(value='NIL')
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.head = self.NIL

    def insert(self, value):
        u = Node(value=value)
        u.right = self.head
        u.left = self.NIL
        last = self.head.left
        last.right = u
        self.head.left = u
        self.head = u

    def get_n(self, n):
        """
        Gets the first min(n, remaining item count) in the list
        :param n:
        :return: list of Nodes
        """
        if self.head == self.NIL: return []
        ans = []
        curr = self.head
        for _ in range(n):
            ans.append(curr)
            if curr.right != self.NIL:
                curr = curr.right
            else:
                break
        return ans

    def delete(self, u: Node):
        if self.head == u:
            self.head = u.right
        l = u.left
        r = u.right
        l.right = r
        r.left = l

    def __str__(self):
        ans = ''
        curr = self.head
        while curr != self.NIL:
            ans += str(curr)
            curr = curr.right
        return ans

# dll = DoubleLinkList()
# for i in range(50):
#     dll.insert(i)
# temp = dll.get_n(49)
#
# print(dll)
# for v in temp:
#     dll.delete(v)
# print(dll)