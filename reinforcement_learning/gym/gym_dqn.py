import random

import gym
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from tqdm import tqdm

I = 4  # Input dimensions
H = 64  # Hidden layer dimensions
O = 2  # output dimensions (one-hot encoding)


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


model = MyModel()
opt = keras.optimizers.Adam(learning_rate=0.1)
model.compile(optimizer=opt, loss="mse", metrics=["mae"])

NUM_ITERATIONS = 50
NUM_EPISODES = 10
NUM_STEPS = 50
env = gym.make('CartPole-v0')
gamma = 1
epsilon = 0.5
alpha = 0.1
EXP = 1
training_history = []
for it in range(NUM_ITERATIONS):
    print(f'Iteration {it}/{NUM_ITERATIONS}')
    xs = []
    ys = []
    for _ in tqdm(range(NUM_EPISODES)):
        history = []
        env.reset()
        obs, reward, done, info = env.step(env.action_space.sample())
        for _ in range(NUM_STEPS):
            env.render()
            if random.random() < (1 - it / NUM_ITERATIONS) ** EXP:
            # if random.random() < epsilon:
                next_action = env.action_space.sample()
            else:
                x = np.array([obs])
                out = model.predict(x)[0]
                next_action = np.argmax(out)
            obs2, reward, done, info = env.step(next_action)
            history.append([obs, next_action, reward, done, info])
            obs = obs2
            # if done: break
        history.reverse()
        G = 0
        x, y = [], []
        for curr_state, next_action, reward, _, _ in history:
            G = gamma * G + reward
            # full_state = np.append(curr_state, next_action)
            x.append(curr_state)
            nxtval = model.predict(np.array([curr_state]))[0]
            # print(f'curr_state: {curr_state} next_action: {next_action} rew: {reward}')
            # print(f'G: {G} nxtval: {nxtval}')
            nxtval[next_action] = nxtval[next_action] * (1 - alpha) + alpha * G
            y.append(nxtval)
            # print(f'nxtval: {nxtval}')

        xs.append(np.array(x))
        ys.append(np.array(y))

    xs = np.concatenate(np.array(xs))
    ys = np.concatenate(np.array(ys))
    # print(xs)
    # print(ys)
    hist = model.fit(xs, ys, epochs=100)
    training_history.append(hist.history)

fig, ax = plt.subplots()
xs = list(map(lambda x: x['mae'], training_history))

with open("deep_gym_model/training_history.txt", "w+") as f:
    f.write(str(training_history))
model.save('deep_gym_model')
