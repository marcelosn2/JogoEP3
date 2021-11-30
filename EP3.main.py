import pygame
from pygame.locals import *
import sys
import random
from configuracoes import *
WIDTH=600
HEIGHT=600
WHITE=(255,255,255)
FPS=50

class Puli(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        dir=pygame.image.load('imagens/right.png').convert()
        self.image=dir
        self.image=pygame.transform.scale(dir, (100,100))

        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=-10
        self.speedx=0
        self.radius=30
        def update(self):
            if self.rect.right>WIDTH:
                self.rect.right=0
            if self.rect.left<0:
                self.rect.left=WIDTH
tela=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pulo desenho")
clock=pygame.time.Clock()

verde=pygame.image.load('imagens/green.png').convert()
azul=pygame.image.load('imagens/blue.png').convert()
vemelho=pygame.image.load('imagens/red.png').convert()
dir=pygame.image.load('imagens/right.png').convert()
esq=pygame.image.load('imagens/left.png').convert()
        
pygame.init()

#def drawGrid(self):
    #for x in range(80):
        #pygame.draw.line(self.screen, (222,222,222), (x * 12, 0), (x * 12, 600))
        #pygame.draw.line(self.screen, (222,222,222), (0, x * 12), (800, x * 12))



player=Puli()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)
try:
    game=True

    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game= False

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:
                    player.speedx=-8
                if event.key==pygame.K_RIGHT:
                    player.speefx=8
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    player.speedx=0
                if event.key==pygame.K_RIGHT:
                    player.speefx=0
        all_sprites.update()
        tela.fill(WHITE)
        all_sprites.draw(tela)
        pygame.display.flip
finally:
    pygame.quit()