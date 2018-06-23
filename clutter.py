import gym
from gym_dobot.envs import DobotClutterPickEnv

env = DobotClutterPickEnv(clutter_num=5)
while True:
    observation = env.reset()
    for i in range(50):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
