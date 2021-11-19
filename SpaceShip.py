import pygame


IDLE = pygame.image.load(("Images//ship_3.png"))
RIGHT = pygame.image.load(("Images//ship_3.png"))
LEFT = pygame.image.load(("Images//ship_3.png"))



class spaceShip:
    xPos = 360
    yPos = 900
    moveSpeed = 11.5
    userInput = pygame.key.get_pressed()    # Gets the state of all keyboard buttons
    
    # __init__ - Initializing attributes of class
    # self - Accesses the attritbutes of class
    def __init__(self):
        self.idle_img = IDLE
        self.right_img = RIGHT
        self.left_img = LEFT
        
        self.ship_idle = True  # Uses Idle Ship image
        self.ship_right = False
        self.ship_left = False 
        
        self.image = self.ship_img[0]           # Initializing first image of spaceShip
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
        
        
        
        
        
        
        
        
        
        
