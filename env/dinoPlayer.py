import pygame
from pygame.locals import *

class dinoPlayerClass(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, width, height):
        super().__init__()

        self.default_top_offset = y

        self.position_x = x
        self.position_y = y


        self.velocity = 2
        self.surface = surface

        self.width = width
        self.height = height


        self.canJump = True

        self.mass = 0.2
    def update(self):

        if self.canJump == False:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.velocity < 0:
                F = ( 0.5 * self.mass * (self.velocity*self.velocity) )
            else:
                F = -( 0.5 * self.mass * (self.velocity*self.velocity) )
           
            self.position_y += F

            self.velocity -= 0.002
 
            # We hit the floor we can jump again
            if self.position_y - 1 >= self.default_top_offset:
                self.canJump = True
                self.velocity = 2
    
    def draw(self):
        pygame.draw.rect(self.surface, (0, 0, 0),pygame.Rect(self.position_x, self.position_y, self.width, self.height
        ))

    def jump(self):
        if self.canJump == True:
            self.canJump = False
    
