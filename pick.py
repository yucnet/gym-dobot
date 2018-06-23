import gym
from gym_dobot.envs import DobotPickAndPlaceEnv

env = DobotPickAndPlaceEnv()
while True:
    observation = env.reset()
    for i in range(5000):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
