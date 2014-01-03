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
gameover = pygame.image.load("Imagenes/gameover.png")
construir = 2
s=0
restart = False
saven=0
pygame.mixer.music.load("music1.mp3")
shoot=False
fondo = pygame.image.load("Imagenes/fondo.png")
fondo_pass = pygame.image.load("Imagenes/fondo_pass.png")
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
save = []
enemigos = []
main = 1
seleccion = 0
caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
var_password = [1, True, "", False]
if construir == 1:
    Novatin = Clases.Novatin((x/2),y)
if construir == 2:
    Novatin = Clases.Novatin(25,0)
#Seteamos la pantalla
screen = pygame.display.set_mode(size, FULLSCREEN)
cabeza = Clases.Extremidad(0,0,"cabeza",0)
brazo_i = Clases.Extremidad(0,0,"brazo_i",0)
brazo_d = Clases.Extremidad(0,0,"brazo_d",0)
menu = pygame.image.load('Imagenes/menu.png')
pygame.mixer.music.play(-1)

def texto(texto, posx, posy, tamano, color=(255, 255, 255)):
    fuente = pygame.font.Font("SF Pixelate.ttf", tamano)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

while 1:
    clock.tick(30)
    if main == 1:
        for event in pygame.event.get():
            if hasattr(event, 'key')==False:
                continue
            down = event.type == KEYDOWN
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            if event.key == K_SPACE:
                if seleccion == 0:
                    main = 0
                else:
                    main = 2
                s = 1
        key = pygame.key.get_pressed()
        if key[K_UP] == True:
            seleccion = 0
        if key[K_DOWN] == True:
            seleccion = 1
        screen.blit(menu, (0,0))
        if seleccion == 0:
            screen.blit(cabeza.image, (600,505))
        else:
            screen.blit(cabeza.image, (600,605))
        pygame.display.flip()
    elif main == 2:
        for event in pygame.event.get():
            if hasattr(event, 'key')==False:
                continue
            down = event.type == KEYDOWN
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            if event.key == K_SPACE:
                if var_password[3]:
                    var_password[3] = False
                    if var_password[0] == 37:
                        aux = ""
                        for j in range(len(var_password[2])-1):
                            aux += var_password[2][j]
                        var_password[2] = aux
                    elif var_password[0] == 38:
                        main = 3
