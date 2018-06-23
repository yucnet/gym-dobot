# gym-dobot
Open AI Gym Environment for the [Dobot Magician Robotic Arm](https://www.dobot.cc/dobot-magician/product-overview.html).
Based on the [fetch](https://gym.openai.com/envs/#robotics) environments provided by gym.

Currently consists of -
 - DobotPickAndPlaceEnv
 - DobotPushEnv
 - DobotClutterPickAndPlaceEnv
 - DobotClutterPushEnv

The ClutterEnv variations add additonal blocks as clutter. The number of blocks can be changed by setting ```clutter_num``` while creating the environment.(Max=40,Default=20)
 
 Requires - 
  - python 3 (Tested on Python 3.6)
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
from gym_dobot.envs import DobotClutterPickAndPlaceEnv

env = DobotClutterPickAndPlaceEnv(clutter_num=10)
for i_episode in range(50):
    observation = env.reset()
    for time_step in range(50):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
```
Alternatively, directly run ```pick.py```,```push.py```, ```clutter_pick.py``` or ```clutter_push.py``` which call the respective environments.
