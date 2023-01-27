import pygame
from pygame.locals import *


class obstacleClass(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, width, height, speed):
        self.position_x = x
        self.position_y = y


        self.surface = surface

        self.width = width
        self.height = height

        self.speed = speed
        
    def draw(self):
        pygame.draw.rect(self.surface, (0, 0, 0),pygame.Rect(self.position_x, self.position_y, self.width, self.height
        ))
    def update(self):
        self.position_x -= self.speed
    def getPos_x(self):
        return self.position_x

    def getWidth(self):
        return self.width
    def __del__(self):
        print('destroyed')