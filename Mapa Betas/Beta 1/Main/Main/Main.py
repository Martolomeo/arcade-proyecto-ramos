import pygame, sys
from pygame.locals import*
pygame.init()

#Variables
x = 1280
y = 720
size = (x,y)
black = (0,0,0)
clock = pygame.time.Clock()

#Seteamos la pantalla
screen = pygame.display.set_mode(size, FULLSCREEN)

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if hasattr(event, 'key')==False:
            continue
        if event.key==K_ESCAPE:
            pygame.quit()
            sys.exit(0)
    screen.fill(black)
