#-----------------------------------------------------------------------------
# Name:        Assignment Template (assignment.py)
# Purpose:     A description of your program goes here.
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
#I think this project deserves a level XXXXXX because ...
#
#Features Added:
#   ...
#   ...
#   ...
#-----------------------------------------------------------------------------

import pygame
import random
import time


""" Set up the game and run the main game loop """
pygame.init()      # Prepare the pygame module for use
screenHeight = 480 # Screen Height
screenWidth = 480 # Screen Width
screen = pygame.display.set_mode((screenWidth, screenHeight))  # Initializing screen for display
    
clock = pygame.time.Clock()  #Force frame rate to be slower



from SpaceShip import Ship
from Obstacles import obstacle
from Obstacles import FlamingMeteor
from Obstacles import Meteor

explosion = pygame.image.load(("Images//explosion.png"))
backGround = pygame.image.load(("Images//background.jpg"))
backGround = pygame.transform.smoothscale(backGround, (screenWidth, screenHeight))
meteorOne = pygame.image.load(("Images//flaming_meteor.png"))
meteorTwo = pygame.image.load(("Images//meteor.png"))
IDLE = pygame.image.load(("Images//ship_4.png"))
RIGHT = pygame.image.load(("Images//ship_4.png"))
LEFT = pygame.image.load(("Images//ship_4.png"))
SHOT = pygame.image.load(("Images//laser2.png"))


def main():
    #-----------------------------Setup------------------------------------------------------#
    pygame.init()

    
    #-----------------------------Program Variable Initialization----------------------------#
    global xPosBackground, yPosBackground, gameSpeed
    gameSpeed = 5
    user = Ship()
    obstacles = []
    deathCount = 0
    xPosBackground = 0
    yPosBackground = 0


    #-----------------------------Main Game Loop---------------------------------------------#
    while True:
        
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
        def background():
            global xPosBackground, yPosBackground
            image_width = backGround.get_width()                                        # Gets and Sets width of Image
            screen.blit(backGround, (xPosBackground, yPosBackground))                   # Blits Image on screen
            


        #-----------------------------Game Logic---------------------------------------------#
        # Update your game objects and data structures here...
        screen.fill((0, 0, 0))
        
        # If amount obstacles is equal to 0 then it randomly picks a smallCactus, largeCactus, or bird and appends them to the obstactles list
        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(Meteor(meteorTwo))
            elif random.randint(0, 1) == 1:
                obstacles.append(FlamingMeteor(meteorOne))
            




         
            for obstacle in obstacles:
                print(obstacles, obstacle, screen)
                obstacle.draw(screen) # Draws Obstacles
                obstacle.update() # Updates Obstacle
                if user.ship_rect.colliderect(obstacle.rect):  # If the rectangle of the obstacle collides with the dinosaur's rectangle
                    
                    screen.blit(explosion, (xPos, yPos))
                 
                    pygame.time.delay(3000) # Stops game for 3 seconds
                    deathCount += 1         # Adds or equals one to deathCount
                    endscreen(deathCount)   # Starts Endscreen
        
        userInput = pygame.key.get_pressed() # Gets the state of all keyboard button
        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        
        background() # Calls background function
        
        clock.tick(30)  #Force frame rate to be slower
        pygame.display.update()
               
        user.draw(screen) # Draws spaceShip on screen
        user.update(userInput) # Updates spaceShip on screen when needed
        

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main()