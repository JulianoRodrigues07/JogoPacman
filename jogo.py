import pygame
import time
import random
from funcoes import historico

pygame.init()
nome = ''
email = ''
historico(nome, email)
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Game Pacman")
icone = pygame.image.load("Pack/icone.png")
pygame.display.set_icon(icone)
pacman = pygame.image.load("Pack/pacman.png")
larguraPac = 110
fundo = pygame.image.load("Pack/tela.png")
ghost = pygame.image.load("Pack/ghost.png")
morte = pygame.mixer.Sound("Pack/morreu.wav")
ghostSom = pygame.mixer.Sound("Pack/pac.wav")
ghostSom.set_volume(0.1)

def mostraPac(x, y):
    gameDisplay.blit(pacman, (x, y))
def mostraGhost(x, y):
    gameDisplay.blit(ghost, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Score:"+str(contador), True, white)
    gameDisplay.blit(texto, (680, 10))
def dead():
    pygame.mixer.Sound.play(ghostSom)
    pygame.mixer.music.stop()
    escreverTela("Você Morreu!")
def game():
    pygame.mixer.music.load("Pack/trilha.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    pacPosicaoX = largura*0.42
    pacPosicaoY = altura*0.8
    movimentoX = 0
    velocidade = 20
    ghostAltura = 250
    ghostLargura = 50
    ghostVelocidade = 3
    ghostX = random.randrange(0, largura)
    ghostY = -200
    round = 0
    pygame.mixer.Sound.play(ghostSom)
    while True:
        acoes = pygame.event.get()

        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))

        escreverPlacar(round)
        ghostY = ghostY + ghostVelocidade
        mostraGhost(ghostX, ghostY)
        if ghostY > altura:
            ghostY = -200
            ghostX = random.randrange(0, largura)
            round = round+1
            ghostVelocidade += 3
            pygame.mixer.Sound.play(ghostSom)
        pacPosicaoX += movimentoX
        if pacPosicaoX < 0:
            pacPosicaoX = 0
        elif pacPosicaoX > largura-larguraPac:
            pacPosicaoX = largura-larguraPac

        if pacPosicaoY < ghostY + ghostAltura:
            if pacPosicaoX < ghostX and pacPosicaoX+larguraPac > ghostX or ghostX+ghostLargura > pacPosicaoX and ghostX+ghostLargura < pacPosicaoX+larguraPac:
                dead()

        mostraPac(pacPosicaoX, pacPosicaoY)
        pygame.display.update()
        clock.tick(60) 
game()
