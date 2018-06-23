from gym.envs.registration import register

for reward_type in ['sparse', 'dense']:
    suffix = 'Dense' if reward_type == 'dense' else ''
    kwargs = {
        'reward_type': reward_type,
    }

register(
    id='DobotPush{}-v0'.format(suffix),
    entry_point='gym_dobot.envs:DobotPushEnv',
    kwargs=kwargs,
    max_episode_steps=50,
)

register(
    id='DobotPickAndPlace{}-v0'.format(suffix),
    entry_point='gym_dobot.envs:DobotPickAndPlaceEnv',
    kwargs=kwargs,
    max_episode_steps=50,
)

register(
    id='DobotClutterPickAndPlace{}-v0'.format(suffix),
    entry_point='gym_dobot.envs:DobotClutterPickAndPlaceEnv',
    kwargs=kwargs,
    max_episode_steps=50,
)

register(
    id='DobotClutterPush{}-v0'.format(suffix),
    entry_point='gym_dobot.envs:DobotClutterPushEnv',
    kwargs=kwargs,
    max_episode_steps=50,
)