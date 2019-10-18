import pygame
import random
pygame.init()

counter = 0
snakeLength = 1
snakeWidth = 50
snakeList = []
fps = 50
clock = pygame.time.Clock()

def quitGame():
    print("Game Over!!")
    pygame.quit()
    quit()

def displayScore():
    msg = "Score : {}".format(counter)
    gameFont = pygame.font.SysFont(None, 30)
    text = gameFont.render(msg, True, red)
    gameBoard.blit(text, (10,10))
    #gameBoard.blit( frog , (x2 , y2) )

def snake(snakeList):
    print(snakeList)
    for i in range(len(snakeList)):
        pygame.draw.rect(gameBoard, red, [snakeList[i][0], snakeList[i][1], 50, 50])

black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
randomColor = (245,123,222)
#red, green, blue -> 0-255

x = 0
y = 0
width = 500
height = 250
moveX = 0
moveY = 0

frog = pygame.image.load('assets/frog.png')
sound = pygame.mixer.Sound('assets/point.wav')
x2 = random.choice(range(0,width - 50))
y2 = random.choice(range(0,height - 50))

#screen for game
gameBoard = pygame.display.set_mode((width,height))
#gameBoard.fill(randomColor)

while True:
    for event in pygame.event.get():
        #print(event)
        #event handling
        if event.type == pygame.QUIT:
            pygame.quit() #quit pygame
            quit() #quit python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    gameBoard.fill( white )
    # surface, color, [x,y,width,height], width
    #creation of object
    rect1 = pygame.draw.rect( gameBoard , red ,[ x , y , snakeWidth , 50 ])
    #rect = pygame.draw.rect(gameBoard, black, [x2,y2,50,50])
    rect2 = pygame.Rect([x2,y2,50,50])
    gameBoard.blit(frog, (x2,y2))
    displayScore( )

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]
    snake( snakeList )


    if rect1.colliderect(rect2):
        x2 = random.choice(range(0,width - 50))
        y2 = random.choice(range(0,height - 50))
        sound.play()
        counter += 1
        snakeLength += 10
        fps += 50


    #animation of object
    x += moveX
    y += moveY



    if x < -100:
        x = width
    elif y < -100:
        y = height
    elif x > width:
        x = -100
    elif y > height:
        y = -100


    '''if x < 0:
        quitGame()
    elif y < 0:
        quitGame()
    elif x > (width - 100):
        quitGame()
    elif y > (height - 100):
        quitGame()'''

    '''if x < 0:
        moveX = 1
    elif x > (width - 100):
        moveX = -1
    elif y < 0:
        moveY = 1
    elif y > (height - 100):
        moveY = -1'''

    pygame.display.update()
    clock.tick(fps)
