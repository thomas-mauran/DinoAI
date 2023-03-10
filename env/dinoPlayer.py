import pygame
from pygame.locals import *
import numpy as np

class dinoPlayerClass(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, width, height, mode):
        super().__init__()

        self.default_top_offset = y

        self.default_width = x
        self.default_height = y

        self.default_x = x
        self.default_y = y

        self.x = x
        self.y = y


        self.velocity = 2
        self.surface = surface

        self.width = width
        self.height = height


        self.canJump = True
        self.stand = True

        self.mass = 2

        self.mode = mode

        if self.mode == "human":
            img = pygame.image.load("./env/assets/dino.png").convert_alpha()
            self.img = pygame.transform.scale(img, (self.width *  3, self.height * 2))
    def update(self):

        if self.canJump == False:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.velocity < 0:
                F = ( 0.5 * self.mass * (self.velocity*self.velocity) )
            else:
                F = -( 0.5 * self.mass * (self.velocity*self.velocity) )
           
            self.y += F

            self.velocity -= 0.018
 
            # We hit the floor we can jump again
            if self.y - 1 >= self.default_top_offset:
                self.canJump = True
                self.velocity = 2
    
    def draw(self):


        if self.mode == "human":
            pygame.draw.rect(self.surface, (200, 0, 0),pygame.Rect(self.x, self.y, self.width, self.height
            ))
            # self.surface.blit(self.img, (self.x, self.y - self.y / 5 ))

        else:
            pygame.draw.rect(self.surface, (200, 0, 0),pygame.Rect(self.x, self.y, self.width, self.height
            ))
            # self.surface.blit(self.img, (self.x, self.y - self.y / 5 ))

    def jump(self):
        if self.canJump and self.stand:
            self.canJump = False
    def get_y(self):
        return self.y
    def get_x(self):
        return self.x

    def get_width(self):
        return self.width    
    def get_height(self):
        return self.height

    def down(self):
        self.y = self.default_y

    def getJump(self):
        return self.canJump
    def obs(self):
        return np.array([self.x, self.y, self.width, self.height], dtype=int)

    def reset(self):
        self.x = self.default_x
        self.y = self.default_y
        self.velocity = 2

        self.canJump = True
        self.stand = True

    # def down(self):
    #     self.stand = not self.stand

    #     if self.stand:
    #         self.width = self.default_width
    #         self.height = self.default_height
    #         self.y = self.default_y
    #     else:
    #         print('crouch')
    #         self.height = self.width / 2
    #         self.y += self.height



