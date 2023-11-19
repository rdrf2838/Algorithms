import multiprocessing
import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from tqdm import tqdm

IT_COUNT = -1
POW = 10
FRAC = 3
CORE_NUM = 8
NUM_ITERATIONS = 5
TOURNAMENT_SIZE = 2 ** POW
WINNER_SIZE = 2 ** (POW - FRAC)
HOF_SIZE = 16
SIGMA = 20
EXP = 2
BASE = 2
A = -1
B = 1


def compare(v):
    a, b = v
    ctr: int = 0
    prev = 0
    a_score = 0
    b_score = 0
    for i in range(10):
        if a[i] > b[i]:
            a_score += i + 1
            if prev == A:
                ctr += 1
                if ctr == 3:
                    i += 1
                    a_score += (10 - i) * (i + 11) / 2
                    break
            else:
                prev = A
                ctr = 1

        elif b[i] > a[i]:
            b_score += i + 1
            if prev == B:
                ctr += 1
                if ctr == 3:
                    i += 1
                    b_score += (10 - i) * (i + 11) / 2
                    break
            else:
                prev = B
                ctr = 1
    return a if a_score > b_score else b


def mutate(a, amt):
    for i, v in enumerate(a):
        a[i] = v + int(amt * random.gauss(0, 1))
        a[i] = max(0, a[i])
    if sum(a) > 100:
        v = sum(a) - 100
        while v > 0:
            i = random.randint(0, 9)
            tmp = a[i]
            a[i] = max(0, a[i] - v)
            v = v - tmp + a[i]
    elif sum(a) < 100:
        v = 100 - sum(a)
        i = random.randint(0, 9)
        a[i] += v
    return a[:]


# input at least 4
def compare_distributed(vs):
    while len(vs) > WINNER_SIZE // CORE_NUM:
        a = vs.pop(0)
        b = vs.pop(0)
        vs.append(compare((a, b)))
    return vs


def compare_distributed_hof(vs):
    while len(vs) > HOF_SIZE // CORE_NUM:
        a = vs.pop(0)
        b = vs.pop(0)
        vs.append(compare((a, b)))
    return vs


def mutate_distributed(vs):
    n = TOURNAMENT_SIZE // CORE_NUM
    res = []
    for _ in range(n):
        res.append(mutate(random.choice(vs), BASE + SIGMA * (1 - IT_COUNT / NUM_ITERATIONS) ** EXP))
        # res.append(mutate(random.choice(vs), BASE + SIGMA * (1 - (IT_COUNT / NUM_ITERATIONS) ** EXP)))
    return res


def multi_mutate(v):
    inputs = []
    l = WINNER_SIZE // CORE_NUM
    for i in range(CORE_NUM):
        inputs.append(v[int(l * i):int(l * (i + 1))])

    with multiprocessing.Pool() as pool:
        outputs = pool.map(mutate_distributed, inputs)
    return [item for sublist in outputs for item in sublist]


def multi_get_winners(v):
    inputs = []
    l = TOURNAMENT_SIZE // CORE_NUM
    for i in range(CORE_NUM):
        inputs.append(v[int(l * i):int(l * (i + 1))])
    with multiprocessing.Pool() as pool:
        outputs = pool.map(compare_distributed, inputs)
    return [item for sublist in outputs for item in sublist]


def multi_get_hof(v):
    inputs = []
    l = WINNER_SIZE // CORE_NUM
    for i in range(CORE_NUM):
        inputs.append(v[int(l * i):int(l * (i + 1))])
    with multiprocessing.Pool() as pool:
        outputs = pool.map(compare_distributed_hof, inputs)
    return [item for sublist in outputs for item in sublist]


if __name__ == '__main__':
    history = [[10.0] * 10]
    prev_winners = [[10] * 10] * WINNER_SIZE
    for i in tqdm(range(NUM_ITERATIONS)):
        IT_COUNT = i
        curr_participants = []
        curr_participants = multi_mutate(prev_winners)
        prev_winners = multi_get_winners(curr_participants)
        hof = multi_get_hof(prev_winners)
        tot = np.sum(np.array(hof), axis=0) / HOF_SIZE
        history.append(tot)

    hof = multi_get_hof(prev_winners)
    print(hof)

    fig, ax = plt.subplots()
    ax.set_title(f'it: {NUM_ITERATIONS} sz: {TOURNAMENT_SIZE}')
    ax.set_xticks(range(1, 11))
    for v in hof:
        plt.plot(range(1, 11), v)
    plt.savefig('HOF.png')
    plt.show()

    history = np.array(history)
    fig, ax = plt.subplots()
    line = ax.plot(range(1, 11), history[0, :])[0]


    def animate(i):
        line.set_ydata(history[i, :])
        ax.set_xticks(range(1, 11))
        ax.set_ylim([0, 50])
        ax.set_title(f'Iteration {i}/{NUM_ITERATIONS}')


    anim = FuncAnimation(fig, animate, interval=100, frames=len(history))
    plt.draw()
    plt.show()

    anim.save('history.gif')
