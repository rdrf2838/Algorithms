from functools import total_ordering
from queue import PriorityQueue


@total_ordering
class Node:
    def __init__(self, freq: int, left=None, right=None, c=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.c = c

    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return f"Node({self.c}, {self.freq}, {str(self.left)}, {str(self.right)})"


def huffman(keyvals: dict) -> Node:
    q = PriorityQueue()
    for k in keyvals:
        q.put(Node(c=k, freq=keyvals[k]))
    for i in range(len(keyvals) - 1):
        x, y = q.get(), q.get()
        z = Node(left=x, right=y, freq=(x.freq + y.freq))
        q.put(z)
    return q.get()


keyvals: dict = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
args = []

ans = huffman(keyvals)
print(ans)
