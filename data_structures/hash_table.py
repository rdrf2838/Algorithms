OCCUPIED = 1
UNOCCUPIED = 0


class Node:
    def __init__(self,
                 key=None,
                 value=None,
                 left=None,
                 right=None,
                 flag=UNOCCUPIED
                 ):
        self.left = left
        self.right = right
        self.key = key
        self.value = value
        self.flag = flag


class HashTable:
    def __init__(self,
                 h,
                 n=20,
                 ):
        self.h = h
        self.arr = [Node() for _ in range(n)]
        for i in range(n - 1):
            u = self.arr[i]
            v = self.arr[i + 1]
            u.right = v
            v.left = u
        self.empty_slots = self.arr[0]

    # def extract_slot(self, u):

    def extract_empty_slot(self):
        assert self.empty_slots is not None
        u = self.empty_slots
        self.empty_slots = u.right
        u.left = None
        u.right = None
        self.empty_slots.left = None
        return u

    def insert(self, k, val):
        i = self.h(k)
        u = self.arr[i]
        if u.value is None:
            u.key = k
            u.value = val
            u.flag = OCCUPIED
            l = u.left
            r = u.right
            if l is not None:
                l.right = r
            if r is not None:
                r.left = l
            if self.empty_slots == u:
                self.empty_slots = r
        elif u.flag == OCCUPIED:
            if u.key == k:
                u.value = val
                return
            v = self.extract_empty_slot()
            v.value = u.value
            if u.right is not None:
                u.right.left = v
            u.value = val
            u.key = k
            u.right = v
            v.left = u
        elif u.flag == UNOCCUPIED:
            v = self.extract_empty_slot()
            v.value = u.value
            l = u.left
            r = u.right
            if l is not None:
                l.right = v
            if r is not None:
                r.left = v
            v.left = l
            v.right = r
            u.value = val
            u.flag = OCCUPIED
            u.key = k
    def __str__(self):
        ans = ''
        for i, v in enumerate(self.arr):
            ans += f'Node(slot={i}, key={v.key}, value={v.value}, flag={v.flag})\n'

        return ans


ht = HashTable(n=20, h=lambda x: x%20)
print(ht)
ht.insert(1,1)
print(ht)
ht.insert(21,4)
print(ht)
ht.insert(1,4)
print(ht)
