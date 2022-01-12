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
screenHeight = 360 # Screen Height
screenWidth = 720 # Screen Width
screen = pygame.display.set_mode((screenWidth, screenHeight))  # Initializing screen for display

screenWidth2 = 720
screenHeight2 = 360
gameScreen = pygame.display.set_mode((screenWidth2, screenHeight2))  # Initializing gameScreen for display
    
clock = pygame.time.Clock()  #Force frame rate to be slower

startTicks = pygame.time.get_ticks()



from SpaceShip import Ship
from Obstacles import obstacle
from Obstacles import Enemy
from Obstacles import Enemy2
from Shoot import Shooting

fullLives = pygame.image.load(("Images//Full Hearts.png"))
fullLives = pygame.transform.smoothscale(fullLives, (120, 40))
twoLives = pygame.image.load(("Images//2 Hearts.png"))
twoLives = pygame.transform.smoothscale(twoLives, (120, 40))
oneLive = pygame.image.load(("Images//1 Heart.png"))
oneLive = pygame.transform.smoothscale(oneLive, (120, 40))
zeroLives = pygame.image.load(("Images//0 Hearts.png"))
zeroLives = pygame.transform.smoothscale(zeroLives, (120, 40))
startTitle = pygame.image.load(("Images//Title.png"))
startTitle = pygame.transform.smoothscale(startTitle, (480, 180))
startBackGround = pygame.image.load(("Images//Start Background.jpg"))
startBackGround = pygame.transform.smoothscale(startBackGround, (screenWidth, 480))
startButton = pygame.image.load(("Images//Start Button.png"))
startButton = pygame.transform.smoothscale(startButton, (240, 120))
exitButton = pygame.image.load(("Images//Exit Button.png"))
exitButton = pygame.transform.smoothscale(exitButton, (180, 100))
helpButton = pygame.image.load(("Images//Controls Button.png"))
helpButton = pygame.transform.smoothscale(helpButton, (185, 105))
backButton = pygame.image.load(("Images//Back Button.png"))
backButton = pygame.transform.smoothscale(backButton, (45, 45))
explosion = [pygame.image.load(("Images//Explosions//Red//64px//1.png")),
             pygame.image.load(("Images//Explosions//Red//64px//2.png")),
             pygame.image.load(("Images//Explosions//Red//64px//3.png")),
             pygame.image.load(("Images//Explosions//Red//64px//4.png")),
             pygame.image.load(("Images//Explosions//Red//64px//5.png")),
             pygame.image.load(("Images//Explosions//Red//64px//6.png")),
             pygame.image.load(("Images//Explosions//Red//64px//7.png")),
             pygame.image.load(("Images//Explosions//Red//64px//8.png"))]
backGround = pygame.image.load(("Images//background.jpg"))
backGround = pygame.transform.smoothscale(backGround, (screenWidth2, screenHeight2))
helpBackGround = pygame.image.load(("Images//Controls Background.jpg"))
helpBackGround = pygame.transform.smoothscale(helpBackGround,(screenWidth, screenHeight))
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



