import pygame

IDLE = pygame.image.load(("Images//ship_4.png"))
RIGHT = pygame.image.load(("Images//ship_4.png"))
LEFT = pygame.image.load(("Images//ship_4.png"))
SHOT = pygame.image.load(("Images//laser2.png"))





class spaceShip(object):
    xPos = 220
    yPos = 360
    movementSpeed = 6
    movementSpeedIdle = 0
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
        
        self.image = self.idle_img              # Initializing first image of spaceShip
        self.ship_rect = self.image.get_rect()  # Takes the rectangle of the spaceShip
        self.ship_rect.x = self.xPos            # Sets the x-cord of rectangle to the x-position
        self.ship_rect.y = self.yPos            # Sets the y-cord of rectangle to the y-position
        
    def update(self, userInput):
        
        # If user
        if userInput[pygame.K_LEFT] or userInput[pygame.K_a] and not self.ship_left:
            self.ship_idle = False     
            self.ship_right = False
            self.ship_left = True
            
        # If user 
        elif userInput[pygame.K_RIGHT] or userInput[pygame.K_d] and not self.ship_right:
            self.ship_idle = False
            self.ship_right = True
            self.ship_left = False
            
        # If user hasn't pressed any key
        elif not (userInput[pygame.K_LEFT] or userInput[pygame.K_RIGHT] or userInput[pygame.K_d] or userInput[pygame.K_a]):
            self.ship_idle = True
            self.ship_right = False
            self.ship_left = False
            
        if self.ship_idle:
            self.idle()
        if self.ship_right:
            self.right()
        if self.ship_left:
            self.left()
            
    def right(self):
        self.image = self.right_img                      # Sets image of spaceShip to right image
        self.ship_rect.x += self.movementSpeed           # Increase the x-position of the spaceShip
        
    def left(self):
        
        self.image = self.left_img                       # Sets image of spaceShip to left image    
        self.ship_rect.x -= self.movementSpeed           # Decrease the x-position of the spaceShip
        
        
    def idle(self):
        self.image = self.idle_img                       # Sets image of spaceShip to idle image
        self.ship_rect.x += self.movementSpeedIdle       # The x-position of the spaceShip is stationary
         
            
            
    # Blits image on to screen
    def draw(self, screen):
            screen.blit(self.image, (self.ship_rect.x, self.ship_rect.y))
            
#class projectile(object):
        
        
