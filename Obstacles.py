import pygame
import random

screenHeight2 = 360 # Screen Height
screenWidth2 = 720 # Screen Width
gameScreen = pygame.display.set_mode((screenWidth2, screenHeight2))  # Initializing screen for display


    
class obstacle:   
    global gameSpeed, obstacles
    gameSpeed = 3.5
    obstacles = []
    
    # Initializing attributes of class
    def __init__(self, image, typeIn):
        self.image = image                            # First Arguement
        self.type = typeIn                            # Second Arguement
        self.rect = self.image [self.typeIn].get_rect() # Gets rectangle of image that going to be displayed
        self.rect.x = screenWidth2                    # Obstacles are created on the Right of the screen

    # Update Function
    def update(self):
        self.rect.x -= gameSpeed            # Obstacle x-cord is being subtracted by the value of gameSpeed

    def onScreen(self):
        if self.rect.x <-self.rect.width:  # If the obstacle moves off the screen
            return False
        else:
            return True
    # Blits image on to screen
    def draw(self,gameScreen):
        gameScreen.blit(self.image[self.type], self.rect)
        
class Enemy(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 3)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 325)


class Enemy2(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 3)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 325)
        
class Enemy3(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 3)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 325)
        
        
class Enemy4(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 3)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 325)
    
