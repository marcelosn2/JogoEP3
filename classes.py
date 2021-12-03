from os import path, times
import time
import pygame
from pygame.locals import *
import sys
import random
from configuracoes import *
#Inicia Escritura
pygame.font.init()
# Importando as imagens
img_dir = path.join(path.dirname(__file__), 'imagens')
# Classe do personagem principal
class Puli(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dir= pygame.image.load(path.join(img_dir, "right.png")).convert()
        self.image=self.dir
        self.esq=pygame.image.load(path.join(img_dir, "left.png")).convert()
        self.image=pygame.transform.scale(self.esq, (50,50))
        self.image.set_colorkey(BLACK)
        self.image=pygame.transform.scale(self.dir, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom= HEIGHT - 40 
        self.screenupdate = False
        self.speedx=0
        self.speedy = -5
        self.isJump = False
        self.jumpCount = 0
        self.radius=10
    #Update da classe do personagem principal
    def update(self):
        
        self.rect.x += self.speedx
        
        if self.isJump:
            if self.jumpCount > 0:
                self.rect.y += self.speedy
                self.jumpCount -= 1
            else:
                self.rect.y -= self.speedy 
        else:
            self.rect.y -= self.speedy 


        if self.rect.right>WIDTH:
            self.rect.left=0
        if self.rect.left<0:
            self.rect.right=WIDTH
        
        if self.screenupdate:
            self.rect.centerx=self.rect.centerx
            self.rect.bottom= HEIGHT - 40 
            self.screenupdate = False
            self.isJump = True
# Classe da plataforma verde
class PlatV(pygame.sprite.Sprite):
    def __init__(self):

        x = random.randint(0,WIDTH)
        y = random.randint(0,HEIGHT)

        pygame.sprite.Sprite.__init__(self)
        verde=pygame.image.load(path.join(img_dir, "green.png")).convert()
        self.image=verde
        self.image=pygame.transform.scale(verde, (120,30))
        self.image.set_colorkey(BLACK)
        self.width=120
        self.height=30
        self.rect=self.image.get_rect()
        self.rect.centerx= x
        self.rect.bottom= y
        self.speedx=0

    #Update da classe da plataforma verde
    def update(self):
        pass

# Classe da plataforma verde inicial
class PlatVInit(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        verde=pygame.image.load(path.join(img_dir, "green.png")).convert()
        self.image=verde
        self.image=pygame.transform.scale(verde, (120,30))
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom= HEIGHT -10 
        self.speedx=0
        self.width=120
        self.height=30
    # Update da classe da plataforma verde inicial
    def update(self):
        self.rect.bottom = self.rect.bottom 
        self.rect.centerx=self.rect.centerx

# Classe da plataforma azul
class PlatB(pygame.sprite.Sprite):
    def __init__(self):
        x = random.randint(0,WIDTH)
        y = random.randint(0,HEIGHT)
        
        pygame.sprite.Sprite.__init__(self)
        azul=pygame.image.load(path.join(img_dir, "blue.png")).convert()
    
        self.image=pygame.transform.scale(azul, (120,30))
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.y= y
        self.count = 0
        self.width = 120
        self.height = 30
        self.speedx=2

    # Update da classe da plataforma azul
    def update(self):
        if 0 <= self.count <= 60 :
            self.rect.x += self.speedx 
            self.count += 1
        elif 60 < self.count <= 120:
            self.rect.x -= self.speedx
            self.count += 1
        else: 
            self.count = 0
        if self.rect.right>WIDTH:
            self.rect.left=0
        if self.rect.left<0:
            self.rect.right=WIDTH
#classe de pontuacao
class Score(pygame.sprite.Sprite):
    def __init__(self):
        self.numero = 0
        self.font = pygame.font.SysFont("Arial", 25)
        self.text= self.font.render(str(self.numero), True, BLACK, WHITE)
        self.rect = self.text.get_rect()
        self.rect.x=10
        self.rect.y=10 
#update da pontuacao
    def update(self):
        self.numero = self.numero