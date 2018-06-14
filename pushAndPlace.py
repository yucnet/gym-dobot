import gym
import random
import numpy as np
from gym_dobot.envs import DobotPickAndPlaceEnv

env = DobotPickAndPlaceEnv()
for i_episode in range(10):
    observation = env.reset()
    while True:
        env.render()
        action = env.action_space.sample()
        print(env.sim.data.get_joint_qpos("dobot:base_pan"))
        observation, reward, done, info = env.step(action)
