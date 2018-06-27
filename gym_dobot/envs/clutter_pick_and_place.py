from gym import utils
from gym_dobot.envs import clutter_env


class DobotClutterPickAndPlaceEnv(clutter_env.DobotClutterEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse',clutter_num=40):
        initial_qpos = {
            'dobot:slide0': 0.8,
            'dobot:slide1': 1.2,
            'dobot:slide2': -0.04,
            'object0:joint': [1.25, 0.53, 0.821,  1., 0., 0., 0.],
        }
        clutter_env.DobotClutterEnv.__init__(
            self, 'dobot/clutter_pick_and_place.xml', has_object=True, block_gripper=False, n_substeps=20,
            gripper_extra_height=0, target_in_the_air=True, target_offset=.0,
            obj_range=0.185, target_range=0.2, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type,
            clutter_num=clutter_num)
        utils.EzPickle.__init__(self)
