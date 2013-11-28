import pygame
from pygame.locals import*

class PlataformaBaja(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("Pbajo.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    self.width = self.image.get_width()
    #self.hi