import gym
from gym_dobot.envs import DobotPushEnv

env = DobotPushEnv()
for i_episode in range(10):
    observation = env.reset()
    while True:
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
