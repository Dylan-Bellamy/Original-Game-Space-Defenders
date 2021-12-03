import pygame
import random

screenHeight = 480 # Screen Height
screenWidth = 480 # Screen Width
screen = pygame.display.set_mode((screenWidth, screenHeight))  # Initializing screen for display

    
class obstacle:   
    global gameSpeed
    gameSpeed = 5
    
    # Initializing attributes of class
    def __init__(self, image, typeIn):
        self.image = image                            # First Arguement
        self.type = typeIn                            # Second Arguement
        self.rect = self.image [self.typeIn].get_rect() # Gets rectangle of image that going to be displayed
        self.rect.x = screenWidth                    # Obstacles are created on the Right of the screen

    # Update Function
    def update(self):
        self.rect.y -= gameSpeed            # Obstacle x-cord is being subtracted by the value of gameSpeed
        if self.rect.y < -self.rect.height:  # If the obstacle moves off the screen
            obstacles.pop()                 # Removes obstacle 

    # Blits image on to screen
    def draw(self,screen):
        print("Got into the draw")
        screen.blit(self.image[self.type], self.rect)
        
class FlamingMeteor(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 5)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 455)


class Meteor(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 5)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 455)
    
