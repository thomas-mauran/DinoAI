from env.dinoEnv import dinoEnvClass
import os

from stable_baselines3 import DQN

from gym.envs.registration import register

register(
    id='ChromeDino-v0', 
    entry_point='env.dinoEnv:dinoEnvClass')

env = dinoEnvClass()


log_path = os.path.join('files', 'Logs')
save_path = os.path.join('files', 'Saved_Models', 'DQN_no_jump6')

model = DQN('CnnPolicy', env, verbose=3, tensorboard_log=log_path, buffer_size=50000, learning_starts=50000)

model.learn(total_timesteps=500000)    
model.save(save_path)
