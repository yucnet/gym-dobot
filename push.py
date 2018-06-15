import gym
from gym_dobot.envs import DobotPushEnv

env = DobotPushEnv()
while True:
    observation = env.reset()
    for i in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
