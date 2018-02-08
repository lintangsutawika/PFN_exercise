from toyRF import CartPoleEnv
from random import *
import sys

env = CartPoleEnv()

new_obs = env.reset()
sys.stderr.write("Reset: {}\n".format(new_obs))
for i in range(500):
    action = randint(0, 1) * 2 - 1
    new_obs, stopSignal, reward = env.step(action)
    sys.stderr.write("{}. new_obs: {},stopSignal: {},Reward: {}\n".format(i,new_obs, stopSignal, reward))
