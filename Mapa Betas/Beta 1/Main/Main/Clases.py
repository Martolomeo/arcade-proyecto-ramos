import pygame
from pygame.locals import*

class PlataformaBaja(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pbajo.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()


class PlataformaAlta(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Palto.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

#Asumo que querias hacer esto?

class Novatin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("iwbtg.png")
        self.image1 = pygame.image.load("iwbtg.png")
        self.image2 = pygame.transform.flip(self.image1, True, False)
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect.centerx = x
        self.rect.centery = y-(self.height/2)
        self.jumpspeed = 20
        self.speedcero = 0
        self.fall = 2
        self.stopm = False
    
    def move (self,n,down,plataformas,x):
        '''n es una variable binaria que indica si el personaje
        se mueve a la derecha o a la izquierda, 0 para la
        derecha, 1 para la izquierda'''
        if n==0:
            self.rect.centerx += down*15
            self.image = self.image1
        elif n==1:
            self.rect.centerx -= down*15
            self.image = self.image2
        for i in range(len(plataformas)):
            if pygame.sprite.collide_rect(self,plataformas[i]) == True and self.rect.top>plataformas[i].rect.top:
                if n==0 and self.rect.left<plataformas[i].rect.right and self.rect.top<plataformas[i].rect.bottom and self.rect.bottom<plataformas[i].rect.bottom:
                    self.iamge = self.image1
                    self.rect.centerx = plataformas[i].rect.left-(self.width/2)
                elif n==1 and self.rect.right>plataformas[i].rect.left and self.rect.top<plataformas[i].rect.bottom and self.rect.bottom<plataformas[i].rect.bottom:
                    self.image = self.image2
                    self.rect.centerx = plataformas[i].rect.right+(self.width/2)
        if self.rect.left <= 0:
            self.rect.centerx = self.width/2
        elif self.rect.right >= x:
            self.rect.centerx = x-(self.width/2)
    '''nuevo jump v 0.25, esta vez reconociendo el entorno (solo plataformas,
    esto es bajo el supuesto de que todos los niveles tendran plataformas)'''
    def jump (self,y,jump,plataformas):
        if self.rect.top <= 0:
            self.rect.centery = self.height/2
        if jump == False:
            a=0
            for i in range(len(plataformas)):
                if pygame.sprite.collide_rect(self, plataformas[i]) == True and self.rect.bottom >= plataformas[i].rect.top and self.rect.top<plataformas[i].rect.top and self.rect.centerx<=plataformas[i].rect.right and self.rect.centerx>=plataformas[i].rect.left:
                    self.rect.centery = plataformas[i].rect.top-(self.height/2)
                    self.jumpspeed = 20
                    self.speedcero = 0
                    self.stopm = True

                elif self.rect.bottom >= y and pygame.sprite.collide_rect(self,plataformas[i])==False:
                    self.rect.centery = y-(self.height/2)
                    self.jumpspeed = 20
                    self.speedcero = 0
                    self.stopm = False

                if pygame.sprite.collide_rect(self, plataformas[i])==False:
                    a += 1
                    if a == len(plataformas):
                        self.stopm = False
                        a=0
            if self.stopm == False:
                if self.speedcero >= -10:
                    self.rect.centery -= self.speedcero
                    self.speedcero -= self.fall
                else:
                    self.rect.centery -= -10
        elif jump == True:
            a=0    
            for i in range(len(plataformas)):
                if pygame.sprite.collide_rect(self, plataformas[i]) == True and self.rect.bottom >= plataformas[i].rect.top and self.rect.top < plataformas[i].rect.top and self.rect.centerx<=plataformas[i].rect.right and self.rect.centerx>=plataformas[i].rect.left:
                    self.rect.centery = plataformas[i].rect.top-(self.height/2)
                    self.jumpspeed = 20
                    self.speedcero = 0
                    self.stopm = True

                elif pygame.sprite.collide_rect(self, plataformas[i]) == True and self.rect.top<=plataformas[i].rect.bottom+1 and self.rect.centerx<=plataformas[i].rect.right and self.rect.centerx>=plataformas[i].rect.left:
                    self.rect.centery = plataformas[i].rect.bottom+(self.height/2)
                    self.jumpspeed = -10
                    self.speedcero = 0
                    self.stopm = False
                    
                elif self.rect.bottom > y and pygame.sprite.collide_rect(self,plataformas[i])==False:
                    self.rect.centery = y-(self.height/2)
                    self.jumpspeed = 20
                    self.speedcero = 0
                    self.stopm = False
                if pygame.sprite.collide_rect(self, plataformas[i])==False:
                    a += 1
                    if a == len(plataformas):
                        self.stopm = False
                        a=0

            if self.stopm == False:
                if self.jumpspeed>= -10:
                    self.rect.centery -= self.jumpspeed
                    self.jumpspeed -= self.fall
                else:
                    self.rect.centery -= -10
