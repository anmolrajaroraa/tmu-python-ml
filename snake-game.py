import pygame, random
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
x = 0
y = 0
width = 1000
height = 500
x2 = random.choice(range(0,width - 50))
y2 = random.choice(range(0,height - 50))
moveX = 0
moveY = 0
snakeWidth = 50

gameBoard = pygame.display.set_mode((width,height))


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            #for quitting pygame
            pygame.quit()
            #for quitting python
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                moveY = 0.3
                moveX = 0
            elif event.key == pygame.K_RIGHT:
                moveX = 0.3
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -0.3
                moveY = 0
            elif event.key == pygame.K_UP:
                moveY = -0.3
                moveX = 0

    gameBoard.fill(white)
    #  surface, color, [x,y,width,height]
    rect1 = pygame.draw.rect(gameBoard, red, [x,y,snakeWidth,50])
    rect2 = pygame.draw.rect(gameBoard, black, [x2,y2,50,50])
    if rect1.colliderect(rect2):
        x2 = random.choice(range(0, width - 50))
        y2 = random.choice(range(0, height - 50))
        snakeWidth += 50
    x += moveX
    y += moveY

    '''if x <= 0:
        moveX = 1
    elif x > width - 50:
        moveX = -1
    if y <= 0:
        moveY = 1
    elif y > height - 50:
        moveY = -1'''

    #pygame.draw.circle(gameBoard, red, [100,100], 50)
    pygame.display.update()
