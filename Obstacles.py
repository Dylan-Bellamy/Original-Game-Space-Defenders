import pygame
import random

screenHeight = 480 # Screen Height
screenWidth = 720 # Screen Width
screen = pygame.display.set_mode((screenWidth, screenHeight))  # Initializing screen for display

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
    
class obstacle:   
    global gameSpeed, obstacles
    gameSpeed = 5
    obstacles = []
    
    # Initializing attributes of class
    def __init__(self, image, typeIn):
        self.image = image                            # First Arguement
        self.type = typeIn                            # Second Arguement
        self.rect = self.image [self.typeIn].get_rect() # Gets rectangle of image that going to be displayed
        self.rect.x = screenWidth                    # Obstacles are created on the Right of the screen

    # Update Function
    def update(self):
        self.rect.x -= gameSpeed            # Obstacle x-cord is being subtracted by the value of gameSpeed
        if self.rect.x < -self.rect.width:  # If the obstacle moves off the screen
            obstacles.pop()                 # Removes obstacle 

    # Blits image on to screen
    def draw(self,screen):
        screen.blit(self.image[self.type], self.rect)
        
class Enemy(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 5)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 455)


class Enemy2(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.image = image   
        self.typeIn = random.randint(0, 5)
        super().__init__(image, self.typeIn)
        self.rect.y = random.randint(25, 455)
    
