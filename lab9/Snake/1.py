import pygame
import random, time
#settings
pygame.init()
running = True
Widht, Height = 1200, 800
Red = (255, 0, 0)
Black = (0, 0, 0)
Blue = (0, 0, 255)
green = (0, 255, 0)
white = (255,255,255)

Level = 0
font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, Black)
screen = pygame.display.set_mode((Widht, Height))
pygame.display.set_caption("Snake Game2")
clock = pygame.time.Clock()

#Collisions between snake and walls
def check_collision(x,y):
    global running
    if x >= Widht or x < 0 or y >= Height or y < 40:
        time.sleep(0.5)
        screen.fill(Red)
        screen.blit(game_over, (550,400))
        scoretag = font.render("Your score: "+str(s.score), True, Black)
        screen.blit(scoretag, (550,500))

        pygame.display.update()

        time.sleep(2)
        
        pygame.quit()

# Snake object 
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 600
        self.y = 400
        self.dx = 3
        self.dy = 3
        self.score = 0
        self.a = 5 
        self.direction = "right" 
        self.directionsnake = {"left" : False, "right" : True, "up" : True, "down" : True}
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.segments = [(self.x, self.y)]    
    # Keyboard pressed
    def press(self):
        pressed_keys = pygame.key.get_pressed()
        directions = {pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right', pygame.K_UP: 'up', pygame.K_DOWN: 'down'}
        for key, direction in directions.items():
            if pressed_keys[key]:
                if direction == "left" and self.directionsnake["left"]:
                    self.direction = direction
                    self.directionsnake = {"left" : True, "right" : False, "up" : True, "down" : True}
                elif direction == "right" and self.directionsnake["right"]:
                    self.direction = direction
                    self.directionsnake = {"left" : False, "right" : True, "up" : True, "down" : True}
                elif direction == "up" and self.directionsnake["up"]:
                    self.direction = direction
                    self.directionsnake = {"left" : True, "right" : True, "up" : True, "down" : False}
                elif direction == "down" and self.directionsnake["down"]:
                    self.direction = direction
                    self.directionsnake = {"left" : True, "right" : True, "up" : False, "down" : True}

    def move(self, add = 1, start = 0):
        global Level
        head_x, head_y = self.segments[0]
        if self.direction == 'left':
            head_x -= self.dx * add
        elif self.direction == 'right':
            head_x += self.dx * add
        elif self.direction == 'up':
            head_y -= self.dy * add
        elif self.direction == 'down':
            head_y += self.dy * add
        self.rect = pygame.Rect(head_x, head_y, 10,10)
        self.segments.insert(0, (head_x, head_y))

        if not pygame.sprite.spritecollide(self, fruits, False):
            self.segments.pop()
        else:
            self.score += add*start
            if s.score % self.a == 0: # Upgrading level
                s.dx += 0.4
                s.dy += 0.4
                self.a += 10
                Level += 1

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, Red, (segment[0], segment[1], 10, 10))
# Handler
def handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
# Fruits object
class Fruits(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__()
        self.x = random.randrange(10, 1190, 50)
        self.y = random.randrange(40, 790, 50)
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.identify = id
        self.created_time = time.time()
    def born(self):
        if self.identify == 1:
            pygame.draw.rect(screen, Blue, self.rect)
        elif self.identify == 2:
            pygame.draw.rect(screen, green, self.rect)
        elif self.identify == 3:
            pygame.draw.rect(screen, Red, self.rect)
        elif self.identify == 4:
            pygame.draw.rect(screen, Black, self.rect)


    


s = Snake()
f1 = Fruits(1)
f2 = Fruits(2)
f3 = Fruits(3)
f4 = Fruits(4)
fruits = pygame.sprite.Group()
fruits.add(f1, f2, f3, f4)

# Game cycle
while running:
    clock.tick(120)
    running = handler()
    screen.fill(white)
    pygame.draw.aaline(screen, Red, [0, 40], [1200, 40])
    
    scoretag = font.render("Score: "+str(s.score), True, (0, 255, 0))
    leveltag = font.render("Level: "+str(Level), True, (0, 255, 0))
    screen.blit(scoretag, (10,10))
    screen.blit(leveltag, (1100, 10))

    

    for entity in fruits:
        entity.born()

    s.press()
    s.move()
    if time.time() - f4.created_time >= 5:  # Если прошло 5 секунд
            f4.kill()
            f4 = Fruits(4)
            fruits.add(f4)
    if pygame.sprite.spritecollide(s, fruits, False):
        for fruct in pygame.sprite.spritecollide(s, fruits, False):
            if fruct.identify == 1:
                s.move(1, 1)
                f1.kill()
                f1 = Fruits(1)
                fruits.add(f1)
            elif fruct.identify == 2:
                s.move(2, 1)
                f2.kill()
                f2 = Fruits(2)
                fruits.add(f2)
            elif fruct.identify == 3:
                s.move(3, 1)
                f3.kill()
                f3 = Fruits(3)
                fruits.add(f3)
            elif fruct.identify == 4:
                s.move(5, 1)
                f4.kill()
                f4 = Fruits(4)
                fruits.add(f4)
    

    s.draw()

    check_collision(s.segments[0][0], s.segments[0][1])

    pygame.display.update()




pygame.quit()