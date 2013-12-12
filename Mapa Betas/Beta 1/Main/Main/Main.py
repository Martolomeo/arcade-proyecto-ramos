import pygame, sys, Clases
from pygame.locals import*
pygame.init()

#Variables
x = 1280
y = 720
size = (x,y)
black = (0,0,0)
clock = pygame.time.Clock()
construir = 1
#Es una variable binaria para saber si hay que construir una etapa o no
plataformas = []
#Aca se almacenan los objetos plataformas

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
    if construir == 1:
        screen.fill(black)
        plataformas.append(Clases.PlataformaAlta(0, 360))
        plataformas.append(Clases.PlataformaAlta(1024, 360))
        plataformas.append(Clases.PlataformaBaja(256, 540))
        plataformas.append(Clases.PlataformaBaja(768, 540))
        for i in range(len(plataformas)):
            screen.blit(plataformas[i].image, (plataformas[i].rect.centerx, plataformas[i].rect.centery))
        construir = 0
    pygame.display.flip()
    
