from env.dinoEnv import dinoEnvClass
from stable_baselines3.common.env_checker import check_env
import os

from stable_baselines3 import PPO
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold

env = dinoEnvClass()
check_env(env)
print(env.action_space.sample())

# env = AsyncVectorEnv([lambda: dinoEnvClass()])
episodes = 5

# print(env.observation_space.sample())

# Random method
# for episode in range (1, episodes + 1):
#     state = env.reset()
#     done = False
#     score = 0

#     while not done:
#         env.render()
#         action = env.action_space.sample()
#         obs, reward, done, info, _ = env.step(action)
#         score += reward
#     print ("Episode: {} Score: {} Obs: {}".format(episode, score, obs))
# env.close()

log_path = os.path.join('files', 'Logs')

save_path = os.path.join('files', 'Saved_Models')

model = PPO('MultiInputPolicy', env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=1000000)

PPO_Path = os.path.join('files', 'Saved_Models', 'PPO_2')
model.save(PPO_Path)