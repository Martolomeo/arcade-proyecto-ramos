import pygame, random
from pygame.locals import*

class PlataformaBaja(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/Pbajo.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()


class PlataformaAlta(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/Palto.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

class Novatin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/novatin_derecha.png")
        self.quieto_d = pygame.image.load("Imagenes/novatin_derecha.png")
        self.quieto_i = pygame.transform.flip(self.quieto_d, True, False)
        self.mov1_d = pygame.image.load("Imagenes/novatin_mov_derecha1.png")
        self.mov1_i = pygame.transform.flip(self.mov1_d, True, False)
        self.mov2_d = pygame.image.load("Imagenes/novatin_mov_derecha2.png")
        self.mov2_i = pygame.transform.flip(self.mov2_d, True, False)
        self.mov3_d = pygame.image.load("Imagenes/novatin_mov_derecha3.png")
        self.mov3_i = pygame.transform.flip(self.mov3_d, True, False)
        self.salto_1_d = pygame.image.load("Imagenes/novatin_salto1.png")
        self.salto_1_i = pygame.transform.flip(self.salto_1_d, True, False)
        self.salto_2_d = pygame.image.load("Imagenes/novatin_salto2.png")
        self.salto_2_i = pygame.transform.flip(self.salto_2_d, True, False)
        self.salto_3_d = pygame.image.load("Imagenes/novatin_salto3.png")
        self.salto_3_i = pygame.transform.flip(self.salto_3_d, True, False)
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect.centerx = x
        self.rect.centery = y-(self.height/2)
        self.jumpspeed = 15
        self.speedcero = 0
        self.fall = 2
        self.animar_d = 0
        self.animar_i = 0
        self.stopm = False
        self.bullets = []
        self.j = 0
        self.alive = True
        self.revivir = 0
        self.pos_actual = (self.rect.centerx, self.rect.centery)
        self.pos_anterior = (self.rect.centerx, self.rect.centery)
    
    def move (self,n,down,plataformas,x):
        '''n es una variable binaria que indica si el personaje
        se mueve a la derecha o a la izquierda, 0 para la
        derecha, 1 para la izquierda'''
        self.pos_anterior = self.pos_actual
        if n==0:
            self.rect.centerx += down*15
            if self.animar_d <= 5:
                self.image = self.mov1_d
                self.animar_d += 1
            elif self.animar_d <= 10:
                self.image = self.mov2_d
                self.animar_d += 1
            elif self.animar_d <= 15:
                self.image = self.mov3_d
                self.animar_d += 1
            elif self.animar_d > 15:
                self.animar_d = 0
            self.animar_i = 0
        elif n==1:
            self.rect.centerx -= down*15
            if self.animar_i <= 5:
                self.image = self.mov1_i
                self.animar_i += 1
            elif self.animar_i <= 10:
                self.image = self.mov2_i
                self.animar_i += 1
            elif self.animar_i <= 15:
                self.image = self.mov3_i
                self.animar_i += 1
            elif self.animar_i > 15:
                self.animar_i = 0
            self.animar_d = 0
        for i in range(len(plataformas)):
            if pygame.sprite.collide_rect(self,plataformas[i]) == True and self.rect.top>plataformas[i].rect.top:
                if n==0 and self.rect.left<plataformas[i].rect.right and self.rect.top<plataformas[i].rect.bottom and self.rect.bottom<=plataformas[i].rect.bottom:
                    self.image = self.quieto_d
                    self.rect.centerx = plataformas[i].rect.left-(self.width/2)
                elif n==1 and self.rect.right>plataformas[i].rect.left and self.rect.top<plataformas[i].rect.bottom and self.rect.bottom<=plataformas[i].rect.bottom:
                    self.image = self.quieto_i
                    self.rect.centerx = plataformas[i].rect.right+(self.width/2)
        if self.rect.left <= 0:
            self.rect.centerx = self.width/2
            self.image = self.quieto_i
        elif self.rect.right >= x:
            self.rect.centerx = x-(self.width/2)
            self.image = self.quieto_d
        self.pos_actual = (self.rect.centerx, self.rect.centery)
        if self.pos_actual == self.pos_anterior:
            self.animar_d = 0
            self.animar_i = 0
            if n == 0:
                self.image = self.quieto_d
            if n == 1:
                self.image = self.quieto_i            
    '''nuevo jump v 0.25, esta vez reconociendo el entorno (solo plataformas,
    esto es bajo el supuesto de que todos los niveles tendran plataformas)'''
    def jump (self,n,y,jump,plataformas):
        a = 0
        if self.rect.top <= 0:
            self.rect.centery = self.height/2
            self.jumpspeed = -10
        if jump == False:
            for i in range(len(plataformas)):
                if self.rect.bottom >= plataformas[i].rect.top and pygame.sprite.collide_rect(self, plataformas[i]) == True and self.rect.top<plataformas[i].rect.top and self.rect.centerx<=plataformas[i].rect.right and self.rect.centerx>=plataformas[i].rect.left:
                    self.rect.centery = plataformas[i].rect.top-(self.height/2)+1
                    self.jumpspeed = 15
                    self.speedcero = 0
                    self.j=0
                    a=0
                    self.stopm = True

                elif self.rect.bottom >= y and pygame.sprite.collide_rect(self,plataformas[i])==False:
                    self.rect.centery = y-(self.height/2)
                    self.jumpspeed = 15
                    self.speedcero = 0
                    self.j=0
                    a=0
                    self.stopm = False

                if pygame.sprite.collide_rect(self, plataformas[i])==False:
                    a += 1
                    if a== len(plataformas) and self.rect.bottom<y and self.j==0:
                        self.jumpspeed=15
                        while jump==True:
                            if self.jumpspeed >= -20:
                                self.rect.centery -= self.jumpspeed
                                self.jumpspeed -= self.fall
                            else:
                                self.rect.centery -= -20
                        self.j=1
                    if a == len(plataformas):
                        self.stopm = False
                        a=0
            if self.stopm == False:
                if n == 0:
                    self.image = self.salto_3_d
                else:
                    self.image = self.salto_3_i
                if self.speedcero >= -20:
                    self.rect.centery -= self.speedcero
                    self.speedcero -= self.fall
                else:
                    self.rect.centery -= -20
        elif jump == True:
            a=0
            for i in range(len(plataformas)):
                
                if pygame.sprite.collide_rect(self, plataformas[i]) == True and self.rect.bottom >= plataformas[i].rect.top and self.rect.top < plataformas[i].rect.top and self.rect.centerx<=plataformas[i].rect.right and self.rect.centerx>=plataformas[i].rect.left:
                    self.rect.centery = plataformas[i].rect.top-(self.height/2)
                    self.jumpspeed = 15
                    self.speedcero = 0
                    self.j=0

                elif pygame.sprite.collide_rect(self, plataformas[i]) == True and self.rect.top<=plataformas[i].rect.bottom+1 and self.rect.centerx<=plataformas[i].rect.right and self.rect.centerx>=plataformas[i].rect.left:
                    self.rect.centery = plataformas[i].rect.bottom+(self.height/2)
                    self.jumpspeed = -10
                    self.speedcero = 0
                    self.j=0
                    
                elif self.rect.bottom > y and pygame.sprite.collide_rect(self,plataformas[i])==False:
                    self.rect.centery = y-(self.height/2)
                    self.jumpspeed = 15
                    self.speedcero = 0
                    self.j=0

            if self.jumpspeed >= -20:
                self.rect.centery -= self.jumpspeed
                self.jumpspeed -= self.fall
                if n == 0:
                    if self.jumpspeed > 4:
                        self.image = self.salto_1_d
                    elif self.jumpspeed > -9:
                        self.image = self.salto_2_d
                    else:
                        self.image = self.salto_3_d
                else:
                    if self.jumpspeed > 4:
                        self.image = self.salto_1_i
                    elif self.jumpspeed > -9:
                        self.image = self.salto_2_i
                    else:
                        self.image = self.salto_3_i
            else:
                self.rect.centery -= -20
                if n == 0:
                    self.image = self.salto_3_d
                else:
                    self.image = self.salto_3_i
            if self.rect.top <= 0:
                self.rect.centery = self.height/2
                self.jumpspeed = 2

    def shoot (self,shoot,n,plataformas,x):
        
        if shoot == True:
            self.bullets.append(Bullet(self.rect.centerx, self.rect.centery, n))
        for bullet in self.bullets:
            bullet.move(plataformas,x)

    def ambiente(self,espinas,n,cabeza,brazo_d,brazo_i, manzanas, camaespinas):
        if self.alive == True:
            for espina in espinas:
                if pygame.sprite.collide_rect(self,espina)==True:
                    self.kill(n,cabeza,brazo_d,brazo_i)
        if self.alive == True:
            for manzana in manzanas:
                if pygame.sprite.collide_rect(self,manzana)==True:
                    self.kill(n,cabeza,brazo_d,brazo_i)
        if self.alive == True:
            for camaespina in camaespinas:
                if pygame.sprite.collide_rect(self,camaespina)==True:
                    self.kill(n,cabeza,brazo_d,brazo_i)

    def kill(self,n,cabeza,brazo_d,brazo_i):
        if self.alive==True:
            self.alive=False
        lista = [cabeza, brazo_d, brazo_i]
        for extremidad in lista:
            extremidad.alive = True
            extremidad.rect.centerx = self.rect.centerx
            extremidad.rect.centery = self.rect.centery
            extremidad.direccion = n

class Extremidad(pygame.sprite.Sprite):
    def __init__(self,x,y,n,direccionx):
        pygame.sprite.Sprite.__init__(self)
        if n == "cabeza":
            self.image = pygame.image.load("Imagenes/novatin_cabeza.png")
        if n == "brazo_i":
            self.image = pygame.image.load("Imagenes/novatin_brazo_i.png")
        if n == "brazo_d":
            self.image = pygame.image.load("Imagenes/novatin_brazo_d.png")
        self.height = self.image.get_height()
        self.cual = n
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.alive = False
        self.jumpspeed = random.randint(10,25)
        self.fall = 2
        self.direccion = direccionx
        self.roce = random.randint(-15,15)
        
    def jump(self,y):
        if self.rect.centery >= y - self.height/2:
            self.rect.centery = y - self.height/2
        else:
            self.rect.centery -= self.jumpspeed
            self.jumpspeed -= self.fall

    def mover(self,y,lado):
        if self.direccion == 0:
            if lado == 1:
                self.rect.centerx -= self.roce
            else:
                self.rect.centerx += self.roce
        if self.direccion == 1:
            if lado == 1:
                self.rect.centerx += self.roce
            else:
                self.rect.centerx -= self.roce
        if self.rect.centery >= y - self.height/2:
            if self.roce > 0:
                self.roce -= 1
            elif self.roce < 0:
                self.roce += 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.alive = True
        if n==0:
            self.speed = 20
        elif n==1:
            self.speed = -20

    def move(self, plataformas,x):
        if self.alive == True:
            self.rect.centerx += self.speed
            for plataforma in plataformas:
                if pygame.sprite.collide_rect(self,plataforma)==True:
                    self.kill()
            if self.rect.centerx<0 or self.rect.centerx>x:
                self.kill()

    def kill(self):
        self.alive=False
        del self.image
        pygame.sprite.Sprite.kill(self)

class Espina(pygame.sprite.Sprite):
    def __init__(self,x,y,movil):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/espina.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.movil = movil
        self.move = False
        self.speed = 40
        self.alive = True

    def trampa(self,novatin):
        if self.alive == True:
            if self.movil ==True and novatin.rect.top<self.rect.top and novatin.rect.bottom<self.rect.top and (novatin.rect.centerx>self.rect.centerx-10 and novatin.rect.centerx<self.rect.centerx+10):
                self.move = True
            if self.movil == True and self.move == True and self.alive == True:
                self.rect.centery -= self.speed
            if self.rect.centery < 0:
                self.kill()

    def kill(self):
        self.alive = False
        del self.image
        pygame.sprite.Sprite.kill(self)

class Arbol(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/arbol.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
class Manzana(pygame.sprite.Sprite):
    def __init__(self,x,y,moveru,moverd):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/manzana.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.moveru = moveru
        self.moverd = moverd
        self.move = False
        self.speed = 20
        self.alive = True

    def trampa(self,novatin,y):
        if self.alive == True:
            if self.moveru == True and (novatin.rect.centerx>self.rect.centerx-10 and novatin.rect.centerx<self.rect.centerx+10) and self.rect.top>novatin.rect.bottom:
                self.move = True
            elif self.moverd == True and (novatin.rect.centerx>self.rect.centerx-10 and novatin.rect.centerx<self.rect.centerx+10) and self.rect.bottom<novatin.rect.top:
                self.move = True
            if self.move == True and self.moveru == True:
                self.rect.centery -= self.speed
            elif self.move == True and self.moverd == True:
                self.rect.centery += self.speed
            if self.rect.centery < 0 or self.rect.centery > y:
                self.kill()

    def kill(self):
        self.alive = False
        del self.image
        pygame.sprite.Sprite.kill(self)

class Camaespina(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/camaespinas.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.yi = y
        self.move = False
        self.moveup = False
        self.speed = 20

    def trampa(self,novatin,plataformas):
        if self.move == False and self.moveup == False and self.rect.centery == self.yi and self.rect.left<novatin.rect.centerx and self.rect.right>novatin.rect.centerx:
            self.move == True
        if self.move == True:
            self.rect.centery+=self.speed
        for plataforma in plataformas:
            if self.rect.bottom>plataforma.rect.top and self.rect.bottom < plataforma.rect.top-1 and pygame.sprite.collide_rect(self,plataforma)==True:
                self.move = False
                self.moveup = True
                self.speed = 5
        if self.moveup == True and self.move == False:
            self.rect.centery -= self.speed
        if self.rect.centery < self.yi-2 and self.moveup == True:
            self.rect.centery = self.yi
            self.moveup == False
            self.speed = 20

class Nubechica(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/nube.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

class NubeL(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/nubel.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

class NubeM(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/nubem.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

class NubeR(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/nuber.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

class Save(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/save.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

