from os import path, times
import time
import pygame
from pygame.locals import *
import sys
import random
from configuracoes import *

# Importando as imagens
img_dir = path.join(path.dirname(__file__), 'imagens')

# Classe do personagem principal
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
            self.rect.centerx=WIDTH/2
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
        self.width = 120
        self.height = 30
        self.speedx=30

    # Update da classe da plataforma azul
    def update(self):
        pass
# Inicializacao do programa
pygame.init()

# Display da tela
tela=pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Pulo desenho")

# Inicializacao do relogio
clock=pygame.time.Clock()

# Inicializacao da imagem de background
background = pygame.image.load(path.join(img_dir, 'background.jpg')).convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))

background_rect = background.get_rect()


# Inicializacao das classes
player = Puli()
platvinit = pygame.sprite.Group()
platV = pygame.sprite.Group()
platB = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()



# Colocando os grupos da variavel all_sprites
all_sprites.add(player)
all_sprites.add(PlatVInit())
platvinit.add(PlatVInit())


# Adicionando varias classes a um grupo e colocando esse grupo no all_sprites
for i in range(8):
    m = PlatV()
    all_sprites.add(m)
    platV.add(m)

for i in range(4):
    b=PlatB()
    all_sprites.add(b)
    platB.add(b)

# Try - Catch para nao travar o jogo
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

        # O boneco principal pula ao colidir com uma plataforma verde
        hitsplatv = pygame.sprite.spritecollide(player, platV, False, pygame.sprite.collide_circle)
        if hitsplatv:
            player.isJump = True
            player.jumpCount = 30
            player.speedy = -5
            player.dir = pygame.image.load(path.join(img_dir, "right.png")).convert()

        else:
            player.dir = pygame.image.load(path.join(img_dir, "right_1.png")).convert()
      
        # O boneco pula ao colidir com a plataforma verde inicial
        hitsplatvinit = pygame.sprite.spritecollide(player, platvinit, False)
        if hitsplatvinit:
            player.isJump = True
            player.jumpCount = 30
            player.speedy = -5
            player.dir = pygame.image.load(path.join(img_dir, "right.png")).convert()
            

        else:
            player.dir = pygame.image.load(path.join(img_dir, "right_1.png")).convert()   

        # Ao atingir o topo da tela ha o screenupdate onde o boneco volta a sua posucao no comeco da tela e as plataformas sao 
        # renderizadas novamente de forma aleatoria na tela
        if player.rect.y == 5:
            player.screenupdate = True
            for i in platV:
                i.kill()
            all_sprites.clear(tela, background)
            all_sprites.draw(tela)
            for i in range(8):
                m = PlatV()
                all_sprites.add(m)
                platV.add(m)

    
        # A cada loop, redesenha o fundo e os sprites
        tela.fill(WHITE)
        tela.blit(background, background_rect)
        all_sprites.draw(tela)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    
    pygame.quit()
