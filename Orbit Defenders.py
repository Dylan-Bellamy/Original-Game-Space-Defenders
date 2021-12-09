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
screenWidth = 720 # Screen Width
screen = pygame.display.set_mode((screenWidth, screenHeight))  # Initializing screen for display
    
clock = pygame.time.Clock()  #Force frame rate to be slower



from SpaceShip import Ship
from Obstacles import obstacle
from Obstacles import Enemy
from Obstacles import Enemy2

startBackGround = pygame.image.load(("Images//Start Background.jpg"))
startBackGround = pygame.transform.smoothscale(startBackGround, (screenWidth, screenHeight))
startButton = pygame.image.load(("Images//Start Button.png"))
startButton = pygame.transform.smoothscale(startButton, (240, 120))
exitButton = pygame.image.load(("Images//Exit Button.png"))
exitButton = pygame.transform.smoothscale(exitButton, (180, 100))
helpButton = pygame.image.load(("Images//Controls Button.png"))
helpButton = pygame.transform.smoothscale(helpButton, (180, 100))
explosion = [pygame.image.load(("Images//Explosions//Red//48px//1.png")),
             pygame.image.load(("Images//Explosions//Red//48px//2.png")),
             pygame.image.load(("Images//Explosions//Red//48px//3.png")),
             pygame.image.load(("Images//Explosions//Red//48px//4.png")),
             pygame.image.load(("Images//Explosions//Red//48px//5.png")),
             pygame.image.load(("Images//Explosions//Red//48px//6.png")),
             pygame.image.load(("Images//Explosions//Red//48px//7.png")),
             pygame.image.load(("Images//Explosions//Red//48px//8.png"))]
backGround = pygame.image.load(("Images//background.jpg"))
backGround = pygame.transform.smoothscale(backGround, (screenWidth, screenHeight))
meteorOne = [pygame.image.load(("Images//Ships//6//Pattern3//Yellow//Left//1.png")),
             pygame.image.load(("Images//Ships//6//Pattern3//Yellow//Left//2.png")),
             pygame.image.load(("Images//Ships//6//Pattern3//Yellow//Left//3.png")),
             pygame.image.load(("Images//Ships//6//Pattern3//Yellow//Left//4.png")),
             pygame.image.load(("Images//Ships//6//Pattern3//Yellow//Left//5.png")),
             pygame.image.load(("Images//Ships//6//Pattern3//Yellow//Left//6.png")),]
meteorTwo = [pygame.image.load(("Images//Ships//4//Pattern2//Blue//Left//1.png")),
             pygame.image.load(("Images//Ships//4//Pattern2//Blue//Left//2.png")),
             pygame.image.load(("Images//Ships//4//Pattern2//Blue//Left//3.png")),
             pygame.image.load(("Images//Ships//4//Pattern2//Blue//Left//4.png")),
             pygame.image.load(("Images//Ships//4//Pattern2//Blue//Left//5.png")),
             pygame.image.load(("Images//Ships//4//Pattern2//Blue//Left//6.png")),]


#SHOT = pygame.image.load[(("Images//Shot1.png")),
#                         (("Images//Shot2.png")),
#                         (("Images//Shot3.png")),
#                         (("Images//Shot4.png")),
#                         (("Images//Shot5.png"))]

def start():
    #-----------------------------Setup------------------------------------------------------#    
    pygame.init()
    #-----------------------------Program Variable Initialization----------------------------#  
    
    
    #-----------------------------Start Loop---------------------------------------------#  
    while True:
        
        #-----------------------------Event Handling-----------------------------------------#                  
            ev = pygame.event.poll()     # Look for any event
            if ev.type == pygame.QUIT:   # Window close button clicked?
                quit()           # Exit from program
              
            # Checks if the mouse has been clicked
            if ev.type == pygame.MOUSEBUTTONDOWN: 
              
                # If the button is clicked, then it will start the game (main())
                if 126 <= mouse[0] <= 356 and 118 <= mouse[1] <= 196:
                    main()
                
                #If the button is clicked, then it will exit the game (quit())
                if 272 <= mouse[0] <= 446 and 146 <= mouse[1] <= 328:
                    quit()
                
                #If the button is clicked, then it will bring up the controls screen (controls())
                if 38 <= mouse[0] <= 202 and 248 <= mouse[1] <= 328:
                    controls()
            
        #-----------------------------Start Screen Logic---------------------------------------------#                    
            screen.fill((0,0,0))  # Fills the screen with black
            screen.blit(startBackGround, (0,0))
        
            mouse = pygame.mouse.get_pos()  # Stores the (x,y) coordinates of the mouse into the variable
            print(mouse)
            #-----------------------------Drawing Everything-------------------------------------#
            screen.blit(startButton, (122,100))
            screen.blit(exitButton, (270,240))
            screen.blit(helpButton, (30,240))
            
            # Updates frames
            pygame.display.update()

def main():
    #-----------------------------Setup------------------------------------------------------#
    pygame.init()

    
    #-----------------------------Program Variable Initialization----------------------------#
    global xPosBackground, yPosBackground, gameSpeed, obstacles
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
            quit()                  #   ... leave game loop
        
        def background():
            global xPosBackground, yPosBackground
            image_width = backGround.get_width()                                        # Gets and Sets width of Image
            screen.blit(backGround, (xPosBackground, yPosBackground))                   # Blits Image on screen
            


        #-----------------------------Game Logic---------------------------------------------#
        # Update your game objects and data structures here...
        screen.fill((0, 0, 0))
        background() # Calls background function

        # If amount obstacles is equal to 0 then it randomly picks a smallCactus, largeCactus, or bird and appends them to the obstactles list
    
        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(Enemy(meteorOne))
            elif random.randint(0, 1) == 1:
                obstacles.append(Enemy2(meteorTwo))
            
        
        for obstacle in obstacles:
            obstacle.draw(screen) # Draws Obstacles
            
            obstacle.update() # Updates Obstacle
            if user.ship_rect.colliderect(obstacle.rect):  # If the rectangle of the obstacle collides with the dinosaur's rectangle
                obstacles.pop()                 # Removes obstacle
                #screen.blit(explosion, (xPos, yPos))
                pygame.time.delay(3000) # Stops game for 3 seconds
                deathCount += 1         # Adds or equals one to deathCount
                endscreen(deathCount)   # Starts Endscreen
        
        userInput = pygame.key.get_pressed() # Gets the state of all keyboard button
        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        
        
        clock.tick(30)  #Force frame rate to be slower
        pygame.display.update()
               
        user.draw(screen) # Draws spaceShip on screen
        user.update(userInput) # Updates spaceShip on screen when needed
        

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower
        #print(deathCount)



start()