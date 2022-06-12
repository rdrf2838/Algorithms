import math


class SegmentTree:
    def __init__(self):
        self.xs = None
        self.la = 0
        self.la2 = 0

    def initialise(self, a):
        self.la = len(a)
        self.la2 = 2 ** math.ceil(math.log2(len(a)))
        self.xs = [0] * (self.la2 * 2 - 1)
        s = len(self.xs) // 2
        self.xs[s:s + self.la] = a
        for i in reversed(range(s)):
            self.xs[i] = self.xs[2 * i + 1] + self.xs[2 * i + 2]

    def range_sum(self, l, r):
        return self._q(l, r, 0)

    def _q(self, l, r, i):
        d = 2 ** math.floor(math.log2(i + 1))
        w = self.la2 // d
        lc = (i - d + 1) * w
        rc = lc + w
        if l == lc and r == rc:
            return self.xs[i]
        else:
            m = (lc + rc) // 2
            if r <= m:
                return self._q(l, r, 2 * i + 1)
            elif l >= m:
                return self._q(l, r, 2 * i + 2)
            else:
                return self._q(l, m, 2 * i + 1) + self._q(m, r, 2 * i + 2)

    def update(self, i, v):
        j = self.la2 + i
        self.xs[j] = v
        while j > 0:
            p = (j - 1) // 2
            self.xs[p] = self.xs[2 * p + 1] + self.xs[2 * p + 2]
            j = p


st = SegmentTree()
xs = [1, 2, 3, 4, 5, 6]
st.initialise(xs)
# for i in range(len(xs)):
#     for j in range(i + 1, len(xs) + 1):
#         print(f"({i}, {j}): {st.range_sum(i, j)}")
for i in range(len(xs)):
    st.update(i, 1)
for i in range(len(xs)):
    for j in range(i + 1, len(xs) + 1):
        print(f"({i}, {j}): {st.range_sum(i, j)}")
