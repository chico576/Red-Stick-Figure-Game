import pygame



loop = True

#pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Chico Delicia")
tela = pygame.display.set_mode((1000, 500))
jogador = pygame.image.load('C:/Users/chico/Downloads/Vermelho/Vermelho.png')
jogador = pygame.transform.scale(jogador, [60,105])

backgroung = pygame.image.load("C:/Users/chico/Downloads/Vermelho/a0n6hs7k.png")

while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
           loop = False
    tela.blit(backgroung, (0,0))
    tela.blit(jogador, (710, 237))


    pygame.display.update()
