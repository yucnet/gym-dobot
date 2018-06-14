import numpy as np
from tkinter import *

import gym
from gym_dobot.envs import DobotPickAndPlaceEnv



env = DobotPickAndPlaceEnv()
env.render()


def update_env(event):
    action = np.array([w1.get(),w2.get(),w3.get(),w4.get()])
    observation, reward, done, info = env.step(action)
    

root = Tk()
root.title("Dobot Controller")
root.geometry("300x300")
w1 = Scale(root, from_=-1, to=1, orient=HORIZONTAL,label="X Coordinate",resolution=0.01,command=update_env)
w1.pack()
w2 = Scale(root, from_=-1, to=1, orient=HORIZONTAL,label="Y Coordinate",resolution=0.01,command=update_env)
w2.pack()
w3 = Scale(root, from_=-1, to=1, orient=HORIZONTAL,label="Z Coordinate",resolution=0.01,command=update_env)
w3.pack()
w4 = Scale(root, from_=-1, to=1, orient=HORIZONTAL,label="Gripper Cont",resolution=0.01,command=update_env)
w4.pack()

while True:
    env.render()
    root.update()
