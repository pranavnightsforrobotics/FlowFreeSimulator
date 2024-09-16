import math
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 480
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set grid dimensions
grid_size = 6
cell_size = screen_width / grid_size

# 2d Matricies
colorGrid = [[0] * grid_size] * grid_size
typeGrid = [[0] * grid_size] * grid_size

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
pink = (255, 105, 180)
green = (0, 255, 0)
brown = (150, 75, 0)
colors = [blue, red, yellow, pink, green, brown]

# Clear the screen
screen.fill(black)

# Circle
circRad = 40
curCelX = 0
curCelY = 0
pastCelX = 0
pastCelY = 0
pastPastCelX = 0
pastPastCelY = 0
color = black


startPosX = cell_size / 2
startPosY = cell_size / 2
curPosX = startPosX
curPosY = startPosY
pastPosX = curPosX
pastPosY = curPosY
pastPastPosX = curPosX
pastPastPosY = curPosY

def pixelPos(num):
    return num * cell_size + circRad


# Draw the grid
for row in range(grid_size):
    typeGrid[row][0] = 2
    typeGrid[row][-1] = 2
    colorGrid[row][0] = colors[row]
    colorGrid[row][-1] = colors[row]
    for col in range(grid_size):
        x = col * cell_size
        y = row * cell_size
        if(typeGrid[row][col] == 2):
            pygame.draw.circle(screen, colorGrid[row][col], (pixelPos(row), pixelPos(col)), circRad - 4)
        pygame.draw.rect(screen, white, (x, y, cell_size, cell_size), 1)

def input():
    mouseY = pygame.mouse.get_pos[1]
    mouseX = pygame.mouse.get_pos[0]
    mousePressed = pygame.mouse.get_pressed()[0]

    if(pastPastCelX != pastCelX or pastPastCelY != pastCelY):
        pastPastCelXRet = pastCelX
        pastPastCelYRet = pastCelY

    pastCelXRet = curCelX
    pastCelYRet = curCelY

    curCelXRet = mouseX / cell_size
    curCelYRet = mouseY / cell_size
    if(abs(curCelXRet - pastCelX) > 1 or abs(curCelYRet - pastCelY) > 1):
        return False

    if(mousePressed):
        return (curCelXRet, curCelYRet, pastCelXRet, pastCelYRet, pastPastCelXRet, pastPastCelYRet, colorGrid[curPosX][curPosY])
    else:
        return False
    
def DrawBoard():#curCelX, curCelY, pastCelX, pastCelY, pastPastCelX, pastPastCelY, color):
    if((typeGrid[curCelX][curCelY] != 2) and (typeGrid[pastCelX][pastCelY] != 2)):
        if(curCelX == pastCelX and curCelY > pastCelY and pastPastCelX < pastCelX and lastTurn[0] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad * 2, circRad), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY), circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad / 2, pixelPos(curCelY) - circRad, circRad, circRad * 2), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[0] = True
            return

        # draw right to up
        elif(curCelX == pastCelX and curCelY < pastCelY and pastPastCelX < pastCelX and lastTurn[1] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad * 2, circRad), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad / 2, pixelPos(curCelY) - circRad, circRad, circRad * 2), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[1] = True

        # draw up to right
        elif(curCelX > pastCelX and curCelY == pastCelY and pastPastCelY > pastCelY and lastTurn[2] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad * 2), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY), circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad, pixelPos(curCelY) - circRad / 2, circRad * 2, circRad), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[2] = True

        # draw up to left
        elif(curCelX < pastCelX and curCelY == pastCelY and pastPastCelY > pastCelY and lastTurn[3] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad * 2), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY), circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad, pixelPos(curCelY) - circRad / 2, circRad * 2, circRad), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[3] = True

        # draw left to down
        elif(curCelX == pastCelX and curCelY > pastCelY and pastPastCelX > pastCelX and lastTurn[4] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad * 2, circRad), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY), circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad / 2, pixelPos(curCelY) - circRad, circRad, circRad * 2), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[4] = True

        # draw left to up
        elif(curCelX == pastCelX and curCelY < pastCelY and pastPastCelX > pastCelX and lastTurn[5] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad * 2, circRad), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad / 2, pixelPos(curCelY) - circRad, circRad, circRad * 2), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[5] = True

        # draw down to right
        elif(curCelX > pastCelX and curCelY == pastCelY and pastPastCelY < pastCelY and lastTurn[6] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad * 2), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad, pixelPos(curCelY) - circRad / 2, circRad * 2, circRad), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[6] = True

        # draw down to left
        elif(curCelX < pastCelX and curCelY == pastCelY and pastPastCelY < pastCelY and lastTurn[7] == False):
            pygame.draw.rect(screen, black, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad * 2), 0)
            pygame.draw.circle(screen, color, (pixelPos(pastCelX), pixelPos(pastCelY)), circRad / 2)
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad, pixelPos(pastCelY) - circRad / 2, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(pastCelX) - circRad / 2, pixelPos(pastCelY) - circRad, circRad, circRad))
            pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad, pixelPos(curCelY) - circRad / 2, circRad * 2, circRad), 0)
            for i in range(len(lastTurn)):
                lastTurn[i] = False
            lastTurn[7] = True

    # draw normals
    if(typeGrid[curCelX][curCelY] != 2 and curCelX != pastCelX):
        pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad, pixelPos(curCelY) - circRad / 2, circRad * 2, circRad), 0)
    elif(typeGrid[curCelX][curCelY] != 2 and curCelY != pastCelY):
        pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad / 2, pixelPos(curCelY) - circRad, circRad, circRad * 2), 0)


    

