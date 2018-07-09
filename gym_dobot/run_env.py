import gym
import click
import gym_dobot.envs as envs
from scipy.misc import imsave


@click.command()
@click.option('--env', default="DobotPickAndPlaceEnv", help='Which environment to run (Eg. - DobotReachEnv)')
@click.option('--render',default=True,help='Whether to render the environment')
@click.option('--steps',default=100,help='Number of timesteps to run the environment each time')
@click.option('--clutter',default=20,help='Number of clutter objects for clutter environments')
@click.option('--rand_dom',default=False,help='Whether to use domain randomization')
def main(env,render,steps,clutter,rand_dom):
    if 'Clutter' in env:
        env = getattr(envs,env)(clutter_num=clutter,rand_dom=rand_dom)
    else:
        env = getattr(envs,env)(rand_dom=rand_dom)

    while True:
        observation = env.reset()
        for i in range(steps):
            if render:
                env.render()
                #img = env.capture()
                #imsave("image.png", img)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

if __name__=='__main__':
    main()