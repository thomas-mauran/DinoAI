import gym
from gym.spaces import Box, Discrete, Dict

import pygame
from pygame.locals import *

from .dinoPlayer import dinoPlayerClass
from .obstacles import obstacleClass
import numpy as np
import random
import cv2

from matplotlib import pyplot as plt
import sys

import time

class dinoEnvClass(gym.Env):

    def __init__(self, render_mode=None):      

        self.render_mode = render_mode
        # Defining variables 

        # Screen
        self.screenSize = [1000, 300]
        if render_mode == 'human':
            self.screen = pygame.display.set_mode([self.screenSize[0], self.screenSize[1]])
        else:
            self.screen = pygame.Surface([self.screenSize[0], self.screenSize[1]])
        # Dino
        self.dinoDimension = [30, 60]
        self.y_init = self.screenSize[1] - self.dinoDimension[1]
        self.dino = dinoPlayerClass(self.screen, 40, self.y_init, self.dinoDimension[0], self.dinoDimension[1], self.render_mode)

        # Obstacle list
        self.obstacles = []

        # Game variables
        self.addScore = 0
        self.running = False
        self.speed = 1

        # Gym env 
        # 2 actions, jump, go back to the floor, or do nothing
        self.action_space = Discrete(3)
        self.observation_space = Box(low=0, high=255, shape=(1, 83, 200), dtype=np.uint8)

        self.i = 0
    def _get_obs(self):
        self.i += 1 
        buffer  = pygame.image.tostring(self.screen, "RGB")
        pixels = np.frombuffer(buffer, dtype=np.uint8)
        pixels = pixels.reshape((300, 1000, 3))
        gray = cv2.cvtColor(pixels, cv2.COLOR_BGR2GRAY)

        cropped = gray[217:300, 20:220]
        channel = np.reshape(cropped, (1,83,200))

        # if self.i == 1000:
        #     plt.imshow(channel, interpolation='nearest')
        #     plt.show()
        
        return channel


    def _get_info(self):
        return {}

    def reset(self, seed=None, options=None):


        self.score = 0
        self.running = True

        self.speed = 1
        # reset the env
        self.dino.reset()

        self.obstacles = []
        self.spawn_obstacle(self.speed, 100)
        self.spawn_obstacle(self.speed, 600)



        observation = self._get_obs()
        info = self._get_info()


        if self.render_mode == "human":
            self._render_frame()
            
        return observation

    def render(self, mode):



        pass
    def _render_frame(self):

        self.dino.update()

        for obs in self.obstacles:
            obs.update()
            if obs.get_x() < 0 - obs.getWidth() :
                self.obstacles.remove(obs)
                del obs
                self.addScore = 100
                self.speed += 0.05
                self.spawn_obstacle(self.speed, random.randint(200, 1000))

                
        self.screen.fill((255, 255, 255))

        if self.render_mode == 'human':
            pygame.init()
            pygame.display.init()
        self.dino.draw()


        for obs in self.obstacles:
            obs.draw()
            if self.render_mode == 'human':
                pygame.display.update()


    def step(self, action):


        # time.sleep(0.002)
        # if action == 0:
        #     self.dino.down()
        if action == 1:
            self.dino.jump()

        # self.score = self.score + 0.001
    
        reward = 0

        self._render_frame()
        terminated = self.isGameDone()
        
        if terminated:
            reward = -100
        
        if self.checkJumpOver():
            reward = 10

        observation = self._get_obs()
        info = {}
        return observation, reward, terminated, info



    def close(self):

        
        if self.screen is not None:
            pygame.display.quit()
            pygame.quit()

    def spawn_obstacle(self, speed, offset):
        obstacle = obstacleClass(self.screen, self.screenSize[0] + offset,self. y_init, self.dinoDimension[0], self.dinoDimension[1], speed, self.render_mode)
        self.obstacles.append(obstacle)





    def isHittingDino(self, obstacle):
        dinoX = self.dino.get_x()
        dinoY = self.dino.get_y()
        dinoWidth = self.dino.get_width()
        dinoHeight = self.dino.get_height()

        obstacleX = obstacle.get_x()
        obstacleY = obstacle.get_y()
        obstacleWidth = obstacle.get_width()
        obstacleHeight = obstacle.get_height()

        if (obstacleX < dinoX + dinoWidth) and (obstacleX + obstacleWidth > dinoX) and (obstacleY < dinoY + dinoHeight) and (obstacleHeight + obstacleY > dinoY):
            
            return True
        return False

    def jumpedOver(self, obstacle):
        dinoX = self.dino.get_x()
        dinoY = self.dino.get_y()
       
        obstacleX = obstacle.get_x()
        obstacleY = obstacle.get_y()
        obstacleHeight = obstacle.get_height()
 
        if (dinoX >= obstacleX and dinoY <= obstacleY - obstacleHeight):
            return True


        return False


    def isGameDone(self):

        for obs in self.obstacles:
            if self.isHittingDino(obs):
                return True
        return False

    def checkJumpOver(self):
        for obs in self.obstacles:
            if self.jumpedOver(obs):
                return True
        return False

    # def initGame(self):
        
    #     # self.score = 0
    #     self.running = True

    #     self.spawn_obstacle(0.1, random.randint(100, 400))
    #     self.spawn_obstacle(0.1, random.randint(600, 1000))

    #     self.main()

    # def main(self):

    #     while running:
    #         self.speed += random.uniform(0.0000001, 0.000001)


    #         self.screen.fill((255, 255, 255))

    #         # self.score = self.score + 0.001

    #         # Event handlers 
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     self.dino.jump()
    #                 if event.key == pygame.K_DOWN:
    #                     self.dino.down()

    #         # Draw the objects on the screen

    #         self.dino.update()
    #         self.dino.draw()

    #         for obs in self.obstacles:
    #             obs.update()
    #             obs.draw()
    #             if self.isHittingDino(obs):
    #                 running = False
    #             if obs.get_x() < 0 - obs.getWidth() :
    #                 self.obstacles.remove(obs)
    #                 del obs
    #                 # self.score += 100
    #                 self.spawn_obstacle(self.speed, random.randint(30, 1000))

    #         # Update the scren frames
    #         pygame.display.update()
        
    #         #print(round(score))

    #     print(round(self.score))
    #     pygame.quit()


