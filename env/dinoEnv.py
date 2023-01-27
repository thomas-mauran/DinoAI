import pygame
from pygame.locals import *
from dinoPlayer import dinoPlayerClass
from obstacles import obstacleClass

pygame.init()

screenSize = (1000, 300)

screen = pygame.display.set_mode([screenSize[0], screenSize[1]])


dinoDimension = (30, 60)

y_init = screenSize[1] - dinoDimension[1]

dino = dinoPlayerClass(screen, 40, y_init, dinoDimension[0], dinoDimension[1])

obstacle = obstacleClass(screen, 400, y_init, dinoDimension[0], dinoDimension[1], 0.1)

current_objects = []
current_objects.append(dino)
current_objects.append(obstacle)

def main():
    score = 0

    running = True
    while running: 
        screen.fill((255, 255, 255))

        score = score + 0.001

        # Event handlers 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()


                


        # Draw the objects on the screen
        for obj in current_objects:
            obj.update()
            obj.draw()
        
        if len(current_objects) > 1:    
            if current_objects[1].getPos_x() < 0 - current_objects[1].getWidth() :
                del current_objects[1]
        # Update the scren frames
        pygame.display.update()
        #print(round(score))

    pygame.quit()

main()

