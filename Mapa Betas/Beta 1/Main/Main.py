import pygame, sys, Clases, random, Maps, Password

from pygame.locals import*

def texto(texto, posx, posy, tamano, color=(255, 255, 255)):
    fuente = pygame.font.Font("SF Pixelate.ttf", tamano)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

def Go():
    #auxiliares del save
    auxi=0
    auxj=0
    deactivate=False
    first=False
    #termino de variables auxiliares del save
    pygame.init()
    #Variables para la panalla y seeo de esa
    x = 1024
    y = 768
    size = (x,y)
    black = (135,206,235)
    screen = pygame.display.set_mode(size)
    #Imagenes
    menu = pygame.image.load("Imagenes/menu.png")
    fondo = pygame.image.load("Imagenes/fondo.png")
    fondo_pass = pygame.image.load("Imagenes/fondo_pass.png")
    gameover = pygame.image.load("Imagenes/gameover.png")
    #Musica
    pygame.mixer.music.load("Music/music1.mp3")
    pygame.mixer.music.play(-1)
    #Clock
    clock = pygame.time.Clock()
    #Variables de Novatin
    s = 0
    cabeza = Clases.Extremidad(0,0,"cabeza")
    brazo_i = Clases.Extremidad(0,0,"brazo_i")
    brazo_d = Clases.Extremidad(0,0,"brazo_d")
    saven = 0
    xi = 40
    yi = y-40
    di = 0
    mi = False
    jefe = False
    jefe2 = False
    Novatin = Clases.Novatin(xi,yi,di,mi)
    Vidas = 10
    Creditos = 1
    cb = True
    firstchange = True
    secondchange = True
    thirdchange = True
    fourthchange = True
    #Portada
    main = 1
    seleccion = 0
    #Mapas
    construir = 0
    cambiar = False
    Mapa = []
    #Inicio etapas
    for i in(range(15)):
        Mapa.append(Maps.Mapa(x,y,"Levels/level"+str(i+1)+".txt",i+1))
    #Fin etapas
    for mapa in Mapa:
        mapa.cambia(Mapa)

    while 1:
        if construir == 4 and jefe2==False:
            jefe = True
            jefe2 = True
        if jefe == True:
            #pygame.mixer.music.load("Music/music2.mp3")
            #pygame.mixer.music.play()
            jefe = False
        if construir in range(len(Mapa)) and cambiar == True:
            Novatin.rect.centerx = xi
            Novatin.rect.centery = yi
            cambiar = False
        if construir < 9 and construir >4 and firstchange == True:
            pygame.mixer.music.load("Music/music3.mp3")
            pygame.mixer.music.play(-1)
            firstchange = False
        if construir == 9 and secondchange == True:
            pygame.mixer.music.load("Music/music4.mp3")
            pygame.mixer.music.play(-1)
            secondchange = False
        if construir < 13 and construir >9 and thirdchange == True:
            pygame.mixer.music.load("Music/music5.mp3")
            pygame.mixer.music.play(-1)
            thirdchange = False
        if construir == 14 and fourthchange == True:
            pygame.mixer.music.load("Music/music6.mp3")
            pygame.mixer.music.play(-1)
            fourthchange = False
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
                screen.blit(cabeza.image, (450,540))
            else:
                screen.blit(cabeza.image, (450,640))
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
                    if Password.no_repetir:
                        Password.no_repetir = False
                        if Password.seleccion == 37:
                            Password.clave = Password.borra_espacio(Password.clave)
                        elif Password.seleccion == 38:
                            main, construir, Novatin.rect.centerx, Novatin.rect.centery, Novatin.metralleta, Novatin.contador_m = Password.clavea()
                        #################SAVE/CHEATS################### 
                        else:
                            Password.clave += Password.caracteres[(Password.seleccion-1)]
                    else:
                        Password.no_repetir = True
                if event.key == K_UP:
                    Password.seleccion, Password.movil = Password.mover_arriba(Password.seleccion, Password.movil)
                if event.key == K_DOWN:
                    Password.seleccion, Password.movil = Password.mover_abajo(Password.seleccion, Password.movil)
                if event.key == K_RIGHT:
                    Password.seleccion, Password.movil = Password.mover_derecha(Password.seleccion, Password.movil)
                if event.key == K_LEFT:
                    Password.seleccion, Password.movil = Password.mover_izquierda(Password.seleccion, Password.movil)
            screen.blit(fondo_pass, (0,0))
            for j in range(len(Password.caracteres)):
                pos = (Password.posicion_teclado(j))
                text, text_rect = texto(Password.caracteres[j], pos[0], pos[1], 40)
                screen.blit(text, text_rect)
            pos = Password.posicion_cursor(Password.seleccion)
            screen.blit(cabeza.image, pos)
            for i in range(len(Password.clave)):
                pos = (Password.posicion_clave(i))
                password, password_rect = texto(Password.clave[i], pos[0], pos[1], 40)
                screen.blit(password, password_rect)
            pygame.display.flip()
        elif main == 3:
            for event in pygame.event.get():
                if hasattr(event, 'key')==False:
                    continue
                down = event.type == KEYDOWN
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == K_SPACE:
                    if Password.no_repetir:
                        Password.no_repetir = False
                        if Password.seleccion == 37:
                            Password.clave = Password.borra_espacio(Password.clave)
                        elif Password.seleccion == 38:
                            main, construir, Novatin.rect.centerx, Novatin.rect.centery, Novatin.metralleta, Novatin.contador_m = Password.clavea()
                        #################SAVE/CHEATS################### 
                        else:
                            Password.clave += Password.caracteres[(Password.seleccion-1)]
                    else:
                        Password.no_repetir = True
                if event.key == K_UP:
                    Password.seleccion, Password.movil = Password.mover_arriba(Password.seleccion, Password.movil)
                if event.key == K_DOWN:
                    Password.seleccion, Password.movil = Password.mover_abajo(Password.seleccion, Password.movil)
                if event.key == K_RIGHT:
                    Password.seleccion, Password.movil = Password.mover_derecha(Password.seleccion, Password.movil)
                if event.key == K_LEFT:
                    Password.seleccion, Password.movil = Password.mover_izquierda(Password.seleccion, Password.movil)
            screen.blit(fondo_pass, (0,0))
            for j in range(len(Password.caracteres)):
                pos = (Password.posicion_teclado(j))
                text, text_rect = texto(Password.caracteres[j], pos[0], pos[1], 40)
                screen.blit(text, text_rect)
            pos = Password.posicion_cursor(Password.seleccion)
            screen.blit(cabeza.image, pos)
            for i in range(len(Password.clave)):
                pos = (Password.posicion_clave(i))
                password, password_rect = texto(Password.clave[i], pos[0], pos[1], 40)
                screen.blit(password, password_rect)
            pygame.display.flip()
        else:
            Novatin.shoot = False
            for event in pygame.event.get():
                if hasattr(event, 'key')==False:
                    continue
                down = event.type == KEYDOWN
                if event.key == K_s:
                    if cb == True:
                        Vidas += 10
                        Creditos += 1
                        cb = False
                    elif cb == False:
                        cb == True
                if event.key == K_RIGHT:
                    Novatin.direccionx = 0
                    Novatin.speed = down*15
                elif event.key == K_r:
                    if Novatin.alive == False:
                        Novatin.restart = True
                elif event.key == K_LEFT:
                    Novatin.direccionx = 1
                    Novatin.speed = down*15
                elif event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == K_SPACE:
                    if s==0 and Novatin.metralleta == False:
                        Novatin.shoot=True
                        s=1
                    elif s==1 and Novatin.metralleta == False:
                        Novatin.shoot=False
                        s=0
            key = pygame.key.get_pressed()
            if key[K_UP] == True:
                Novatin.jump = True
            elif key[K_UP] == False:
                Novatin.jump = False
            if key[K_SPACE] == True and Novatin.metralleta == True:
                Novatin.shoot = True
            elif key[K_SPACE] == False and Novatin.metralleta == True:
                Novatin.shoot = False
            #############################################################################
            screen.fill(black) #si se pone dentro del if entonces se vuelve negra una vez
            #############################################################################
            if Novatin.alive==True:
                Novatin.move(Mapa[construir].plataformas,x)
                Novatin.saltar(y,Mapa[construir].plataformas)
                Novatin.disparar(Mapa[construir].plataformas,Mapa[construir].save,Mapa[construir].enemigos,x, Mapa[construir].jefes)
                Novatin.ambiente(Mapa[construir].espinas,cabeza,brazo_d,brazo_i, Mapa[construir].manzanas,Mapa[construir].camaespinas,Mapa[construir].enemigos,Mapa[construir].powerups, Mapa[construir].jefes)
                for change in Mapa[construir].changes:
                    if ((Novatin.rect.right> change[0] and Novatin.rect.left <= change[0]) or (Novatin.rect.left<change[0] and Novatin.rect.right >= change[0])) and Novatin.rect.centery-16<change[1] and Novatin.rect.centery+16>change[1]:
                        xi = change[3]
                        yi = change[4]
                        construir = change[2]
                        cambiar = True
            else:
                Novatin.shoot = False
                Novatin.disparar(Mapa[construir].plataformas,Mapa[construir].save,Mapa[construir].enemigos,x, Mapa[construir].jefes)
                if Novatin.play == True:
                    pygame.mixer.music.load("Music/gameover.mp3")
                    pygame.mixer.music.play()
                    Novatin.play = False
                    Vidas -=1
                    if (Vidas==0):
                        main = 3
                Novatin.revivir += 1
                if Novatin.revivir == 300 or Novatin.restart == True:
                    if construir !=4:
                        pygame.mixer.music.load("Music/music1.mp3")
                        pygame.mixer.music.play(-1)
                    elif construir == 4:
                        pygame.mixer.music.load("Music/music2.mp3")
                        pygame.mixer.music.play()
                    elif construir>4 and construir<9:
                        pygame.mixer.music.load("Music/music3.mp3")
                        pygame.mixer.music.play(-1)
                    elif construir == 9:
                        pygame.mixer.music.load("Music/music4.mp3")
                        pygame.mixer.music.play(-1)
                    elif construir>9 and construir<13:
                        pygame.mixer.music.load("Music/music5.mp3")
                        pygame.mixer.music.play(-1)
                    elif construir == 14:
                        pygame.mixer.music.load("Music/music6.mp3")
                        pygame.mixer.music.play(-1)
                    Novatin.revivir = 0
                    Novatin.alive = True
                    Novatin.play = True
                    Novatin.restart = False
                    for i in range(len(Mapa)):
                        for jefe in Mapa[i].jefes:
                            jefe.reppos()
                    for i in range(len(Mapa)):
                        for j in range(len(Mapa[i].save)):
                            if Mapa[i].save[j].deactivate==True:
                                auxi=i
                                auxj=j
                                deactivate=True
                    if deactivate==True:
                        for i in range(len(Mapa)):
                            for j in range(len(Mapa[i].save)):
                                if i!=auxi and j!=auxj:
                                    Mapa[i].save[j].active=False
                        Mapa[auxi].save[auxj].deactivate=False
                        deactivate=False
                        auxi=0
                        auxj=0
                    for i in range(len(Mapa)):
                        for j in range(len(Mapa[i].save)):
                            if Mapa[i].save[j].active==True:
                                Novatin.rect.centerx = Mapa[i].save[j].savex
                                Novatin.rect.centery = Mapa[i].save[j].savey
                                construir = i
                                first=True
                    if first==False:
                        Novatin.rect.centerx = 48
                        Novatin.rect.centery = y-48
                        construir=0
                    cabeza.alive = False
                    cabeza.roce = random.randint(-15,15)
                    cabeza.jumpspeed = random.randint(10, 25)
                    brazo_d.alive = False
                    brazo_d.roce = random.randint(-15,15)
                    brazo_d.jumpspeed = random.randint(10,25)
                    brazo_i.alive = False
                    brazo_i.roce = random.randint(-15,15)
                    brazo_i.jumpspeed = random.randint(10,25)
                    Mapa[construir].Restaurar()
            muertes, muertes_rect = texto(str(Novatin.muertes), x-100, 20, 20)
            creditos, creditos_rect = texto(str(Creditos), x-150, 20, 20)
            if Novatin.contador_m < 300:
                bonus, bonus_rect = texto(str(Novatin.contador_m//30+1), x-100, 40, 20)
            if cabeza.alive:
                cabeza.jump(y)
            if brazo_i.alive:
                brazo_i.jump(y)
                brazo_i.mover(y)
            if brazo_d.alive:
                brazo_d.mover(y)
                brazo_d.jump(y)
            screen.blit(fondo, (0,0))
            Mapa[construir].Imprimir(Novatin, Clases.PowerUp)
            for clave in Mapa[construir].claves:
                password, password_rect = texto(clave.password, clave.posx, clave.posy, 40)
                screen.blit(password, password_rect)
            if Novatin.alive==True:
                screen.blit(Novatin.image, Novatin.rect)
            if cabeza.alive:
                screen.blit(cabeza.image, cabeza.rect)
            if brazo_d.alive:
                screen.blit(brazo_d.image, brazo_d.rect)
            if brazo_i.alive:
                screen.blit(brazo_i.image, brazo_i.rect)
            screen.blit(muertes, muertes_rect)
            screen.blit(creditos, creditos_rect)
            if Novatin.contador_m < 300:
                screen.blit(bonus, bonus_rect)
            for bullet in Novatin.bullets:
                if bullet.alive==True:
                    screen.blit(bullet.image, bullet.rect)
            if Novatin.alive == False:
                screen.blit(gameover,(x/2-400,(y-191)/2))
            pygame.display.flip()
    
if __name__=="__main__":
    Go()
