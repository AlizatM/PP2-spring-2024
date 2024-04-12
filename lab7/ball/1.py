import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
x = 300
y = 300
s = 20
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
        screen.fill((255, 255, 255))
        circle = pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - 50 > 0:
            y -= s
        if pressed[pygame.K_DOWN] and y + 50 < 600:
            y += s
        if pressed[pygame.K_LEFT] and x - 50 > 0:
            x -= s
        if pressed[pygame.K_RIGHT] and x + 50 < 600:
            x += s
        
        
        clock.tick(60)
        pygame.display.flip()