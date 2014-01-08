import pygame, sys, Clases, random, Maps, Password

from pygame.locals import*

def texto(texto, posx, posy, tamano, color=(255, 255, 255)):
    fuente = pygame.font.Font("SF Pixelate.ttf", tamano)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

def main():
    pygame.init()
    #Variables para la panalla y seeo de esa
    x = 1280
    y = 720
    size = (x,y)
    black = (135,206,235)
    screen = pygame.display.set_mode(size, FULLSCREEN)
    #Imagenes
    menu = pygame.image.load("Imagenes/menu.png")
    fondo = pygame.image.load("Imagenes/fondo.png")
    fondo_pass = pygame.image.load("Imagenes/fondo_pass.png")
    gameover = pygame.image.load("Imagenes/gameover.png")
    #Musica
    #pygame.mixer.music.load("Music/music1.mp3")
    #pygame.mixer.music.play(-1)
    #Clock
    clock = pygame.time.Clock()
    #Variables de Novatin
    s = 0
    cabeza = Clases.Extremidad(0,0,"cabeza")
    brazo_i = Clases.Extremidad(0,0,"brazo_i")
    brazo_d = Clases.Extremidad(0,0,"brazo_d")
    saven = 0
    xi = x/2
    yi = y-20
    di = 0
    mi = False
    Novatin = Clases.Novatin(xi,yi,di,mi)
    #Portada
    main = 1
    seleccion = 0
    #Mapas
    construir = 0
    cambiar = False
    Mapa = []
    Mapa.append(Maps.MapaUnoBeta(x,y))
    Mapa.append(Maps.MapaDosBeta(x,y))

    while 1:
        if construir == 0 and cambiar == True:
            if Novatin.metralleta == True:
                Novatin = Clases.Novatin(xi,yi,di,True)
            else:
                Novatin = Clases.Novatin(xi,yi,di,False)
            cambiar = False
        if construir == 1 and cambiar == True:
            if Novatin.metralleta == True:
                Novatin = Clases.Novatin(xi,yi,di,True)
            else:
                Novatin = Clases.Novatin(xi,yi,di,False)
            cambiar = False
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
                    if Password.no_repetir:
                        Password.no_repetir = False
                        if Password.seleccion == 37:
                            Password.clave = Password.borra_espacio(Password.clave)
                        elif Password.seleccion == 38:
                            main = 3
    #En esta parte va a ir la parte del save, una vez que hayan mas cosas que guardar                        
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
            #########################################################################
            screen.fill(black) #si se pone dentro del if entonces se vuelve negra una vez
            #########################################################################
            if Novatin.alive==True:
                Novatin.move(Mapa[construir].plataformas,x)
                Novatin.saltar(y,Mapa[construir].plataformas)
                Novatin.disparar(Mapa[construir].plataformas,Mapa[construir].save,Mapa[construir].enemigos,x)
                Novatin.ambiente(Mapa[construir].espinas,cabeza,brazo_d,brazo_i, Mapa[construir].manzanas,Mapa[construir].camaespinas,Mapa[construir].enemigos,Mapa[construir].powerups)
                for change in Mapa[construir].changes:
                    if ((Novatin.rect.right> change[0] and Novatin.rect.left <= change[0]) or (Novatin.rect.left<change[0] and Novatin.rect.right >= change[0])) and Novatin.rect.centery-10<change[1] and Novatin.rect.centery+10>change[1]:
                        xi = change[3]
                        yi = change[4]
                        di = change[5]
                        construir = change[2]
                        cambiar = True
            else:
                if Novatin.play == True:
                    #pygame.mixer.music.load("Music/gameover.mp3")
                    #pygame.mixer.music.play()
                    Novatin.play = False
                Novatin.revivir += 1
                if Novatin.revivir == 300 or restart == True:
                    #pygame.mixer.music.load("Music/music1.mp3")
                    #pygame.mixer.music.play(-1)
                    Novatin.revivir = 0
                    Novatin.alive = True
                    Novatin.play = True
                    Novatin.restart = False
                    Novatin.rect.centerx = Mapa[construir].save[saven].savex
                    Novatin.rect.centery = Mapa[construir].save[saven].savey
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
            if cabeza.alive:
                cabeza.jump(y)
            if brazo_i.alive:
                brazo_i.jump(y)
                brazo_i.mover(y)
            if brazo_d.alive:
                brazo_d.mover(y)
                brazo_d.jump(y)
            screen.blit(fondo, (0,0))
            #primero el if para que novatin se mueva por enfrente de las plataformas
            Mapa[construir].Imprimir(Novatin)
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
    
if __name__=="__main__":
    main()
