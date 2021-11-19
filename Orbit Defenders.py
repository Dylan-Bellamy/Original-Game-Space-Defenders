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
#from SpaceShip import spaceShip
IDLE = pygame.image.load(("Images//ship_3.png"))
RIGHT = pygame.image.load(("Images//ship_3.png"))
LEFT = pygame.image.load(("Images//ship_3.png"))



class spaceShip:
    xPos = 360
    yPos = 900
    moveSpeed = 11.5
    #userInput = pygame.key.get_pressed()    # Gets the state of all keyboard buttons
    
    # __init__ - Initializing attributes of class
    # self - Accesses the attritbutes of class
    def __init__(self):
        self.idle_img = IDLE
        self.right_img = RIGHT
        self.left_img = LEFT
        
        self.ship_idle = True  # Uses Idle Ship image
        self.ship_right = False
        self.ship_left = False 
        
        self.image = self.idle_img         # Initializing first image of spaceShip
        self.ship_rect = self.image.get_rect()  # Takes the rectangle of the spaceShip
        self.ship_rect.x = self.xPos            # Sets the x-cord of rectangle to the x-position
        self.ship_rect.y = self.yPos            # Sets the y-cord of rectangle to the y-position
        
    def update(self, userInput):
        if self.ship_idle:
            self.idle()
        if self.ship_right:
            self.right()
        if self.ship_left:
            self.left()
            
        # If user 
        if userInput[pygame.K_LEFT] and not self.ship_left:
            self.ship_idle = False     
            self.ship_right = False
            self.ship_left = True
            
        # If user 
        elif userInput[pygame.K_RIGHT] and not self.ship_right:
            self.ship_idle = False
            self.ship_right = True
            self.ship_left = False
            
        # If user hasn't pressed any 
        elif not (userInput[pygame.K_LEFT] or userInput[pygame.K_RIGHT]):
            self.ship_idle = True
            self.ship_right = False
            self.ship_left = False
            
            
            
            
            
            
        # Blits image on to screen
        def draw(self, screen):
            creen.blit(self.image, (self.ship_rect.x, self.ship_rect.y))
            
def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    screenHeight = 1000 # Screen Height
    screenWidth = 720 # Screen Width
    screen = pygame.display.set_mode((screenWidth, screenHeight))  # Initializing screen for display
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    
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


        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        screen.fill((0, 0, 0))

               
        user.draw(screen) # Draws dinosaur on screen
        user.update(userInput) # Updates dinosaur on screen when needed
        

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main()