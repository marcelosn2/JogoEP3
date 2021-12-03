from os import path, times
import time
import pygame
from pygame.locals import *
import sys
import random
from configuracoes import *
from classes import *
# Importando as imagens
img_dir = path.join(path.dirname(__file__), 'imagens')
# Inicializacao do programa
pygame.init()

# Display da tela
tela=pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Puli Pulante")

# Inicializacao do relogio
clock=pygame.time.Clock()

# Inicializacao da imagem de background
background = pygame.image.load(path.join(img_dir, 'background.jpg')).convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
background_rect = background.get_rect()

# Inicializacao das classes
player = Puli()
score = Score()
platVinit = pygame.sprite.Group()
platV = pygame.sprite.Group()
platB = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Colocando os grupos da variavel all_sprites
all_sprites.add(player)
all_sprites.add(PlatVInit())
platVinit.add(PlatVInit())
#all_sprites.add(score())

# Adicionando varias classes a um grupo e colocando esse grupo no all_sprites
for i in range(6):
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
                    player.image=player.esq
                    player.image=pygame.transform.scale(player.esq, (50,50))
                    player.image.set_colorkey(BLACK)
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                    player.image=player.dir
                    player.image=pygame.transform.scale(player.dir, (50,50))
                    player.image.set_colorkey(BLACK)

                    
            # Verifica se soltou alguma tecla.        
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
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

        # O boneco principal pula ao colidir com uma plataforma azul
        hitsplatb = pygame.sprite.spritecollide(player, platB, False, pygame.sprite.collide_circle)
        if hitsplatb:
            player.isJump = True
            player.jumpCount = 30
            player.speedy = -5
            player.dir = pygame.image.load(path.join(img_dir, "right.png")).convert()

        else:
            player.dir = pygame.image.load(path.join(img_dir, "right_1.png")).convert()



        # O boneco pula ao colidir com a plataforma verde inicial
        hitsplatvinit = pygame.sprite.spritecollide(player, platVinit, False)
        if hitsplatvinit:
            player.isJump = True
            player.jumpCount = 30
            player.speedy = -5
            player.dir = pygame.image.load(path.join(img_dir, "right.png")).convert()
        else:
            player.dir = pygame.image.load(path.join(img_dir, "right_1.png")).convert()   

        # Ao atingir o topo da tela ha o screenupdate onde o boneco passa para a proxima fase e as plataformas sao 
        # renderizadas novamente de forma aleatoria na tela
        if player.rect.y == 5:
            player.screenupdate = True
            score.numero +=100
            for i in platV:
                i.kill()
            all_sprites.clear(tela, background)
            all_sprites.draw(tela)
            for i in range(6):
                m = PlatV()
                all_sprites.add(m)
                platV.add(m)
            for i in platB:
                i.kill()
            for i in range(4):
                b=PlatB()
                all_sprites.add(b)
                platB.add(b)
            all_sprites.clear(tela, background)
            all_sprites.draw(tela)
        if player.rect.bottom>HEIGHT-10:
            running=False
        # A cada loop, redesenha o fundo e os sprites
        tela.fill(WHITE)
        tela.blit(background, background_rect)
        all_sprites.draw(tela)
       
       # adiciona pontuacao na tela
        text_surface = score.font.render("{}".format(score.numero), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (103,  10)
        tela.blit(text_surface, text_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
   #finaliza o jogo 
    pygame.quit()