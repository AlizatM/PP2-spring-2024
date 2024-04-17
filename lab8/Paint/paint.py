import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
#settings
clock = pygame.time.Clock()
screen.fill((255,255,255))
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = BLACK
#image of eraser
eraser = pygame.image.load('eraser.png')
eraser = pygame.transform.scale(eraser, (70, 70))

def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))
#picking color:red,green and blue
def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0<=x<=40 and 0<=y<=40:
            return RED
        elif 40<x<=80 and 0<=y<=40:
            return GREEN
        elif 80<x<=120 and 0<=y<=40:
            return BLUE
        elif 700<=x<=770 and 0<=y<=40:
            return WHITE
        
    return color
#drawing with form that you choose
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0] and not (0<=x<=400 and 0<=y<=90):
        if mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), 27)
        if mode == 'rect':
            pygame.draw.rect(screen, color, (x, y, 40, 40), 4)
        
mode = 'circle'

while True:

    #working until pressing the button quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    for i in range(len(colors)):
        draw_rect(i)
    #settings of the form
    screen.blit(eraser, (700, 0))
    rect = pygame.draw.rect(screen, BLACK, (130, 0, 40, 40), 3)
    circle = pygame.draw.circle(screen, BLACK, (197, 20), 23, 3)
    

    pos = pygame.mouse.get_pos()
    print(mode)
    if rect.collidepoint(pos):
        mode = "rect"
    if circle.collidepoint(pos):
        mode = "circle"
    


    color = pick_color()
    painting(color)


    clock.tick(120)
    pygame.display.update()