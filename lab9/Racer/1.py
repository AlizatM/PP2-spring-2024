#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FramePerSec = pygame.time.Clock()
 
#Creating colors
Blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
White = (255, 255, 255)
 
#Other Variables for use in the program
Widht = 400
height = 600
speed = 3
score = 0
COINS = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
screen = pygame.display.set_mode((400,600))
screen.fill(White)
pygame.display.set_caption("Game")

#Появление врагов
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Widht-40), 0)  
 
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, Widht - 40), 0)

# Появление монет           
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Widht-40), 0)  
 
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, Widht - 40), 0)      
# Появление новой монеты
class Blackcoin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("blackcoin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Widht-40), 0)  
 
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, Widht - 40), 0) 

 
#УПравление игркоом
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left >= 30:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right <= 370:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
Coin1 = Coin()
Coin2 = Blackcoin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# coin points
coin_add = pygame.sprite.Group()
blackcoin_add = pygame.sprite.Group()

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 10000)
 
#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get():
        #if event.type == INC_SPEED:
              #speed += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    screen.blit(background, (0,0))
    scores = font_small.render("Score: " + str(score), True, black)
    screen.blit(scores, (10,10))
    collect = font_small.render("Coins: " + str(COINS), True, black)
    screen.blit(collect, (280,10))
    #Moves and Re-draws all Sprit
    # РАБОТА С СПРАЙТАМИ И ВЫВОД
    if score >= 40:
        speed = 10
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    for entity in coin_add:
        screen.blit(entity.image, entity.rect)
        entity.move()
    for entity in blackcoin_add:
        screen.blit(entity.image, entity.rect)
        entity.move()
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          screen.fill(red)
          screen.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
    coin_add.add(Coin1)
    # КОЛЛИЗИЯ С МОНЕТОЙ
    if pygame.sprite.spritecollideany(P1, coin_add):
          
          for entity in coin_add:
                entity.kill() 
                COINS += 2
                Coin1 = Coin()
    blackcoin_add.add(Coin2)
    # КОЛЛИЗИЯ С МОНЕТОЙ 2
    if pygame.sprite.spritecollideany(P1, blackcoin_add):
          for entity in blackcoin_add:
                entity.kill() 
                COINS += 5
                Coin2 = Blackcoin()
    pygame.display.update()
    FramePerSec.tick(120)