import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
# Settings
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
Collected_coins = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
#good = font.render("Good", True, BLACK)
#bad = font.render("Bad", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

display = pygame.display.set_mode((400,600))
display.fill(WHITE)
pygame.display.set_caption("Racer Game")

#Class pf enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), -10)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
      def draw(self, surface):
        surface.blit(self.image, self.rect)
#Class of Coins
class Coins(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 40), 0)
            if pygame.sprite.spritecollideany(self, enemies):
                self.rect.center = (random.randint(30,SCREEN_WIDTH-40),0)
      
      def draw(self, surface):
        surface.blit(self.image, self.rect)
#Class pf player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
                  
#Распределение по группам
P1 = Player()
E1 = Enemy()
C1 = Coins()

enemies = pygame.sprite.Group()
enemies.add(E1)
gold = pygame.sprite.Group()
gold.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


#Event на увелечение скорости каждые 2000 милисекунд
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

while True:
    # 
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #displaying number of scores and coins
    display.blit(background, (0,0))
    
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    collect = font_small.render("Coins: " + str(Collected_coins), True, BLACK)
    
    display.blit(scores, (10,10))
    display.blit(collect, (300,10))
    
    for entity in all_sprites:
        display.blit(entity.image, entity.rect)
        entity.move()
    for entity in gold:
        display.blit(entity.image, entity.rect)
        entity.move()
        
    #displaying the game over if player collides with enemy 
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          display.fill(RED)
          display.blit(game_over, (30,250))
          

          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    # removing the coins if it collides with player and showing the number of collected coins
    if pygame.sprite.spritecollide(P1, gold, True):
           Collected_coins += 1
           new_c = Coins()
           gold.add(new_c)        
              
    pygame.display.update()
    FramePerSec.tick(FPS)