def end(deathCount):
    #-----------------------------Setup------------------------------------------------------#    
    pygame.init()
    
    #-----------------------------Program Variable Initialization----------------------------#  
    # Setting up fonts size
    global xPosBackground, yPosBackground
    xPosBackground = 0
    yPosBackground = 0 
    font = pygame.font.Font('freesansbold.ttf', 30)
    
    
    def background():
            global xPosBackground, yPosBackground
            image_width = backGround.get_width()                                        # Gets and Sets width of Image
            gameScreen.blit(backGround, (xPosBackground, yPosBackground))                   # Blits Image on screen
            screen.blit(backGround, (image_width + xPosBackground, yPosBackground))     # Behind that Image we blit another one, becuase with out it there would be a gab after running out of background
            if xPosBackground <= -image_width:                                  # If Background moves off screen
                screen.blit(backGround, (image_width + xPosBackground, yPosBackground)) # Another background is made
                xPosBackground = 0                                              # xPosBackground is reset to 0
            xPosBackground -= gameSpeed                                         # Background x-cord is being subtracted by the value of gameSpeed
    #-----------------------------Event Handling-----------------------------------------#
    #screen.fill((0,0,0))  # Fills the screen with black
    background()
    
    ev = pygame.event.poll()     # Look for any event
    if ev.type == pygame.QUIT:   # Window close button clicked?        
        quit()            # Exit for program
    if ev.type == pygame.KEYDOWN:
        main()
    #-----------------------------End Screen Logic---------------------------------------------# 
    # Rendering written font
    text = font.render("Press any Key to Restart", True, (0, 255, 255))  
    finalscore = font.render("How long you Lasted: " + str(seconds), True, (0, 255, 255))
    
    finalscoreRect = finalscore.get_rect()                                    # Takes Rectangle of "finalscore"
    finalscoreRect.center = (screenWidth // 2, screenHeight // 2 + 50)   # Centers Rectangle of the screen and changes the height 
    textRect = text.get_rect()                                      # Takes Rectangle of "text"
    textRect.center = (screenWidth // 2, screenHeight // 2)         # Centers Rectangle of the screen 
    
    #-----------------------------Drawing Everything-------------------------------------#
    finalTime = seconds
    screen.blit(text, textRect)  # Draws text 
    screen.blit(finalscore, finalscoreRect) # Draws finalscore
    pygame.display.update() # Updates display
    
    
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
                if 260 <= mouse[0] <= 466 and 120 <= mouse[1] <= 196:
                    main()
                
                #If the button is clicked, then it will exit the game (quit())
                if 410 <= mouse[0] <= 567 and 256 <= mouse[1] <= 318:
                    quit()
                
                #If the button is clicked, then it will bring up the controls screen (controls())
                if 165 <= mouse[0] <= 316 and 254 <= mouse[1] <= 320:
                    controls()
            
        #-----------------------------Start Screen Logic---------------------------------------------#                    
            screen.fill((0,0,0))  # Fills the screen with black
            screen.blit(startBackGround, (0,0))  # Prints StartBackGround
        
            mouse = pygame.mouse.get_pos()  # Stores the (x,y) coordinates of the mouse into the variable
            print(mouse)
            #-----------------------------Drawing Everything-------------------------------------#
            screen.blit(startButton, (245,100))  # Prints StartButton
            screen.blit(exitButton, (400,240))   # Prints ExitButton
            screen.blit(helpButton, (150,234))   # Prints HelpButton
            screen.blit(startTitle, (122,5))     # Prints StartTitle
            
            # Updates frames
            pygame.display.update()

def controls():
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
              
                #If the button is clicked, it will go back to the start screen (start())
                if 10 <= mouse[0] <= 55 and 305 <= mouse[1] <= 350:
                    start()
            
        #-----------------------------Start Screen Logic---------------------------------------------#                    
            screen.fill((0,0,0))  # Fills the screen with black
            screen.blit(helpBackGround, (0,0))
            screen.blit(backButton, (10, 305))
        
            mouse = pygame.mouse.get_pos()  # Stores the (x,y) coordinates of the mouse into the variable
            print(mouse)
            #-----------------------------Drawing Everything-------------------------------------#
            
            # Updates frames
            pygame.display.update()

def main():
    #-----------------------------Setup------------------------------------------------------#
    pygame.init()

    
    #-----------------------------Program Variable Initialization----------------------------#
    global xPosBackground, yPosBackground, gameSpeed, obstacles, points, seconds
    gameSpeed = 3.5
    user = Ship()
    bullet = Shooting(user.xPos, user.yPos)
    obstacles = []
    deathCount = 0
    xPosBackground = 0
    yPosBackground = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    seconds = (pygame.time.get_ticks() - startTicks) / 1000
    

    #-----------------------------Main Game Loop---------------------------------------------#
    while True:
        
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            quit()                  #   ... leave game loop
        
        userInput = pygame.key.get_pressed() # Gets the state of all keyboard button
        
        def score():
            global points, gameSpeed, seconds
            seconds = (pygame.time.get_ticks() - startTicks) / 1000 
            if seconds % 60 == 0:
                    gameSpeed += 0.25    # gameSpeed is increased by 0.25

            text = font.render("Seconds Alive: " + str(seconds), True, (255, 255, 255)) # Display "Seconds Alive" and number of points on screen
            textRect = text.get_rect()        # Gets cooridinates of text
            textRect.center = (605, 30)       # Sets text rectangle to the top corner of the screen
            gameScreen.blit(text, textRect)       # Blits seconds Alive on screen
        
        def background():
            global xPosBackground, yPosBackground
            image_width = backGround.get_width()                                        # Gets and Sets width of Image
            gameScreen.blit(backGround, (xPosBackground, yPosBackground))                   # Blits Image on screen
            screen.blit(backGround, (image_width + xPosBackground, yPosBackground))     # Behind that Image we blit another one, becuase with out it there would be a gab after running out of background
            if xPosBackground <= -image_width:                                  # If Background moves off screen
                screen.blit(backGround, (image_width + xPosBackground, yPosBackground)) # Another background is made
                xPosBackground = 0                                              # xPosBackground is reset to 0
            xPosBackground -= gameSpeed                                         # Background x-cord is being subtracted by the value of gameSpeed
            


        #-----------------------------Game Logic---------------------------------------------#
        # Update your game objects and data structures here...
        gameScreen.fill((0, 0, 0))
        background() # Calls background function
        
        user.draw(gameScreen) # Draws spaceShip on screen
        user.update(userInput) # Updates spaceShip on screen when needed
        
        # If deathCount is equal to 0 print fullLives on screen
        if deathCount == 0:
            gameScreen.blit(fullLives, (10, 10))
            
        # If deathCount is equal to 1 print twoLives on screen
        if deathCount == 1:
            gameScreen.blit(twoLives, (10, 10))
            
        # If deathCount is equal to 2 print oneLive on screen
        if deathCount == 2:
            gameScreen.blit(oneLive, (10, 10))
            
        # If deathCount is equal to 3 print zeroLives on screen
        if deathCount == 3:
            gameScreen.blit(zeroLives, (10, 10))
        
        # If amount obstacles is equal to 0 then it randomly picks an enemy and appends them to the obstactles list
        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(Enemy(meteorOne))
            elif random.randint(0, 1) == 1:
                obstacles.append(Enemy2(meteorTwo))
        
        # If amount obstacles is equal to 1 then it randomly picks an enemy and appends them to the obstactles list
        if len(obstacles) == 1:
            if random.randint(0, 1) == 0:
                obstacles.append(Enemy(meteorOne))
            elif random.randint(0, 1) == 1:
                obstacles.append(Enemy2(meteorTwo))
        
        # If seconds is equal to 180 / 180 seconds / 3 minutes, then it randomly picks an enemy and appends them to the obstactles list
        if seconds >= 180:      
            if len(obstacles) == 2:
                if random.randint(0, 1) == 0:
                    obstacles.append(Enemy(meteorOne))
                elif random.randint(0, 1) == 1:
                    obstacles.append(Enemy2(meteorTwo))
            
        
        for obstacle in obstacles:
            obstacle.draw(gameScreen) # Draws Obstacles
            
            obstacle.update() # Updates Obstacle
            if deathCount == 3:
                end(deathCount)   # Starts Endscreen
            if (not obstacle.onScreen()):
                obstacles.remove(obstacle)
            if user.ship_rect.colliderect(obstacle.rect):  # If the rectangle of the obstacle collides with the Ship's rectangle
                obstacles.remove(obstacle)                 # Removes obstacle
                
                gameScreen.blit(explosion[3], (user.xPos+25, user.yPos-20)) # Makes an explosion when collison is present
                deathCount += 1         # Adds or equals one to deathCount
            
            if bullet.rect.colliderect(obstacle.rect):  # If the rectangle of the obstacle collides with the Ship's rectangle
                obstacles.remove(obstacle)                 # Removes obstacle
                
                gameScreen.blit(explosion[3], (bullet.rect.x+25, bullet.rect.y-20)) # Makes an explosion when collison is present
                
        if userInput[pygame.K_SPACE]: # If user presses spacebar on keyboard
            bullet.rect.x = user.xPos
            bullet.rect.y = user.yPos
            
        bullet.draw(gameScreen)  # Draws Bullet on screen
        bullet.update() # Runs Update Code   
            #if (not bullet.onScreen2()):   # If obstacle is off screen
               # bullet.remove() # Removes bullet
        
        
        
        
        userInput = pygame.key.get_pressed() # Gets the state of all keyboard button
        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        
        score()  # Starts score function
        
        clock.tick(30)  #Force frame rate to be slower
        pygame.display.update()
               
        
        
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        
        #print(deathCount)



start()