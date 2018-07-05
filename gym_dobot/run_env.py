import gym
import click
import gym_dobot.envs as envs


@click.command()
@click.option('--env', default="DobotPickAndPlaceEnv", help='Which environment to run (Eg. - DobotReachEnv)')
@click.option('--render',default=1,help='Whether to render the environment')
@click.option('--steps',default=100,help='Number of timesteps to run the environment each time')
@click.option('--clutter',default=20,help='Number of clutter objects for clutter environments')
def main(env,render,steps,clutter):
    if 'Clutter' in env:
        env = getattr(envs,env)(clutter_num=clutter)
    else:
        env = getattr(envs,env)()

    while True:
        observation = env.reset()
        for i in range(steps):
            if render:
                env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

if __name__=='__main__':
    main()