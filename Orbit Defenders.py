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



from SpaceShip import spaceShip
from Obstacles import obstacle
from Obstacles import flamingMeteor
from Obstacles import meteor

explosion = pygame.image.load(("Images//explosion.png"))



def main():
    #-----------------------------Setup------------------------------------------------------#
    pygame.init()

    
    #-----------------------------Program Variable Initialization----------------------------#
    user = spaceShip()
    


    #-----------------------------Main Game Loop---------------------------------------------#
    while True:
        
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop


        #-----------------------------Game Logic---------------------------------------------#
        # Update your game objects and data structures here...
        screen.fill((0, 0, 0))
        
        
        userInput = pygame.key.get_pressed() # Gets the state of all keyboard button
        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        
        clock.tick(30)  #Force frame rate to be slower
        pygame.display.update()
               
        user.draw(screen) # Draws spaceShip on screen
        user.update(userInput) # Updates spaceShip on screen when needed
        

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main()