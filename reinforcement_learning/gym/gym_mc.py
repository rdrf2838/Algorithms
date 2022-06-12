import random
import gym
import numpy as np

SHAPE = (10, 10, 10, 10, 2)
Q = np.zeros(shape=SHAPE)


def parse(a):
    """
    converts observation space into (4,) with range [0,10) to index into memo table
    :param a: observation space, e.g. [0.1,-0.1,-1.2,1.3]
    """
    a += 1
    a *= 5
    a = np.maximum(a, np.zeros(a.shape))
    a = np.minimum(a, np.full(a.shape, 9))
    a = a.astype(int)
    return a


env = gym.make('CartPole-v0')

theta = 0.001
epsilon = 0.1
gamma = 0.9
lr = 0.1
for _ in range(1000):
    delta = 0
    env.reset()
    history = []
    obs, reward, done, info = env.step(env.action_space.sample())
    for _ in range(1000):
        curr_state = tuple(parse(obs))
        if random.random() < epsilon:
            next_action = env.action_space.sample()
        else:
            next_action = np.argmax(Q[curr_state])
        obs, reward, done, info = env.step(next_action)
        history.append([curr_state, next_action, reward, done, info])
        if done: break

    history.reverse()
    G = 0
    # at this stage instead of using Q we should use a network to learn
    for curr_state, next_action, reward, _, _ in history:
        G += gamma * G + reward
        Q_prev = Q[curr_state][next_action]
        Q[curr_state][next_action] = (1 - lr) * Q_prev + lr * G
        delta = max(delta, abs(Q_prev - Q[curr_state][next_action]))
    if delta < theta: break

env.reset()
obs, reward, done, info = env.step(env.action_space.sample())
for _ in range(1000):
    env.render()
    curr_state = tuple(parse(obs))
    next_action = np.argmax(Q[curr_state])
    obs, reward, done, info = env.step(next_action)
    if done: break
env.close()