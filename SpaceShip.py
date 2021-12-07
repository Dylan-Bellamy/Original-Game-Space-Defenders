import pygame


IDLE = [pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//1.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//2.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//3.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//4.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//5.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//6.png"))]
RIGHT =[pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//1.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//2.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//3.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//4.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//5.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//6.png"))]
LEFT = [pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//1.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//2.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//3.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//4.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//5.png")),
        pygame.image.load(("Images//Ships//1//Pattern1//Red//Right//6.png"))]



class Ship(object):
    xPos = 120
    yPos = 240
    movementSpeed = 5
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
        
        self.step_index = 0                     # step_index starts at 0 and used to help animate Ship
        self.image = self.idle_img[0]  #[0]           # Initializing first image of spaceShip
        self.ship_rect = self.image.get_rect()  # Takes the rectangle of the spaceShip
        self.ship_rect.x = self.xPos            # Sets the x-cord of rectangle to the x-position
        self.ship_rect.y = self.yPos            # Sets the y-cord of rectangle to the y-position
        
    def update(self, userInput):
        
        if self.step_index >= 20:  # If step_index is greater or equal to 10
            self.step_index = 0    # Then reset step_index's value to 0
        
        # If user
        if userInput[pygame.K_UP] or userInput[pygame.K_w] and not self.ship_left:
            self.ship_idle = False     
            self.ship_right = False
            self.ship_left = True
            
        # If user 
        elif userInput[pygame.K_DOWN] or userInput[pygame.K_s] and not self.ship_right:
            self.ship_idle = False
            self.ship_right = True
            self.ship_left = False
            
        # If user hasn't pressed any key
        elif not (userInput[pygame.K_DOWN] or userInput[pygame.K_UP] or userInput[pygame.K_s] or userInput[pygame.K_w]):
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
        self.image = self.right_img[self.step_index // 10] # Cycles through RIGHT list of images every 5 steps
        self.ship_rect.y += self.movementSpeed           # Increase the y-position of the spaceShip
        self.yPos = self.ship_rect.y
        self.step_index += 1                             # Adds one to or makes step_index equal to one
        
    def left(self):
        self.image = self.left_img[self.step_index // 10] # Cycles through LEFT list of images every 5 steps    
        self.ship_rect.y -= self.movementSpeed           # Decrease the y-position of the spaceShip
        self.yPos = self.ship_rect.y
        self.step_index += 1                             # Adds one to or makes step_index equal to one
        
        
    def idle(self):
        self.image = self.idle_img[self.step_index // 10] # Cycles through IDLE list of images every 5 steps
        self.ship_rect.y += self.movementSpeedIdle       # The y-position of the spaceShip is stationary
        self.yPos = self.ship_rect.y
        self.step_index += 1                             # Adds one to or makes step_index equal to one
         
            
            
    # Blits image on to screen
    def draw(self, screen):
        screen.blit(self.image, (self.ship_rect.x, self.ship_rect.y))
            
#class Projectile(object):
        
        
