from env.dinoEnv import dinoEnvClass

from stable_baselines3 import PPO
from stable_baselines3 import DQN
from stable_baselines3 import A2C
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.evaluation import evaluate_policy



import os 

env = dinoEnvClass(render_mode="human")
check_env(env)

env.reset()
episodes = 10


# for episode in range (1, episodes + 1):
#     state = env.reset()
#     done = False
#     score = 0

#     while not done:
#         env.render()
#         action = env.action_space.sample()
#         n_state, reward, done, info= env.step(action)
#         score += reward
#     print ("Episode: {} Score: {}".format(episode, score))
# env.close()

model_path = os.path.join('files', 'Saved_Models', 'DQN_buffer.zip')

model = DQN.load(model_path, env=env)

evaluate_policy(model, env, n_eval_episodes=2, render=True)

# for episode in range (1, episodes + 1):
#     obs = env.reset()
#     done = False
#     score = 0

#     while not done:
#         env.render()
#         action, _ = model.predict(obs)
#         obs, reward, done, info = env.step(action)
#         score += reward
#         print(obs)
#     print ("Episode: {} Score: {}".format(episode, score))
# env.close()


