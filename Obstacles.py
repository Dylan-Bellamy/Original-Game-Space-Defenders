import pygame

meteorOne = pygame.image.load(("Images//flaming_meteor.png"))
meteorTwo = pygame.image.load(("Images//meteor.png"))

    
class obstacle:   
    
    # Initializing attributes of class
    def __init__(self, image, type):
        self.image = image                           # First Arguement
        self.type = type                             # Second Arguement
        self.rect = self.image[self.type].get_rect() # Gets rectangle of image that going to be displayed
        self.rect.y = screenHight                    # Obstacles are created on the top of the screen

    # Update Function
    def update(self):
        self.rect.y -= gameSpeed            # Obstacle x-cord is being subtracted by the value of gameSpeed
        if self.rect.y < -self.rect.height:  # If the obstacle moves off the screen
            obstacles.pop()                 # Removes obstacle 

    # Blits image on to screen
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
        
class flamingMeteor(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.x = random.randint(25, 455)


class meteor(obstacle):
    
    # Initializing attributes of class
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.x = random.randint(25, 455)