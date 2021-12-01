from os import path, times
import time
import pygame
from pygame.locals import *
import sys
import random
from configuracoes import *

img_dir = path.join(path.dirname(__file__), 'imagens')

class Puli(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dir= pygame.image.load(path.join(img_dir, "right.png")).convert()
        self.image=self.dir
        self.image=pygame.transform.scale(self.dir, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom= HEIGHT - 40 
        self.speedx=0
        self.speedy = -5
        self.isJump = False
        self.jumpCount = 0
        self.radius=10

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


        self.dir= self.dir
        self.image=self.dir
        self.image=pygame.transform.scale(self.dir, (50,50))
        self.image.set_colorkey(BLACK)



        if self.rect.right>WIDTH:
            self.rect.left=0
        if self.rect.left<0:
            self.rect.right=WIDTH


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

    def update(self):
        self.rect.bottom = self.rect.bottom 
        self.rect.centerx=self.rect.centerx


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
        self.width = 120
        self.height = 30
        self.speedx=30
    #def update(self):
     #   if self.rect.right==WIDTH:
      #      self.speedx=-2
       # if self.rect.left==0:
        #    self.speedx=2


pygame.init()
tela=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pulo desenho")
clock=pygame.time.Clock()
background = pygame.image.load(path.join(img_dir, 'background.jpg')).convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
background_rect = background.get_rect()





player = Puli()
platvinit = pygame.sprite.Group()
platV = pygame.sprite.Group()
platB = pygame.sprite.Group()

# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(PlatVInit())
platvinit.add(PlatVInit())



for i in range(8):
    m = PlatV()
    all_sprites.add(m)
    platV.add(m)

for i in range(4):
    b=PlatB()
    all_sprites.add(b)
    platB.add(b)
try:
    
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)


        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                

                    
                    
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    
        # Depois de processar os eventos.
        # Atualiza a acao de     cada sprite.
        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, platV, False, pygame.sprite.collide_circle)
        if hits:
            player.isJump = True
            player.jumpCount = 30
            player.speedy = -5
            player.dir = pygame.image.load(path.join(img_dir, "right.png")).convert()

        else:
            player.dir = pygame.image.load(path.join(img_dir, "right_1.png")).convert()
      

        hits = pygame.sprite.spritecollide(player, platvinit, False)
        if hits:
            player.isJump = True
            player.jumpCount = 30
            player.speedy = -5
            player.dir = pygame.image.load(path.join(img_dir, "right.png")).convert()
            

        else:
            player.dir = pygame.image.load(path.join(img_dir, "right_1.png")).convert()       
            
            
           
      
    
        # A cada loop, redesenha o fundo e os sprites
        tela.fill(WHITE)
        tela.blit(background, background_rect)
        all_sprites.draw(tela)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    
    pygame.quit()
