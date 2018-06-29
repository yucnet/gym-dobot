import gym
from gym_dobot.envs import DobotPushEnv
import mujoco_py
from scipy import misc

env = DobotPushEnv()
viewer = mujoco_py.MjViewer(env.sim)
for j in range(1000):
    img = viewer._read_pixels_as_in_window()
    misc.imsave('test.png',img)
    observation = env.reset()
    img = viewer._read_pixels_as_in_window()
    misc.imsave('imgs/test{}.png'.format(j),img)
    for i in range(50):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
