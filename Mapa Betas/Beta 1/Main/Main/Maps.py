import pygame, Clases
from pygame.locals import*

class MapaUnoBeta(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.plataformas = []
        self.plataformas.append(Clases.PlataformaAlta(128, y-180))
        self.plataformas.append(Clases.PlataformaBaja(384, y-45))
        self.plataformas.append(Clases.PlataformaBaja(x-384, y-45))
        self.plataformasr = self.plataformas
        self.screen = pygame.display.set_mode((x,y))
        self.save = []
        self.enemigos = []
        self.espinas = []
        self.manzanas = []
        self.camaespinas = []
        self.powerups = []
        self.changes = []
        self.changes.append([x, y-20,1,25,0,0])

    def Imprimir(self,Novatin,PowerUp):
        for plataforma in self.plataformas:
            self.screen.blit(plataforma.image, plataforma.rect)

    def Restaurar(self):
        self.plataformas = self.plataformasr

class Mapa(pygame.sprite.Sprite):
    def __init__(self,x,y,level,n):
        self.x = x
        self.y = y
        self.screen = pygame.display.set_mode((x,y))
        self.plataformas = []
        self.save = []
        self.enemigos = []
        self.enemigosr = []
        self.espinas = []
        self.espinasr = []
        self.manzanas = []
        self.manzanasr = []
        self.camaespinas = []
        self.powerups = []
        self.changes = []
        self.lugares = []
        self.nubes = []
        self.arboles = []
        self.etapa = n
        level = open(level)
        for j in range(48):
            aux = level.readline()
            for i in range(32):
                if aux[i] == "m":
                    self.plataformas.append(Clases.Plataforma(i*32+16, j%24*32+16))
                elif aux[i] == "e":
                    self.enemigos.append(Clases.Enemigo(i*32+16, j%24*32+16))
                    self.enemigosr.append(Clases.Enemigo(i*32+16, j%24*32+16))
                elif aux[i] == "w":
                    self.espinas.append(Clases.Espina(i*32+16, j%24*32+16, True))
                    self.espinasr.append(Clases.Espina(i*32+16, j%24*32+16, True))
                elif aux[i] == "q":
                    self.espinas.append(Clases.Espina(i*32+16, j%24*32+16, False))
                    self.espinasr.append(Clases.Espina(i*32+16, j%24*32+16, False))
                elif aux[i] == "l":
                    self.manzanas.append(Clases.Manzana(i*32+16, j%24*32+16, False, True))
                    self.manzanasr.append(Clases.Manzana(i*32+16, j%24*32+16, False, True))
                elif aux[i] == "k":
                    self.manzanas.append(Clases.Manzana(i*32+16, j%24*32+16, True, False))
                    self.manzanasr.append(Clases.Manzana(i*32+16, j%24*32+16, True, False))
                elif aux[i] == "n":
                    self.manzanas.append(Clases.Manzana(i*32+16, j%24*32+16, False, False))
                    self.manzanasr.append(Clases.Manzana(i*32+16, j%24*32+16, False, False))
                elif aux[i] == "c":
                    self.camaespinas.append(Clases.Camaespina(i*32+48, j%24*32+16))
                elif aux[i] == "s":
                    self.save.append(Clases.Save(i*32+16,j%24*32+16, i*32+16, j%24*32+48))
                elif aux[i] == "f":
                    self.lugares.append((i*32+16, j%24*32+16))
                elif aux[i] == "o":
                    self.ombudsman = Clases.Ombudsman(i*32+16, j%24*32+16)
                elif aux[i] == "p":
                    if aux[i+1] == "p" and aux[i-1] == "p":
                        self.nubes.append(Clases.NubeM(i*32+16, j%24*32+16))
                    elif aux[i+1] == "p":
                        self.nubes.append(Clases.NubeL(i*32+16, j%24*32+16))
                    elif aux[i-1] == "p":
                        self.nubes.append(Clases.NubeR(i*32+16, j%24*32+16))
                    else:
                        self.nubes.append(Clases.Nubechica(i*32+16, j%24*32+16))
                elif aux[i] == "a":
                    self.arboles.append(Clases.Arbol(i*32+48, j%24*32+80))
                    

    def cambia(self, mapas):
        for i in range(len(mapas)):
            if self.etapa == mapas[i].etapa:
                for j in range(len(self.lugares)):
                    if i == len(mapas)-1:
                        pass
                    else:
                        for k in range(len(mapas[i+1].lugares)):
                            if self.lugares[j][1] == mapas[i+1].lugares[k][1] and (self.lugares[j][0] == 16 or self.lugares[j][0] == 1008):
                                aux = [self.lugares[j][0], self.lugares[j][1], self.etapa, mapas[i+1].lugares[k][0]+17, mapas[i+1].lugares[k][1]]
                                self.changes.append(aux)
                            elif self.lugares[j][0] == mapas[i+1].lugares[k][0] and (self.lugares[j][1] == 16 or self.lugares[j][1] == 752):
                                aux = [self.lugares[j][0], self.lugares[j][1], self.etapa, mapas[i+1].lugares[k][0], mapas[i+1].lugares[k][1]+17]
                                self.changes.append(aux)
                    if i == 0:
                        pass
                    else:
                        for k in range(len(mapas[i-1].lugares)):
                            if self.lugares[j][1] == mapas[i-1].lugares[k][1] and (self.lugares[j][0] == 16 or self.lugares[j][0] == 100):
                                aux = [self.lugares[j][0], self.lugares[j][1], self.etapa-2, mapas[i-1].lugares[k][0]-17, mapas[i-1].lugares[k][1]]
                                self.changes.append(aux)
                            elif self.lugares[j][0] == mapas[i-1].lugares[k][0] and (self.lugares[j][1] == 16 or self.lugares[j][1] == 752):
                                aux = [self.lugares[j][0], self.lugares[j][1], self.etapa-2, mapas[i-1].lugares[k][0], mapas[i-1].lugares[k][1]-17]
                                self.changes.append(aux)
                    
    def Imprimir(self, Novatin, PowerUp):
            for nube in self.nubes:
                self.screen.blit(nube.image, nube.rect)
            for camaespina in self.camaespinas:
                camaespina.trampa(Novatin,self.plataformas)
                self.screen.blit(camaespina.image, camaespina.rect)
            for sav in self.save:
                self.screen.blit(sav.image, sav.rect)
            for arbol in self.arboles:
                self.screen.blit(arbol.image, arbol.rect)
            for manzana in self.manzanas:
                manzana.trampa(Novatin,self.y)
                if manzana.alive == True:
                    self.screen.blit(manzana.image, manzana.rect)
            for espina in self.espinas:
                espina.trampa(Novatin)
                if espina.alive == True:
                    self.screen.blit(espina.image, espina.rect)
            self.ombudsman.liberarse(Novatin, self, PowerUp)
            self.screen.blit(self.ombudsman.image, self.ombudsman.rect)                
            for enemigo in self.enemigos:
                if enemigo.alive == True:
                    enemigo.move(self.plataformas,self.x)
                    self.screen.blit(enemigo.image, enemigo.rect)
            for powerup in self.powerups:
                if powerup.alive == True:
                    self.screen.blit(powerup.image, powerup.rect)
            for plataforma in self.plataformas:
                self.screen.blit(plataforma.image, plataforma.rect)                    

    def Restaurar(self):
        self.espinas = []
        for espina in self.espinasr:
            self.espinas.append(Clases.Espina(espina.rect.centerx, espina.rect.centery, espina.movil))
        self.manzanas = []
        for manzana in self.manzanasr:
            self.manzanas.append(Clases.Manzana(manzana.rect.centerx, manzana.rect.centery, manzana.moveru, manzana.moverd))
        self.enemigos = []
        for enemigo in self.enemigosr:
            self.enemigos.append(Clases.Enemigo(enemigo.rect.centerx, enemigo.rect.centery))
        if not self.ombudsman.atrapado:
            self.ombudsman.atrapado = True
            self.ombudsman.restaurar()
        for camaespina in self.camaespinas:
            camaespina.rect.centery=camaespina.yi

class MapaDosBeta(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.plataformas = []
        self.espinasr = []
        self.espinas = []
        self.arboles = []
        self.manzanasr = []
        self.manzanas = []
        self.camaespinas = []
        self.nubes = []
        self.save = []
        self.enemigosr = []
        self.enemigos = []
        self.powerups = []
        self.plataformas.append(Clases.PlataformaBaja(128, 95))
        self.plataformas.append(Clases.PlataformaBaja(384, 145))
        self.plataformas.append(Clases.PlataformaAlta(768, 320))
        self.plataformas.append(Clases.PlataformaAlta(896, 0))
        self.plataformas.append(Clases.PlataformaBaja(512, 455))
        self.plataformas.append(Clases.PlataformaAlta(128, 620))
        self.plataformas.append(Clases.PlataformaBaja(896, y))
        self.plataformas.append(Clases.PlataformaBaja(x, y-90))
        self.plataformas.append(Clases.PlataformaBaja(896, y-180))
        self.plataformas.append(Clases.PlataformaBaja(x, y-270))
        self.plataformas.append(Clases.PlataformaBaja(896, y-360))
        self.plataformas.append(Clases.PlataformaBaja(x, y-450))
        self.espinasr.append(Clases.Espina(600, y-24, True))
        self.espinasr.append(Clases.Espina(648,y-24, False))
        self.espinasr.append(Clases.Espina(552,y-24, False))
        self.espinas.append(Clases.Espina(600, y-24, True))
        self.espinas.append(Clases.Espina(648,y-24, False))
        self.espinas.append(Clases.Espina(552,y-24, False))
        self.arboles.append(Clases.Arbol(450,y-75))
        self.manzanasr.append(Clases.Manzana(430,y-120,False,True))
        self.manzanasr.append(Clases.Manzana(470, y-130,False,False))
        self.manzanas.append(Clases.Manzana(430,y-120,False,True))
        self.manzanas.append(Clases.Manzana(470, y-130,False,False))
        self.camaespinas.append(Clases.Camaespina(950, y-360))
        self.nubes.append(Clases.Nubechica(600,50))
        self.nubes.append(Clases.NubeL(1050, 100))
        self.nubes.append(Clases.NubeM(1098, 100))
        self.nubes.append(Clases.NubeM(1146, 100))
        self.nubes.append(Clases.NubeR(1194, 100))
        self.save.append(Clases.Save(896,y-100,25,0))
        self.enemigosr.append(Clases.Enemigo(700, 120))
        self.enemigosr.append(Clases.Enemigo(450, 390))
        self.enemigosr.append(Clases.Enemigo(550, 390))
        self.enemigosr.append(Clases.Enemigo(128, 420))
        self.enemigosr.append(Clases.Enemigo(x-30, y-155))
        self.enemigosr.append(Clases.Enemigo(x-30, y-335))
        self.enemigosr.append(Clases.Enemigo(x-30, y-515))
        self.enemigos.append(Clases.Enemigo(700, 120))
        self.enemigos.append(Clases.Enemigo(450, 390))
        self.enemigos.append(Clases.Enemigo(550, 390))
        self.enemigos.append(Clases.Enemigo(128, 420))
        self.enemigos.append(Clases.Enemigo(x-30, y-155))
        self.enemigos.append(Clases.Enemigo(x-30, y-335))
        self.enemigos.append(Clases.Enemigo(x-30, y-515))
        self.screen = pygame.display.set_mode((x,y))
        self.ombudsman = Clases.Ombudsman(50,420)
        self.changes = []
        self.changes.append([0,30,0,x-30,y-20,1])

    def Imprimir(self, Novatin, PowerUp):
        for nube in self.nubes:
            self.screen.blit(nube.image, nube.rect)
        for camaespina in self.camaespinas:
            camaespina.trampa(Novatin,self.plataformas)
            self.screen.blit(camaespina.image, camaespina.rect)
        for plataforma in self.plataformas:
            self.screen.blit(plataforma.image, plataforma.rect)
        for sav in self.save:
            self.screen.blit(sav.image, sav.rect)
        for arbol in self.arboles:
            self.screen.blit(arbol.image, arbol.rect)
        for manzana in self.manzanas:
            manzana.trampa(Novatin,self.y)
            if manzana.alive == True:
                self.screen.blit(manzana.image, manzana.rect)
        for espina in self.espinas:
            espina.trampa(Novatin)
            if espina.alive == True:
                self.screen.blit(espina.image, espina.rect)
        self.ombudsman.liberarse(Novatin, self, PowerUp)
        self.screen.blit(self.ombudsman.image, self.ombudsman.rect)                
        for enemigo in self.enemigos:
            if enemigo.alive == True:
                enemigo.move(self.plataformas,self.x)
                self.screen.blit(enemigo.image, enemigo.rect)
        for powerup in self.powerups:
            if powerup.alive == True:
                self.screen.blit(powerup.image, powerup.rect)

    def Restaurar(self):
        self.espinas = []
        for espina in self.espinasr:
            self.espinas.append(Clases.Espina(espina.rect.centerx, espina.rect.centery, espina.movil))
        self.manzanas = []
        for manzana in self.manzanasr:
            self.manzanas.append(Clases.Manzana(manzana.rect.centerx, manzana.rect.centery, manzana.moveru, manzana.moverd))
        self.enemigos = []
        for enemigo in self.enemigosr:
            self.enemigos.append(Clases.Enemigo(enemigo.rect.centerx, enemigo.rect.centery))
        if not self.ombudsman.atrapado:
            self.ombudsman.atrapado = True
            self.ombudsman.restaurar()
