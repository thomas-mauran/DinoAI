from env.dinoEnv import dinoEnvClass
from stable_baselines3.common.env_checker import check_env
import os

import gym
from multiprocessing import freeze_support

from stable_baselines3 import PPO
from stable_baselines3 import DQN
from stable_baselines3 import A2C
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold


from gym.envs.registration import register

register(
    id='ChromeDino-v0', 
    entry_point='env.dinoEnv:dinoEnvClass', 
)


freeze_support()

nproc = 8
env_name = 'ChromeDino-v0'


def make_env():
    def _f():
        env = gym.make('ChromeDino-v0')
        return env
    return _f

if __name__ == '__main__':
    freeze_support()
    envs = [make_env() for i in range(nproc)]
    envs = SubprocVecEnv(envs)
    envs = VecFrameStack(envs, n_stack=10)


    envs = gym.make(env_name)
    check_env(envs)
    print(envs.action_space.sample())


    # # Random method
    # episodes = 5

    # for episode in range (1, episodes + 1):
    #     state = envs.reset()
    #     done = False
    #     score = 0

    #     while not done:
    #         envs.render()
    #         action = envs.action_space.sample()
    #         obs, reward, done, info, _ = envs.step(action)
    #         score += reward
    #     print ("Episode: {} Score: {} Obs: {}".format(episode, score, obs))
    # envs.close()

    log_path = os.path.join('files', 'Logs')

    save_path = os.path.join('files', 'Saved_Models', 'DQN_1')

    model = DQN('MultiInputPolicy', envs, verbose=1, tensorboard_log=log_path)

    model.learn(total_timesteps=1000000)    


    model.save(save_path)    
