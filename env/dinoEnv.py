import pygame
from pygame.locals import *
from dinoPlayer import dinoPlayerClass
from obstacles import obstacleClass

import random
import math

pygame.init()

screenSize = (1000, 300)

screen = pygame.display.set_mode([screenSize[0], screenSize[1]])


dinoDimension = (30, 60)

y_init = screenSize[1] - dinoDimension[1]


dino = dinoPlayerClass(screen, 40, y_init, dinoDimension[0], dinoDimension[1])

obstacles = []

score: int
running: bool


def spawn_obstacle(speed, offset):
    obstacle = obstacleClass(screen, screenSize[0] + offset, y_init, dinoDimension[0], dinoDimension[1], speed)
    obstacles.append(obstacle)


def initGame():
    global score, running
    
    score = 0
    running = True

    spawn_obstacle(0.1, random.randint(100, 1000))
    spawn_obstacle(0.1, random.randint(500, 1500))

    main()


def isHittingDino(obstacle):
    dinoX = dino.get_x()
    dinoY = dino.get_y()
    dinoWidth = dino.get_width()
    dinoHeight = dino.get_height()

    obstacleX = obstacle.get_x()
    obstacleY = obstacle.get_y()
    obstacleWidth = obstacle.get_width()
    obstacleHeight = obstacle.get_height()

    if (obstacleX < dinoX + dinoWidth) and (obstacleX + obstacleWidth > dinoX) and (obstacleY < dinoY + dinoHeight) and (obstacleHeight + obstacleY > dinoY):
        print('collide')
        return True
    return False



def main():
    global score, running, obstacles
    speed = 0.1

    while running:
        speed += random.uniform(0.0000001, 0.000001)


        screen.fill((255, 255, 255))

        score = score + 0.001


        # Event handlers 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()
                if event.key == pygame.K_DOWN:
                    dino.down()

                    


                


        # Draw the objects on the screen

        dino.update()
        dino.draw()

        for obs in obstacles:
            obs.update()
            obs.draw()
            if isHittingDino(obs):
                running = False
            if obs.get_x() < 0 - obs.getWidth() :
                obstacles.remove(obs)
                del obs
                spawn_obstacle(speed, random.randint(30, 1000))

        # Update the scren frames
        pygame.display.update()
    
        #print(round(score))

    print(round(score))
    pygame.quit()

initGame()