# left down - 1 
# left up - 2
# up right - 3
# up left - 4
# left down - 5
# left up - 6
# down right - 7
# down right - 8
lastTurn = [False, False, False, False, False, False, False, False]

# Game loop
running = True
while running:
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    mousePressed = pygame.mouse.get_pressed()[0]
    
    
    if(curPosX != pastPosX or curPosY != pastPosY):
        pastPastPosX = pastPosX
        pastPastPosY = pastPosY
    

    pastPosX = curPosX
    pastPosY = curPosY
    
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if(mousePressed and (abs(mouseX - curPosX) > 40 or abs(mouseY - curPosY) > 40)):
        if(mouseX > curPosX + 40 and curPosX < 440):
            curPosX += 80

        elif(mouseY < curPosY - 40 and curPosY > 40):
            curPosY -= 80

        elif(mouseX < curPosX - 40 and curPosX > 40):
            curPosX -= 80

        elif(mouseY > curPosY + 40 and curPosY < 440):
            curPosY += 80
    

    # print(pygame.mouse.get_pos())
    # print(pygame.mouse.get_pressed()[0])

    if(keys[pygame.K_q]):
        break
    

    # pygame.draw.circle(screen, black, (pastPosX, pastPosY), circRad)
    print(str(pastPastPosX) + " " + str(pastPastPosY) + " " + str(pastPosX) + " " + str(pastPosY) + " " + str(curPosX) + " " + str(curPosY))

    # draw right to down
    if((curPosX != startPosX or curPosY != startPosY) and curPosX == pastPosX and curPosY > pastPosY and pastPastPosX < pastPosX and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[0] == False):
        print("gah")
        pygame.draw.rect(screen, black, (pastPosX - circRad, pastPosY - circRad / 2, circRad * 2, circRad), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX - circRad, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad / 2, curPosY - circRad, circRad, circRad * 2), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[0] = True
    
    # draw right to up
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX == pastPosX and curPosY < pastPosY and pastPastPosX < pastPosX and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[1] == False):
        pygame.draw.rect(screen, black, (pastPosX - circRad, pastPosY - circRad / 2, circRad * 2, circRad), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX - circRad, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad / 2, curPosY - circRad, circRad, circRad * 2), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[1] = True

    # draw up to right
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX > pastPosX and curPosY == pastPosY and pastPastPosY > pastPosY and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[2] == False):
        pygame.draw.rect(screen, black, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad * 2), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad, curPosY - circRad / 2, circRad * 2, circRad), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[2] = True

    # draw up to left
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX < pastPosX and curPosY == pastPosY and pastPastPosY > pastPosY and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[3] == False):
        pygame.draw.rect(screen, black, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad * 2), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX - circRad, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad, curPosY - circRad / 2, circRad * 2, circRad), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[3] = True

    # draw left to down
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX == pastPosX and curPosY > pastPosY and pastPastPosX > pastPosX and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[4] == False):
        pygame.draw.rect(screen, black, (pastPosX - circRad, pastPosY - circRad / 2, circRad * 2, circRad), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad / 2, curPosY - circRad, circRad, circRad * 2), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[4] = True

    # draw left to up
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX == pastPosX and curPosY < pastPosY and pastPastPosX > pastPosX and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[5] == False):
        pygame.draw.rect(screen, black, (pastPosX - circRad, pastPosY - circRad / 2, circRad * 2, circRad), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad / 2, curPosY - circRad, circRad, circRad * 2), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[5] = True
    
    # draw down to right
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX > pastPosX and curPosY == pastPosY and pastPastPosY < pastPosY and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[6] == False):
        pygame.draw.rect(screen, black, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad * 2), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad, curPosY - circRad / 2, circRad * 2, circRad), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[6] = True

    # draw down to left
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX < pastPosX and curPosY == pastPosY and pastPastPosY < pastPosY and (pastPosX != startPosX or pastPosY != startPosY) and lastTurn[7] == False):
        pygame.draw.rect(screen, black, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad * 2), 0)
        pygame.draw.circle(screen, blue, (pastPosX, pastPosY), circRad / 2)
        pygame.draw.rect(screen, blue, (pastPosX - circRad, pastPosY - circRad / 2, circRad, circRad))
        pygame.draw.rect(screen, blue, (pastPosX - circRad / 2, pastPosY - circRad, circRad, circRad))
        pygame.draw.rect(screen, blue, (curPosX - circRad, curPosY - circRad / 2, circRad * 2, circRad), 0)
        for i in range(len(lastTurn)):
            lastTurn[i] = False
        lastTurn[7] = True
    
    

    # draw normals
    elif((curPosX != startPosX or curPosY != startPosY) and curPosX != pastPosX):
        pygame.draw.rect(screen, blue, (curPosX - circRad, curPosY - circRad / 2, circRad * 2, circRad), 0)
    elif((curPosX != startPosX or curPosY != startPosY) and curPosY != pastPosY):
        pygame.draw.rect(screen, blue, (curPosX - circRad / 2, curPosY - circRad, circRad, circRad * 2), 0)

    


    # pygame.draw.arc(screen, blue, (180, 20, 40, 40), 0, math.pi / 2, 20)
    # pygame.draw.circle(screen, black, (180, 60), 20)

    # pygame.draw.rect(screen, black, (170, 40, 10, 10))
    # pygame.draw.rect(screen, black, (190, 60, 10, 10))
    
    



    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()