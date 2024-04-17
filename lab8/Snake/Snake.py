import pygame
import random, time

pygame.init()

Widht, Height = 900, 800
Black = (0, 0, 0)
Blue = (0, 0, 255)
Level = 0
font = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, Black)
screen = pygame.display.set_mode((Widht, Height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

# Handler
def handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

# Class of snake 
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 600
        self.y = 400
        self.dx = 5
        self.dy = 5
        self.score = 0
        self.a = 5 # Speed 
        self.direction = "RIGHT" # Basic directon
        self.directionsnake = {"LEFT" : False, "RIGHT" : True, "UP" : True, "DOWN" : True}
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.segments = [(self.x, self.y)]    
    # Keyboard pressed
    def keyboard(self):
        pressed_keys = pygame.key.get_pressed()
        directions = {pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT', pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN'}
        for key, direction in directions.items():
            if pressed_keys[key]:
                if direction == "LEFT" and self.directionsnake["LEFT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : True, "RIGHT" : False, "UP" : True, "DOWN" : True}
                elif direction == "RIGHT" and self.directionsnake["RIGHT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : False, "RIGHT" : True, "UP" : True, "DOWN" : True}
                elif direction == "UP" and self.directionsnake["UP"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : True, "RIGHT" : True, "UP" : True, "DOWN" : False}
                elif direction == "DOWN" and self.directionsnake["DOWN"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : True, "RIGHT" : True, "UP" : False, "DOWN" : True}

    def move_snake(self):
        global Level
        head_x, head_y = self.segments[0]
        if self.direction == 'LEFT':
            head_x -= self.dx
        elif self.direction == 'RIGHT':
            head_x += self.dx
        elif self.direction == 'UP':
            head_y -= self.dy
        elif self.direction == 'DOWN':
            head_y += self.dy
        self.rect = pygame.Rect(head_x, head_y, 10,10)
        self.segments.insert(0, (head_x, head_y))

        if not pygame.sprite.spritecollide(self, fruits, False):
            self.segments.pop()
        else:
            self.score += 1
            if s.score % self.a == 0: # Upgrading level
                s.dx += 0.4
                s.dy += 0.4
                self.a += 10
                Level += 1

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, (255, 0, 0), (segment[0], segment[1], 10, 10))

# Fruits object
class Fruits(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randrange(10, 890, 50)
        self.y = random.randrange(61, 790, 50)
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
    def born(self):
        pygame.draw.rect(screen, Blue, self.rect)

# Checking collisions between snake and walls
def check_collision(x,y):
    global running
    if x >= Widht or x < 0 or y >= Height or y < 60:
        time.sleep(0.5)
        screen.fill((255,255,255))
        screen.blit(game_over, (360,300))
        scoretag = font.render("Your score:"+str(s.score), True, Black)
        screen.blit(scoretag, (360,350))

        pygame.display.update()

        time.sleep(2)
        
        pygame.quit()

s = Snake()
f = Fruits()
fruits = pygame.sprite.Group()
fruits.add(f)

# Game cycle
while running:
    clock.tick(60)
    running = handler()
    screen.fill(Black)
    pygame.draw.aaline(screen, Blue, [0, 60], [900, 60])
    
    scoretag = font.render("Score: "+str(s.score), True, (0, 255, 0))
    leveltag = font.render("Level: "+str(Level), True, (0, 255, 0))
    screen.blit(scoretag, (10,10))
    screen.blit(leveltag, (750, 10))

    for entity in fruits:
        entity.born()

    s.keyboard()
    s.move_snake()

    if pygame.sprite.spritecollide(s, fruits, True):
        f = Fruits()
        fruits.add(f)

    s.draw()

    check_collision(s.segments[0][0], s.segments[0][1])

    pygame.display.update()

pygame.quit()