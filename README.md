<div align="center"> 
<h1>Chrome dino game machine learning</h1>

  <img src="./env/assets/readme.gif" alt="Laputa guardian gif" width="70%">
</div>


# What's the goal ?

The goal of this project is to make the environment of the famous chrome dino game and build / train a machine learning algorithm to beat it. <br>
This game is very simple, since your goal is to avoid obstacles by jumping over them or crouching on the floor, the score is calculated using. The version of the game I will develop will only have the jump option

## Tech stack
- Python3
- Stablebaselines3
- Tensorboard
- Pygames
- Gym environments

## setup steps 

#### clone the repo
```bash
git@github.com:thomas-mauran/DinoAI.git
```

#### install python3 
```bash
apt install python3
```
#### install pip
```bash
apt install pip
```

#### install gym 
```bash
pip install gym
```

#### install stable-baseline3 
```bash
pip install stable-baselines3[extra]
```

#### install pygame 
```bash
pip install pygame
```

## how to use it 

the env is stocked and made in the env folder. You can train a model in the train.py file using the ml algorithm you want or change the values of the current one. Then after the training you can set the model path var to the model you just made and run the file to see how it performs 

#### train a model
:warning: make sure you change the model name in the file (save_path variable)
```bash
python3 train.py
```
#### test a model
:warning: make sure you load the good model in the model_path variable

```bash
python3 test.py
```