import gym
import tensorflow.keras as keras
import numpy as np

model = keras.models.load_model('deep_gym_model')
env = gym.make('CartPole-v0')

env.reset()
for _ in range(10):
    obs, reward, done, info = env.step(env.action_space.sample())
for _ in range(1000):
    env.render()
    action_values = model.predict(np.array([obs]))[0]
    next_action = np.argmax(action_values)
    obs, reward, done, info = env.step(next_action)
    # if done: break
env.close()
