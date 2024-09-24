import math
import pygame

# Initialize Pygame
pygame.init()

points = []

black = (0, 0, 0)
white = (255, 255, 255)

xSize = 0
ySize = 0
circRad = 0
cellSize = 0

f = open("map1.txt", "r")
for x in f:
    if(x[0:1] == "g"):
        x = x[2:]
        space = x.find(" ")
        xSize = int(x[0:space])
        x = x[space+1:]
        space = x.find(" ")
        ySize = int(x[0:space])
        continue
    if(x[0:1] == "s"):
        x = x[2:]
        space = x.find(" ")
        circRad = int(x[0:space])
        x = x[space+1:]
        space = x.find(" ")
        cellSize = int(x[0:space])
        continue

    space = x.find(" ")
    red = int(x[0:space])
    x = x[space+1:]
    space = x.find(" ")
    green = int(x[0:space])
    x = x[space+1:]
    space = x.find(" ")
    blue = int(x[0:space])
    x = x[space+3:]
    space = x.find(" ")
    firstXPos = int(x[0:space])
    x = x[space+1:]
    space = x.find(" ")
    firstYPos = int(x[0:space])
    points.append((firstXPos, firstYPos, (red, green, blue)))
    x = x[space+3:]
    space = x.find(" ")
    secondXPos = int(x[0:space])
    x = x[space+1:]
    secondYPos = int(x[0:])
    points.append((secondXPos, secondYPos, (red, green, blue)))
    

screen_width = cellSize * xSize
screen_height = cellSize * ySize
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(black)


typeGrid = [[]]
colorGrid = [[]]
for i in range(xSize):
    typeGrid.append([])
    colorGrid.append([])
    for j in range(ySize):
        typeGrid[i].append(0)
        colorGrid[i].append(black)

for i in points:
    typeGrid[i[0]][i[1]] = 2
    colorGrid[i[0]][i[1]] = i[2]

def pixelPos(num):
    return num * cellSize + 40

def draw():
    for row in range(ySize):
        for col in range(xSize):
            x = col * cellSize
            y = row * cellSize
            if(typeGrid[row][col] == 2):
                pygame.draw.circle(screen, colorGrid[row][col], (pixelPos(row), pixelPos(col)), 40 - 4)
            pygame.draw.rect(screen, white, (x, y, cellSize, cellSize), 1)

draw()

pygame.display.flip()

curCelX = 0
curCelY = 0
pastCelX = 0
pastCelY = 0
pastPastCelX = 0
pastPastCelY = 0

inputs = (curCelX, curCelY, pastCelX, pastCelY, pastPastCelX, pastPastCelY, colorGrid[curCelX][curCelY], False)

def input(curCelX, curCelY, pastCelX, pastCelY, pastPastCelX, pastPastCelY):
    mouseY = pygame.mouse.get_pos()[1]
    mouseX = pygame.mouse.get_pos()[0]
    mousePressed = pygame.mouse.get_pressed()[0]

    futurecurCelX = (int) (mouseX / cellSize)
    futurecurCelY = (int) (mouseY / cellSize)

    if( (pastPastCelX != pastCelX or pastPastCelY != pastCelY) and (pastCelX != curCelX or pastCelY != curCelY)):
        pastPastCelX = pastCelX
        pastPastCelY = pastCelY

    if( (pastCelX != curCelX or pastCelY != curCelY) and (curCelX != futurecurCelX or curCelY != futurecurCelY)):
        pastCelX = curCelX
        pastCelY = curCelY

    curCelX = (int) (mouseX / cellSize)
    curCelY = (int) (mouseY / cellSize)
    if(colorGrid[curCelX][curCelY] != black):
        color = colorGrid[curCelX][curCelY]
    else:
        color = colorGrid[pastCelX][pastCelY]

    if( (colorGrid[curCelX][curCelY] == black) and ( ((abs(curCelX - pastCelX) >= 1) ) and ((curCelY - pastCelY) >= 1) ) ):
        return (curCelX, curCelY, pastCelX, pastCelY, pastPastCelX, pastPastCelY, colorGrid[pastCelX][pastCelY], False)
    elif(mousePressed):
        return (curCelX, curCelY, pastCelX, pastCelY, pastPastCelX, pastPastCelY, color, True)
    else:
        return (curCelX, curCelY, pastCelX, pastCelY, pastPastCelX, pastPastCelY, colorGrid[pastCelX][pastCelY], False)
    

# left down - 1 
# left up - 2
# up right - 3
# up left - 4
# left down - 5
# left up - 6
# down right - 7
# down right - 8
lastTurn = [False, False, False, False, False, False, False, False]
    
def DrawBoard(curCelX, curCelY, pastCelX, pastCelY, pastPastCelX, pastPastCelY, color, bleh):
    print(str(curCelX) + " " + str(curCelY) + " " + str(pastCelX) + " " + str(pastCelY) + " " + str([pastPastCelX]) + " " + str(pastPastCelY) + " " + str(color))
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
            colorGrid[curCelX][curCelY] = color
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
            colorGrid[curCelX][curCelY] = color
            return

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
            colorGrid[curCelX][curCelY] = color
            return

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
            colorGrid[curCelX][curCelY] = color
            return

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
            colorGrid[curCelX][curCelY] = color
            return

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
            colorGrid[curCelX][curCelY] = color
            return

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
            colorGrid[curCelX][curCelY] = color
            return

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
            colorGrid[curCelX][curCelY] = color
            return

    # draw normals
    if(typeGrid[curCelX][curCelY] != 2 and curCelX != pastCelX):
        pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad, pixelPos(curCelY) - circRad / 2, circRad * 2, circRad), 0)
        colorGrid[curCelX][curCelY] = color
        for i in range(len(lastTurn)):
            lastTurn[i] = False
    elif(typeGrid[curCelX][curCelY] != 2 and curCelY != pastCelY):
        pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad / 2, pixelPos(curCelY) - circRad, circRad, circRad * 2), 0)
        colorGrid[curCelX][curCelY] = color
        for i in range(len(lastTurn)):
            lastTurn[i] = False


first = True
# Game loop
running = True
while running:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed()
    
    last = inputs
    inputs = input(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5])


    if(inputs[-1]):
        DrawBoard(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], inputs[7])

    else:
        inputs = last
        continue

    if(keys[pygame.K_q]):
        break

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()