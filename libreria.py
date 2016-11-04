import pygame
import time
import threading
import sys
import random

BLANCO=(255,255,255)
ROJO=(255,0,0)
NEGRO=(0,0,0)
AMARILLO=(255,219,0)

ancho=1095
alto=615

class FinalBoss(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=1
        self.var_y=0
        self.vida=100
        self.sonido1=pygame.mixer.Sound("sonidos/golpeGanon.wav")
        self.sonido2=pygame.mixer.Sound("sonidos/ganonMuriendo.wav")

    def menosVidaBala(self):
        self.vida-=1
    def golpe1 (self):
        self.sonido1.play()
    def golpe2 (self):
        self.sonido2.play()


    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==ancho/2-30:
            self.var_x=self.var_x*-1
        elif self.rect.x==ancho/2+30:
            self.var_x=self.var_x*-1


class Arco(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Trifuerza(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bala(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.dir=0


    def update(self):
        vel=15
        if self.dir==0:
            self.rect.x+=vel
        if self.dir==1:
            self.rect.y-=vel
        if self.dir==2:
            self.rect.x-=vel
        if self.dir==3:
            self.rect.y+=vel







class Bala2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.dir=0
        self.contador=0
        self.linea=[]

    def update(self):
        if self.contador < len(self.linea):
          self.rect.x=self.linea[self.contador][0]
          self.rect.y=self.linea[self.contador][1]
          self.contador+=1
        else:
          self.contador=0


class botonPresionado(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cofre(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Contenedor(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Caballero1(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==200 and self.rect.x==80:
            self.var_x=1
            self.var_y=1
        if self.rect.y>280  and self.rect.x>170:
            self.var_y=-1
            self.var_x=-1

class Caballero2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==265 and self.rect.x==360:
            self.var_x=-1
            self.var_y=-1
        if self.rect.y<228  and self.rect.x<300:
            self.var_y=1
            self.var_x=1




class EnemigoOctorok(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=1
        self.var_y=0




    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==550:
            self.var_x=self.var_x*-1
        elif self.rect.x==18:
            self.var_x=self.var_x*-1

class EnemigoVolando(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=3
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==600:
            self.var_x=self.var_x*-1
        elif self.rect.x==930:
            self.var_x=self.var_x*-1

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=2

    def update(self):
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==300:
            self.var_y=self.var_y*-1
        elif self.rect.y==430:
            self.var_y=self.var_y*-1


class Enemigo2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=4

    def update(self):
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==250:
            self.var_y=self.var_y*-1
        elif self.rect.y==450:
            self.var_y=self.var_y*-1



class Cuchilla1(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==414 and self.rect.x==350:
            self.var_x=0
            self.var_y=2
        if self.rect.y==460 and self.rect.x==350:
            self.var_y=0
            self.var_x=2

        if self.rect.y==460 and self.rect.x==470:
            self.var_y=-2
            self.var_x=0

        if self.rect.y==414 and self.rect.x==470:
            self.var_y=0
            self.var_x=-2

class Cuchilla2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==260 and self.rect.x==670:
            self.var_x=0
            self.var_y=-2
        if self.rect.y==214 and self.rect.x==670:
            self.var_y=0
            self.var_x=-2

        if self.rect.y==214 and self.rect.x==370:
            self.var_y=2
            self.var_x=0

        if self.rect.y==260 and self.rect.x==370:
            self.var_y=0
            self.var_x=2


class MuroBloques(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Muro(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Muro2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta1(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta3(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta4(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton1(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado1(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton3(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado3(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton4(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado4(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class llegadaNivel2(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imagen).convert_alpha()
        self.rect=self.image.get_rect()

class llegada(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imagen).convert_alpha()
        self.rect=self.image.get_rect()

class llegadaFake(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imagen).convert_alpha()
        self.rect=self.image.get_rect()



class Jugador(pygame.sprite.Sprite):

    muros=None
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.sonido1=pygame.mixer.Sound("sonidos/win.wav")
        self.sonido2=pygame.mixer.Sound("sonidos/lose.wav")
        self.sonido3=pygame.mixer.Sound("sonidos/golpeEnemigo.wav")
        self.sonido4=pygame.mixer.Sound("sonidos/abriendoPuerta.wav")
        self.sonido5=pygame.mixer.Sound("sonidos/abrir.wav")
        self.sonido7=pygame.mixer.Sound("sonidos/error.wav")
        self.sonido8=pygame.mixer.Sound("sonidos/matando.wav")
        self.sonido9=pygame.mixer.Sound("sonidos/corazon.wav")
        self.sonido10=pygame.mixer.Sound("sonidos/flecha.wav")
        self.sonido11=pygame.mixer.Sound("sonidos/corazones.wav")
        self.var_x=0
        self.var_y=0
        self.vida=100

    def menosVida(self):
        self.vida-=1

    def menosVidaBala(self):
        self.vida-=10

    def menosVidaRejas(self):
        self.vida-=0.04

    def golpe1 (self):
            self.sonido1.play()

    def golpe2 (self):
        self.sonido2.play()

    def golpe3 (self):
        self.sonido3.play()

    def golpe4 (self):
        self.sonido4.play()

    def golpe5 (self):
        self.sonido5.play()


    def golpe7 (self):
        self.sonido7.play()

    def golpe8 (self):
        self.sonido8.play()

    def golpe9 (self):
        self.sonido9.play()

    def golpe10 (self):
        self.sonido10.play()

    def golpe11 (self):
        self.sonido11.play()

    def update(self):
        self.rect.x += self.var_x
        lista_golpes = pygame.sprite.spritecollide(self, self.muros, False)
        for bloque in lista_golpes:
            if self.var_x > 0:
                self.rect.right = bloque.rect.left
            else:
                self.rect.left = bloque.rect.right

        self.rect.y += self.var_y
        lista_golpes = pygame.sprite.spritecollide(self, self.muros, False)
        for bloque in lista_golpes:
            if self.var_y > 0:
                self.rect.bottom = bloque.rect.top
            else:
                self.rect.top = bloque.rect.bottom

    def direccion(self,pos):
        if pos == 1:
            self.image = pygame.image.load("imagenes/personaje_a.png").convert_alpha()
            self.var_y = -3
            self.var_x = 0
        if pos == 2:
            self.image = pygame.image.load("imagenes/personaje.png").convert_alpha()
            self.var_y = 3
            self.var_x = 0
        if pos == 3:
            self.image = pygame.image.load("imagenes/personaje_izq.png").convert_alpha()
            self.var_x = -3
            self.var_y = 0
        if pos == 4:
            self.image = pygame.image.load("imagenes/personaje_der.png").convert_alpha()
            self.var_x = 3
            self.var_y = 0

        if pos == 14:
            self.image = pygame.image.load("imagenes/personaje_a.png").convert_alpha()
            self.var_x = 2
            self.var_y = -2

        if pos == 13:
            self.image = pygame.image.load("imagenes/personaje_a.png").convert_alpha()
            self.var_x = -2
            self.var_y = -2

        if pos == 24:
            self.image = pygame.image.load("imagenes/personaje.png").convert_alpha()
            self.var_x = 2
            self.var_y = 2

        if pos == 23:
            self.image = pygame.image.load("imagenes/personaje.png").convert_alpha()
            self.var_x = -2
            self.var_y = 2

        if pos == 5:
            self.image = pygame.image.load("imagenes/personaje.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 6:
            self.image = pygame.image.load("imagenes/personaje_izq.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 7:
            self.image = pygame.image.load("imagenes/personaje_der.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 8:
            self.image = pygame.image.load("imagenes/personaje_a.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        #------------------------------------ trifuerzaEquipada---------------------------------------#

        if pos == 11:
            self.image = pygame.image.load("imagenes/linkArriba.png").convert_alpha()
            self.var_y = -3
            self.var_x = 0
        if pos == 22:
            self.image = pygame.image.load("imagenes/linkAbajo.png").convert_alpha()
            self.var_y = 3
            self.var_x = 0
        if pos == 33:
            self.image = pygame.image.load("imagenes/linkIzqTrifuerza.png").convert_alpha()
            self.var_x = -3
            self.var_y = 0
        if pos == 44:
            self.image = pygame.image.load("imagenes/linkDerTrifuerza.png").convert_alpha()
            self.var_x = 3
            self.var_y = 0

        if pos == 55:
            self.image = pygame.image.load("imagenes/linkAbajo.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 66:
            self.image = pygame.image.load("imagenes/linkIzqTrifuerza.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 77:
            self.image = pygame.image.load("imagenes/linkDerTrifuerza.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 88:
            self.image = pygame.image.load("imagenes/linkArriba.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 144:
            self.image = pygame.image.load("imagenes/linkArriba.png").convert_alpha()
            self.var_x = 2
            self.var_y = -2

        if pos == 133:
            self.image = pygame.image.load("imagenes/linkArriba.png").convert_alpha()
            self.var_x = -2
            self.var_y = -2

        if pos == 244:
            self.image = pygame.image.load("imagenes/linkAbajo.png").convert_alpha()
            self.var_x = 2
            self.var_y = 2

        if pos == 233:
            self.image = pygame.image.load("imagenes/linkAbajo.png").convert_alpha()
            self.var_x = -2
            self.var_y = 2
