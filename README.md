# gym-dobot
Open AI Gym Environment for the Dobot Magician Robotic Arm.
Based on the fetch environments provided by gym.

Currently consists of -
 - DobotPickAndPlace
 - DobotPush
 
 Requires - 
  - python 3.6
  - gym > 0.10.3
  - mujoco_py > 1.5
  - mujoco - mjpro150 


## Installation
```bash
cd gym-dobot
pip install -e .
```

## Test
Test everything is working by running the following snippet - 
```python
import gym
from gym_dobot.envs import DobotPickAndPlaceEnv

env = DobotPickAndPlaceEnv()
for i_episode in range(10):
    observation = env.reset()
    while True:
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
```
