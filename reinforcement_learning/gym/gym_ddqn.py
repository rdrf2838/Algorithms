# import random

import gym
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras

I = 4  # Input dimensions
H = 64  # Hidden layer dimensions
O = 2  # output dimensions (one-hot encoding)
LEARNING_RATE = 0.001
REPLAY_LENGTH = 1000
EPISODE_NUM = 1000
EPISODE_LENGTH = 200
WARMUP_LENGTH = 10
EPSILON = 0.1
MINIBATCH_SIZE = 1000
GAMMA = 1

class MyModel(tf.keras.Model):

    def __init__(self):
        super(MyModel, self).__init__()
        self.dense1 = keras.layers.Dense(I, activation=tf.nn.relu)
        self.dense2 = keras.layers.Dense(H, activation=tf.nn.relu)
        self.dense3 = keras.layers.Dense(H, activation=tf.nn.relu)
        self.dense4 = keras.layers.Dense(O)

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        x = self.dense3(x)
        return self.dense4(x)


class Replay:
    def __init__(self, n):
        self.rng = np.random.default_rng()
        self.n = n
        self.arr = []

    def debug(self, n):
        print(np.array(self.arr, dtype='object'))
        print(self.rng.choice(np.array(self.arr, dtype='object'), (n,)))

    def sample(self, n):
        minibatch = self.rng.choice(np.array(self.arr, dtype='object'), (n,))
        obs2_arr = np.vstack(minibatch[:, 3]).astype(np.float)
        obs_arr = np.vstack(minibatch[:, 0]).astype(np.float)
        action_arr = np.vstack(minibatch[:, 1]).astype(np.int).flatten()
        reward_arr = np.vstack(minibatch[:, 2]).astype(np.float).flatten()
        return obs_arr, action_arr, reward_arr, obs2_arr

    def add_one(self, v):
        self.arr.append(v)
        if len(self.arr) > self.n:
            self.arr.pop(0)


model1 = MyModel()
opt = keras.optimizers.Adam(learning_rate=LEARNING_RATE)
model1.compile(optimizer=opt, loss="mse", metrics=["mae"])
model2 = MyModel()
opt = keras.optimizers.Adam(learning_rate=LEARNING_RATE)
model2.compile(optimizer=opt, loss="mse", metrics=["mae"])

replay = Replay(REPLAY_LENGTH)
env = gym.make('CartPole-v0')

for episode in range(EPISODE_NUM):
    env.reset()
    obs, reward, done, info = env.step(env.action_space.sample())
    for time in range(EPISODE_LENGTH):
        env.render()
        if np.random.rand() < EPSILON or episode < WARMUP_LENGTH:
            next_action = env.action_space.sample()
        else:
            action_values = model1.predict(np.array([obs]))[0] + model2.predict(np.array([obs]))[0]
            next_action = np.argmax(action_values)
        obs2, reward, done, info = env.step(next_action)
        replay.add_one((obs, next_action, reward, obs2))
        obs = obs2
    if episode >= WARMUP_LENGTH:
        obs_arr, action_arr, reward_arr, obs2_arr = replay.sample(MINIBATCH_SIZE)
        idx = np.array(range(MINIBATCH_SIZE), dtype=int)
        if np.random.rand() < 0.5:
            x = obs_arr
            y = model1.predict(obs_arr)
            y2 = model2.predict(obs2_arr)
            y[idx, action_arr] = GAMMA * np.max(y2, axis=1) + reward_arr
            model1.fit(x, y)
        else:
            x = obs_arr
            y = model2.predict(obs_arr)
            y2 = model1.predict(obs2_arr)
            y[idx, action_arr] = GAMMA * np.max(y2, axis=1) + reward_arr
            model2.fit(x, y)

model1.save('ddqn')
