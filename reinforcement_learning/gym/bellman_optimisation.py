import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

N = 100


def a(s):
    return range(1, min(s, N - s) + 1)


theta = 0.0001
p_win = 0.3
s = list(range(N + 1))
V = [0] * (N + 1)
V[N] = 1

while True:
    delta = 0
    for curr_state in s:
        if curr_state == N or curr_state == 0:
            continue
        v = V[curr_state]
        action_range = a(curr_state)
        for curr_action in action_range:
            win_state = curr_state + curr_action
            lose_state = curr_state - curr_action
            V[curr_state] = max(
                V[curr_state],
                p_win * V[win_state] + (1 - p_win) * V[lose_state]
            )
        delta = max(delta, abs(v - V[curr_state]))
    if delta < theta: break

fig, ax = plt.subplots()
ax.plot(range(len(V)), V)
plt.show()

pi = [0] * (N + 1)

for curr_state in s:
    if curr_state == 0 or curr_state == N: continue
    actions = a(curr_state)
    best_val = -1
    for curr_action in actions:
        win_state = curr_state + curr_action
        lose_state = curr_state - curr_action
        next_val = p_win * V[win_state] + (1 - p_win) * V[lose_state]
        if next_val - best_val >= theta:
            best_val = next_val
            pi[curr_state] = curr_action
# fig, ax = plt.subplots()
# ax.plot(range(len(pi)), pi)
# plt.show()

plt.bar(range(len(pi)), pi)
plt.show()