#En esta parte va a ir la parte del save, una vez que hayan mas cosas que guardar                        
                    else:
                        var_password[2] += caracteres[(var_password[0]-1)]
                else:
                    var_password[3] = True
            if event.key == K_UP:
                if var_password[1]:
                    if var_password[0] > 12:
                        var_password[0] -= 12
                    elif var_password[0]%12 <= 6:
                        var_password[0] = 37
                    else:
                        var_password[0] = 38
                    var_password[1] = False
                else:
                    var_password[1] = True
            if event.key == K_DOWN:
                if var_password[1]:
                    if var_password[0] <= 24:
                        var_password[0] += 12
                    elif var_password[0] > 36:
                        var_password[0] = 6
                    elif var_password[0]%12 <= 6:
                        var_password[0] = 37
                    else:
                        var_password[0] = 38
                    var_password[1] = False
                else:
                    var_password[1] = True
            if event.key == K_RIGHT:
                if var_password[1]:
                    if var_password[0] <= 36:
                        if var_password[0]%12 == 0:
                            var_password[0] -= 11
                        else:
                            var_password[0] += 1
                    elif var_password[0] == 37:
                        var_password[0] = 38
                    else:
                        var_password[0] = 37
                    var_password[1] = False
                else:
                    var_password[1] = True
            if event.key == K_LEFT:
                if var_password[1]:
                    if var_password[0] <= 36:
                        if var_password[0]%12 == 1:
                            var_password[0] += 11
                        else:
                            var_password[0] -= 1
                    elif var_password[0] == 37:
                        var_password[0] = 38
                    else:
                        var_password[0] = 37
                    var_password[1] = False
                else:
                    var_password[1] = True
        screen.blit(fondo_pass, (0,0))
        for j in range(len(caracteres)):
            text, text_rect = texto(caracteres[j], 100 + j%12 * 80, 200 + j//12 * 100, 40)
            screen.blit(text, text_rect)
        if var_password[0] <= 36:
            screen.blit(cabeza.image, (55 + (var_password[0]-1)%12*80, 185 + (var_password[0]-1)//12 * 100))
        else:
            screen.blit(cabeza.image, (290 + (var_password[0] - 37) * 350, 520))
        for i in range(len(var_password[2])):
            password, password_rect = texto(var_password[2][i], 400 + 40 * i, 100, 40)
            screen.blit(password, password_rect)
        pygame.display.flip()
    else:
        shoot = False
        restart = False
        for event in pygame.event.get():
            if hasattr(event, 'key')==False:
                continue
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                directionx = 0
                speed = down*1
            elif event.key == K_r:
                restart = True
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
            saven=0
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
            manzanas.append(Clases.Manzana(480,y-120,False,True))
            manzanas.append(Clases.Manzana(520, y-130,False,False))
            camaespinas.append(Clases.Camaespina(950, y-360))
            nubes.append(Clases.Nubechica(600,50))
            nubes.append(Clases.NubeL(1050, 100))
            nubes.append(Clases.NubeM(1098, 100))
            nubes.append(Clases.NubeM(1146, 100))
            nubes.append(Clases.NubeR(1194, 100))
            save.append(Clases.Save(896,y-100,25,0))
            enemigos.append(Clases.Enemigo(700, 120))
            enemigos.append(Clases.Enemigo(450, 390))
            enemigos.append(Clases.Enemigo(550, 390))
            enemigos.append(Clases.Enemigo(128, 420))
            enemigos.append(Clases.Enemigo(x-30, y-155))
            enemigos.append(Clases.Enemigo(x-30, y-335))
            enemigos.append(Clases.Enemigo(x-30, y-515))
            saven=0
            construir = 0
        if Novatin.alive==True:
            Novatin.move(directionx,speed,plataformas,x)
            Novatin.jump(directionx,y,jump,plataformas)
            Novatin.shoot(shoot,directionx,plataformas,save,x)
            Novatin.ambiente(espinas,directionx,cabeza,brazo_d,brazo_i, manzanas,camaespinas)
        else:
            if Novatin.play == True:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                Novatin.play = False
            Novatin.revivir += 1
            if Novatin.revivir == 300 or restart == True:
                pygame.mixer.music.load("music1.mp3")
                pygame.mixer.music.play(-1)
                Novatin.revivir = 0
                Novatin.alive = True
                Novatin.play = True
                Novatin.rect.centerx = save[saven].savex
                Novatin.rect.centery = save[saven].savey
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
                manzanas.append(Clases.Manzana(480,y-120,False,True))
        muertes, muertes_rect = texto(str(Novatin.muertes), x-100, 20, 20)
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
        for camaespina in camaespinas:
            camaespina.trampa(Novatin,plataformas)
            screen.blit(camaespina.image, camaespina.rect)
        for plataforma in plataformas:
            screen.blit(plataforma.image, plataforma.rect)
        for sav in save:
            screen.blit(sav.image, sav.rect)
        for arbol in arboles:
            screen.blit(arbol.image, arbol.rect)
        for manzana in manzanas:
            manzana.trampa(Novatin,y)
            if manzana.alive == True:
                screen.blit(manzana.image, manzana.rect)
        for espina in espinas:
            espina.trampa(Novatin)
            if espina.alive == True:
                screen.blit(espina.image, espina.rect)
        for enemigo in enemigos:
            enemigo.move(plataformas,x)
            screen.blit(enemigo.image, enemigo.rect)
        if Novatin.alive==True:
            screen.blit(Novatin.image, Novatin.rect)
        if cabeza.alive:
            screen.blit(cabeza.image, cabeza.rect)
        if brazo_d.alive:
            screen.blit(brazo_d.image, brazo_d.rect)
        if brazo_i.alive:
            screen.blit(brazo_i.image, brazo_i.rect)
        screen.blit(muertes, muertes_rect)
        for bullet in Novatin.bullets:
            if bullet.alive==True:
                screen.blit(bullet.image, bullet.rect)
        if Novatin.alive == False:
            screen.blit(gameover,(x/2-400,(y-191)/2))
        pygame.display.flip()
    
