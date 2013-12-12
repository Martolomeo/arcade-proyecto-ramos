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
        self.rect.centerx = x
        self.rect.centery = y-(self.height/2)
        self.jumpspeed = 20
        self.speedcero = 0
        self.fall = 2
        self.doublejump = True
    
    def move (self,n,down):
        '''n es una variable binaria que indica si el personaje
        se mueve a la derecha o a la izquierda, 0 para la
        derecha, 1 para la izquierda'''
        if n==0:
            self.rect.centerx += down*15
            self.image = self.image1
        elif n==1:
           self.rect.centerx -= down*15
           self.image = self.image2

    def jump (self,y,jump):
        if jump == False:
            if self.rect.bottom >= y:
                 self.rect.centery = y-(self.height/2)
                 self.jumpspeed = 20
                 self.speedcero = 0
                 self.doublejump = True
            else:
                self.rect.centery -= self.speedcero
                self.speedcero -= self.fall
        elif jump == True:
            self.rect.centery -= self.jumpspeed
            self.jumpspeed -= self.fall
            if self.rect.bottom > y:
                self.rect.centery = y-(self.height/2)
                self.jumpspeed = 20
                self.speedcero = 0
                self.doublejump = True
