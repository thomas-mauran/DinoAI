import pygame
from pygame.locals import *


class obstacleClass(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, width, height, speed):
        self.x = x
        self.y = y


        self.surface = surface

        self.width = width
        self.height = height

        self.speed = speed
        
    def draw(self):
        pygame.draw.rect(self.surface, (0, 0, 0),pygame.Rect(self.x, self.y, self.width, self.height
        ))
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

