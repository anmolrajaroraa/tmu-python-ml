import pygame
pygame.init()

gameBoard = pygame.display.set_mode((500,250))

white = (255,255,255)

while True:
    gameBoard.fill(white)
    pygame.display.update()
