import pygame, sys, Clases
from pygame.locals import*
pygame.init()

#Variables
x = 1280
y = 720
size = (x,y)
black = (0,0,0)
clock = pygame.time.Clock()
directionx = 0 #Variable Binaria que indica direccion en x
jump = False
speed = 0
jspeed = 0
t = 0
construir = 2
#Es una variable que indica la etapa a jugar0
plataformas = []
#Aca se almacenan los objetos plataformas
if construir == 1:
    Novatin = Clases.Novatin((x/2),y)
if construir == 2:
    Novatin = Clases.Novatin(0,0)
#Seteamos la pantalla
screen = pygame.display.set_mode(size, FULLSCREEN)

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if hasattr(event, 'key')==False:
            continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT:
            directionx = 0
            speed = down*1
        elif event.key == K_LEFT:
            directionx = 1
            speed = down*1
        elif event.key==K_ESCAPE:
            pygame.quit()
            sys.exit(0)
    key = pygame.key.get_pressed()
    if key[K_UP] == True:
        jump = True
    elif key[K_UP] == False:
        jump = False
    #########################################################################
    screen.fill(black) #si se pone dentro del if entonces se vuelve negra una vez
    #########################################################################
    if construir == 1:
        plataformas.append(Clases.PlataformaAlta(128, y-180))
        plataformas.append(Clases.PlataformaAlta(x-128, y-180))
        plataformas.append(Clases.PlataformaBaja(384, y-45))
        plataformas.append(Clases.PlataformaBaja(x-384, y-45))
        construir = 0
    if construir == 2:
        plataformas.append(Clases.PlataformaBaja(128, 90))
        plataformas.append(Clases.PlataformaBaja(384, 180))
        plataformas.append(Clases.PlataformaAlta(768, 320))
        plataformas.append(Clases.PlataformaAlta(896, 0))
        plataformas.append(Clases.PlataformaBaja(512, 455))
        plataformas.append(Clases.PlataformaAlta(128, 620))
        plataformas.append(Clases.PlataformaBaja(896, y))
        plataformas.append(Clases.PlataformaBaja(x, y-90))
        plataformas.append(Clases.PlataformaBaja(896, y-180))
        plataformas.append(Clases.PlataformaBaja(x, y-270))
        plataformas.append(Clases.PlataformaBaja(896, y-360))
        plataformas.append(Clases.PlataformaBaja(x, y-450))
        construir = 0
    Novatin.move(directionx,speed,plataformas)
    Novatin.jump(y,jump,plataformas)
    #primero el if para que novatin se mueva por enfrente de las plataformas
    for i in range(len(plataformas)):
        screen.blit(plataformas[i].image, plataformas[i].rect)
    screen.blit(Novatin.image, Novatin.rect)
    pygame.display.flip()
    
