import pygame
from pygame.locals import *

import numpy as np

class obstacleClass(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, width, height, speed, mode):
        self.x = x
        self.y = y


        self.surface = surface

        self.width = width
        self.height = height
        self.mode = mode

        self.speed = speed

        if self.mode == "human":
            img = pygame.image.load("./env/assets/cactus.png").convert_alpha()
            self.img = pygame.transform.scale(img, (self.width *  3, self.height * 1.3))

    def draw(self):
        # pygame.draw.rect(self.surface, (0, 0, 0),pygame.Rect(self.x, self.y, self.width, self.height
        # ))
        if self.mode == "human":
            pygame.draw.rect(self.surface, (0, 0, 0),pygame.Rect(self.x, self.y, self.width, self.height
            ))
        else:
            self.surface.blit(self.img, (self.x, self.y - self.y / 14 ))

    def update(self):
        self.x -= self.speed

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def get_width(self):
        return self.width    

    def get_height(self):
        return self.height

    def getWidth(self):
        return self.width

    def obs(self):
        return np.array([self.x, self.y, self.width, self.height], dtype=int)

