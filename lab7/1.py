import pygame
from datetime import datetime

pygame.init()

widht, height = 829, 750
center = widht/2, height/2

screen = pygame.display.set_mode((widht, height))

clock = pygame.time.Clock()
mickey = pygame.image.load('mickey.png')
left = pygame.image.load('left-hand.png')
right = pygame.image.load('right-hand.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    time = datetime.now()
    seconds = (time.second / 60) * 360
    minutes = (time.minute / 60) * 360 + (time.second / 60) * (360 / 60)

    rotateleft = pygame.transform.rotate(left, -seconds)
    left_rect = rotateleft.get_rect(center=center)
    rotateright = pygame.transform.rotate(right, -minutes)
    right_rect = rotateright.get_rect(center=center)

    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))
    screen.blit(rotateleft, left_rect)
    screen.blit(rotateright, right_rect)
    pygame.display.flip()