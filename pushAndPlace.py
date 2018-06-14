import gym
import random
import numpy as np
from gym_dobot.envs import DobotPickAndPlaceEnv

env = DobotPickAndPlaceEnv()
nums = [1,-1]
actions = []
for i_episode in range(10):
    observation = env.reset()
    while True:
        env.render()
        action = env.action_space.sample()
        actions.append(action)
        print("STD = ",np.std(actions,axis=0))
        #action = [random.choice(nums) for i in range(4)]
        observation, reward, done, info = env.step(action)
