import pygame, sys, Clases, random
from pygame.locals import*
pygame.init()

#Variables
x = 1280
y = 720
size = (x,y)
black = (135,206,235)
clock = pygame.time.Clock()
directionx = 0 #Variable Binaria que indica direccion en x
jump = False
speed = 0
jspeed = 0
t = 0
construir = 2
s=0
shoot=False
fondo = pygame.image.load("Imagenes/fondo.png")
#Es una variable que indica la etapa a jugar
plataformas = []
#Aca se almacenan los objetos plataformas
espinas = []
#Aqui se almacenan los objetos espinas :)
arboles = []
#creo que de ahora en adelante se entiende la idea
manzanas = []
camaespinas = []
nubes = []
save = None
if construir == 1:
    Novatin = Clases.Novatin((x/2),y)
if construir == 2:
    Novatin = Clases.Novatin(25,0)
#Seteamos la pantalla
screen = pygame.display.set_mode(size, FULLSCREEN)
cabeza = Clases.Extremidad(0,0,"cabeza",0)
brazo_i = Clases.Extremidad(0,0,"brazo_i",0)
brazo_d = Clases.Extremidad(0,0,"brazo_d",0)

while 1:
    clock.tick(30)
    shoot = False
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
        if event.key == K_SPACE:
            if s==0:
                shoot=True
                s=1
            elif s==1:
                shoot=False
                s=0
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
        plataformas.append(Clases.PlataformaBaja(128, 95))
        plataformas.append(Clases.PlataformaBaja(384, 145))
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
        espinas.append(Clases.Espina(600, y-24, True))
        espinas.append(Clases.Espina(648,y-24, False))
        espinas.append(Clases.Espina(552,y-24, False))
        arboles.append(Clases.Arbol(500,y-75))
        manzanas.append(Clases.Manzana(480,y-120))
        manzanas.append(Clases.Manzana(520, y-130))
        camaespinas.append(Clases.Camaespina(950, y-360))
        nubes.append(Clases.Nubechica(600,50))
        nubes.append(Clases.NubeL(1050, 100))
        nubes.append(Clases.NubeM(1098, 100))
        nubes.append(Clases.NubeM(1146, 100))
        nubes.append(Clases.NubeR(1194, 100))
        save = Clases.Save(500,50)
        construir = 0
    if Novatin.alive==True:
        Novatin.move(directionx,speed,plataformas,x)
        Novatin.jump(directionx,y,jump,plataformas)
        Novatin.shoot(shoot,directionx,plataformas,x)
        Novatin.ambiente(espinas,directionx,cabeza,brazo_d,brazo_i)
    else:
        Novatin.revivir += 1
        if Novatin.revivir == 90:
            Novatin.revivir = 0
            Novatin.alive = True
            Novatin.rect.centerx = 25
            Novatin.rect.centery = 0
            cabeza.alive = False
            cabeza.roce = random.randint(-15,15)
            cabeza.jumpspeed = random.randint(10, 25)
            brazo_d.alive = False
            brazo_d.roce = random.randint(-15,15)
            brazo_d.jumpspeed = random.randint(10,25)
            brazo_i.alive = False
            brazo_i.roce = random.randint(-15,15)
            brazo_i.jumpspeed = random.randint(10,25)
            espinas.append(Clases.Espina(600,y-24, True))
    if cabeza.alive:
        cabeza.jump(y)
    if brazo_i.alive:
        brazo_i.jump(y)
        brazo_i.mover(y,0)
    if brazo_d.alive:
        brazo_d.mover(y,1)
        brazo_d.jump(y)
    screen.blit(fondo, (0,0))
    #primero el if para que novatin se mueva por enfrente de las plataformas
    for nube in nubes:
        screen.blit(nube.image, nube.rect)
    for plataforma in plataformas:
        screen.blit(plataforma.image, plataforma.rect)
    screen.blit(save.image, save.rect)
    for arbol in arboles:
        screen.blit(arbol.image, arbol.rect)
    for manzana in manzanas:
        screen.blit(manzana.image, manzana.rect)
    for camaespina in camaespinas:
        screen.blit(camaespina.image, camaespina.rect)
        """la cama de espinas debera ir originalmente por debajo de las plataformas
           ,la razon por la que esta sobre ellas es para ver ubicacion"""
    for espina in espinas:
        espina.trampa(Novatin)
        if espina.alive == True:
            screen.blit(espina.image, espina.rect)        
    if Novatin.alive==True:
        screen.blit(Novatin.image, Novatin.rect)
    if cabeza.alive:
        screen.blit(cabeza.image, cabeza.rect)
    if brazo_d.alive:
        screen.blit(brazo_d.image, brazo_d.rect)
    if brazo_i.alive:
        screen.blit(brazo_i.image, brazo_i.rect)
    for bullet in Novatin.bullets:
        if bullet.alive==True:
            screen.blit(bullet.image, bullet.rect)
    pygame.display.flip()
    
