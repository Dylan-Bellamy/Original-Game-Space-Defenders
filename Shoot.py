import pygame
import random

screenHeight2 = 360 # Screen Height
screenWidth2 = 720 # Screen Width
gameScreen = pygame.display.set_mode((screenWidth2, screenHeight2))  # Initializing screen for display

SHOT = [pygame.image.load(("Images//Shot1.png")),
        pygame.image.load(("Images//Shot2.png")),
        pygame.image.load(("Images//Shot3.png")),
        pygame.image.load(("Images//Shot4.png")),
        pygame.image.load(("Images//Shot5.png"))]

class Shooting():
    bulletSpeed = 12.5
    step_index = 0                     # step_index starts at 0 and used to help animate Ship
    
    def __init__(self, userXpos, userYpos):
        self.image = SHOT[0]
        self.rect = self.image.get_rect()
        self.rect.x = userXpos
        self.rect.y = userYpos
    def update(self):
        self.image = self.image[self.step_index // 5] # Cycles through SHOT list of images every 5 steps
        self.rect.x += bulletSpeed   # Bullet's x-cord is being added on by bulletSpeed
        if self.step_idex == 26:
            self.step_index += 0     # step_index doesn't change
        else:
            self.step_index += 1     # Adds one to or makes step_index equal to one
        
        
    def onScreen2(self):
        if self.rect.x <-self.rect.width:  # If the obstacle moves off the screen
            return False
        else:
            return True
    # Blits image on to screen
    def draw(self,gameScreen):
        gameScreen.blit(self.image, self.rect)