from env.dinoEnv import dinoEnvClass

from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.evaluation import evaluate_policy

import os 

env = dinoEnvClass(render_mode="human")
check_env(env)



model_path = os.path.join('files', 'Saved_Models', 'DQN_no_jump5.zip')
model = DQN.load(model_path, env=env)
evaluate_policy(model, env, n_eval_episodes=5, render=False)



# episodes = 10
# for episode in range (1, episodes + 1):
#     state = env.reset()
#     done = False
#     score = 0

#     while not done:
#         env.render(mode="human")
#         action = env.action_space.sample()
#         n_state, reward, done, info= env.step(action)
#         score += reward

#     print ("Episode: {} Score: {}".format(episode, score))
# env.close()