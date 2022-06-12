import numpy as np


def random_sizes(N, avg_size, rng=None):
    if rng is None: rng = np.random.default_rng()
    return rng.geometric(1 / avg_size, size=N)


def trunc_sizes(s):
    N = len(s)
    i = np.argmax(np.cumsum(s) >= N)
    r = s[:i]
    return np.append(r, N - np.sum(r))


def first_occ(loc_sizes):
    M = len(loc_sizes)
    f = np.cumsum(loc_sizes)[:-1]
    return np.insert(f, 0, 0)


def person_in(loc_sizes):
    M = len(loc_sizes)
    return np.repeat(np.arange(M), loc_sizes)

def exposure(infected, loc_sizes):
    fo = first_occ(loc_sizes)
    lo = np.append(fo[1:]-1, len(infected)-1)
    ci = np.cumsum(infected)
    i = ci[lo] - ci[fo] + infected[fo]
    pi = person_in(loc_sizes)
    return i[pi]

infected = np.array([0,1,1,0,1,0,0,0,1,0,0,0])
loc_sizes = np.array([4,1,1,3,3])
b = exposure(infected, loc_sizes)
print(b)