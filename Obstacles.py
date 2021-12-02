import pygame
import random


    
class obstacle:   
    
    # Initializing attributes of class
    def __init__(self, image, typeIn):
        self.image = image                           # First Arguement
        self.type = typeIn                             # Second Arguement
        self.rect = self.image[self.type].get_rect() # Gets rectangle of image that going to be displayed
        self.rect.y = screenHight                    # Obstacles are created on the top of the screen

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
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.x = random.randint(25, 455)


class Meteor(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.x = random.randint(25, 455)
    
#         # Blits image on to screen
#     def draw(self,screen):
#         print("Got into the draw")
#         screen.blit(self.image[self.type], self.rect)