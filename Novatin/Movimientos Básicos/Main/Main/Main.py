import pygame, math, sys, Clases
from pygame.locals import*
pygame.init()

#Variables
x = 1280
y = 720
size = (x,y)
black = (0,0,0)
Novatin = Clases.Novatin((x/2),y)
clock = pygame.time.Clock()
directionx = 0 #Variable Binaria que indica direccion en x
jump = False
speed = 0
jspeed=0
t = 0

#Pantalla
screen=pygame.display.set_mode(size, FULLSCREEN)

#Elementos Básicos
while 1:
    clock.tick(30)
    t += 1
    for event in pygame.event.get():
        if hasattr (event, 'key')==False:
            continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT:
            directionx = 0
            speed = down*1
        elif event.key == K_LEFT:
            directionx = 1
            speed = down*1
        elif event.key == K_ESCAPE:
            pygame.quit()
            sys.exit(0)
    key = pygame.key.get_pressed()
    if key[K_UP] == True:
        jump = True
    elif key[K_UP] == False:
        jump = False
    screen.fill(black)

    #Iniciamos la simulación
    Novatin.move(directionx,speed)
    Novatin.jump(y,jump)
    screen.blit(Novatin.image, Novatin.rect)
    pygame.display.flip()