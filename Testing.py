import math
import pygame

# all our grids and maps are set up with [x][y] so therefore when visualizing

# [[ (0,0), (0, 1), (0,2) ],
#  [ (1,0), (1, 1), (1,2) ],
#  [ (2,0), (2, 1), (2,2) ]]

# so flip to left 90 degrees and horizontaly cut in middle and flip

# Node Class
class DoubleNode:
    def __init__(self, x, y, pastNode=None, head=None):
        self.x = x
        self.y = y
        self.pastNode = pastNode
        if(head == None and pastNode != None):
            self.head = pastNode.head
        else:
            self.head = head

    def __str__(self):
        return f"{self.x}{self.y}"

# use node that got cut to find its last accpectable pos
def gotCut(nodeCut):
    cut = []
    cut.append([nodeCut.x, nodeCut.y])
    nodeCut = nodeCut.pastNode
    cut.append(nodeCut)
    return cut
    
# use node that cut itself to get path to erase and current pos
def cutBack(node):
    cut = []
    curX = node.x
    curY = node.y
    reset = False
    if(curX == node.head.x and curY == node.head.y):
        reset = True
    # cut.append([curX, curY])
    cur = node.pastNode
    cut.append([cur.x, cur.y])
    while(cur.x != curX or cur.y != curY):
        cur = cur.pastNode
        cut.append([cur.x, cur.y])

    cut.pop(-1)
    cut.append(cur)

    return cut

def cutToStart(node):
    cut = []
    if(node.x == node.head.x and node.y == node.head.y):
        return cut
    cur = node
    cut.append([cur.x, cur.y])
    while(cur.x != node.head.x or cur.y != node.head.y):
        cur = cur.pastNode
        cut.append([cur.x, cur.y])

    cut.pop(-1)

    return cut

# Initialize Pygame
pygame.init()

points = []
colors = []

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
    colors.append((red, green, blue))
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

nodesDict = {}
for i in colors:
    nodesDict.update({i:None})

typeGrid = []
colorGrid = []
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
    for row in range(xSize):
        for col in range(ySize):
            x = row * cellSize
            y = col * cellSize
            if(typeGrid[row][col] == 2):
                pygame.draw.circle(screen, colorGrid[row][col], (pixelPos(row), pixelPos(col)), 40 - 4)
            pygame.draw.rect(screen, white, (x, y, cellSize, cellSize), 1)

def drawGrid():
    for row in range(xSize):
        for col in range(ySize):
            x = row * cellSize
            y = col * cellSize
            pygame.draw.rect(screen, white, (x, y, cellSize, cellSize), 1)

draw()

print(colorGrid)

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

    # global typeGrid
    # global colorGrid

    if(typeGrid[curCelX][curCelY] == 2):
        if(nodesDict.get(color) != None):
            if( abs(nodesDict.get(color).x - curCelX) + abs(nodesDict.get(color).y - curCelY) == 1):
                return
            curNode = nodesDict.get(color)
            print(curNode)
            arr = cutToStart(curNode)
            print(curNode.head.x)
            print(curNode.head.y)
            
            print("scoopy poopy")
            print(arr)            
            print("scoopy poopy")
            for i in arr:
                typeGrid[i[0]][i[1]] = 0
                colorGrid[i[0]][i[1]] = black
                pygame.draw.rect(screen, black, (pixelPos(i[0]) - circRad, pixelPos(i[1]) - circRad, circRad * 2, circRad * 2), 0)
            nodesDict.update({color : DoubleNode(curCelX, curCelY)})
        else:
            nodesDict.update({color : DoubleNode(curCelX, curCelY)})

    elif(typeGrid[curCelX][curCelY] == 1):
        if(colorGrid[curCelX][curCelY] == color):
            if(nodesDict.get(color).pastNode.x != pastCelX and nodesDict.get(color).pastNode.y != pastCelY):
                curNode = nodesDict.get(color)
                if(curNode.pastNode == None):
                    return(curCelX, curCelY, 0, 0, 0, 0)
                elif(curNode.pastNode.pastNode == None):
                    return(curCelX, curCelY, curNode.pastNode.x, curNode.pastNode.y, 0, 0)
                else:
                    return(curCelX, curCelY, curNode.pastNode.x, curNode.pastNode.y, curNode.pastNode.pastNode.x, curNode.pastNode.pastNode.y)
            curNode = nodesDict.get(color)
            curNode = DoubleNode(curCelX, curCelY, curNode)
            nodesDict.update({color : curNode})
            print(curNode)
            print(color)
            arr = cutBack(nodesDict.get(color))
            newNode = arr[-1]
            nodesDict.update({color: newNode})
            arr.pop(-1)
            for i in arr:
                typeGrid[i[0]][i[1]] = 0
                colorGrid[i[0]][i[1]] = black
                pygame.draw.rect(screen, black, (pixelPos(i[0]) - circRad, pixelPos(i[1]) - circRad, circRad * 2, circRad * 2), 0)
            curNode = nodesDict.get(color)
            print(curNode.pastNode)
            if(curNode.pastNode == None):
                return(curCelX, curCelY, 0, 0, 0, 0)
            elif(curNode.pastNode.pastNode == None):
                return(curCelX, curCelY, curNode.pastNode.x, curNode.pastNode.y, 0, 0)
            else:
                return(curCelX, curCelY, curNode.pastNode.x, curNode.pastNode.y, curNode.pastNode.pastNode.x, curNode.pastNode.pastNode.y)
        else:
            curNode = nodesDict.get(color)
            intersectingNode = nodesDict.get(colorGrid[curCelX][curCelY])
            newIntersect = gotCut(intersectingNode)
            nodesDict.update({colorGrid[curCelX][curCelY]: newIntersect[-1]})
            newIntersect.pop(-1)
            typeGrid[newIntersect[0][0]][newIntersect[0][1]] = 0
            colorGrid[newIntersect[0][0]][newIntersect[0][1]] = black
            curNode = DoubleNode(curCelX, curCelY, curNode)
            nodesDict.update({color: curNode})
            pygame.draw.rect(screen, black, (pixelPos(newIntersect[0][0]) - circRad, pixelPos(newIntersect[0][1]) - circRad, circRad * 2, circRad * 2), 0)

    else:
        curNode = nodesDict.get(color)
        if(typeGrid[curNode.x][curNode.y] == 2 and (curNode.x != curCelX or curNode.y != curCelY)):
            curNode = DoubleNode(curCelX, curCelY, curNode, curNode)
        elif((curNode.x != curCelX or curNode.y != curCelY)):
            curNode = DoubleNode(curCelX, curCelY, curNode)
        nodesDict.update({color : curNode})



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
            typeGrid[curCelX][curCelY] = 1
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
            typeGrid[curCelX][curCelY] = 1
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
            typeGrid[curCelX][curCelY] = 1
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
            typeGrid[curCelX][curCelY] = 1
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
            typeGrid[curCelX][curCelY] = 1
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
            typeGrid[curCelX][curCelY] = 1
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
            typeGrid[curCelX][curCelY] = 1
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
            typeGrid[curCelX][curCelY] = 1
            return

    # draw normals
    if(typeGrid[curCelX][curCelY] != 2 and curCelX != pastCelX):
        pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad, pixelPos(curCelY) - circRad / 2, circRad * 2, circRad), 0)
        colorGrid[curCelX][curCelY] = color
        typeGrid[curCelX][curCelY] = 1
        for i in range(len(lastTurn)):
            lastTurn[i] = False
    elif(typeGrid[curCelX][curCelY] != 2 and curCelY != pastCelY):
        pygame.draw.rect(screen, color, (pixelPos(curCelX) - circRad / 2, pixelPos(curCelY) - circRad, circRad, circRad * 2), 0)
        colorGrid[curCelX][curCelY] = color
        typeGrid[curCelX][curCelY] = 1
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
    lastCelX = inputs[0]
    lastCelY = inputs[1]
    inputs = input(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5])

    if(inputs[0] == lastCelX and inputs[1] == lastCelY):
        inputs = (inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], False)

    if(inputs[-1]):
        arr = DrawBoard(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], inputs[7])
        if(arr != None):
            inputs = (inputs[0], inputs[1], arr[2], arr[3], arr[4], arr[5], inputs[6], inputs[7])

    else:
        inputs = last
        continue

    if(keys[pygame.K_q]):
        break
    
    drawGrid()

    # Update the display
    pygame.display.flip()


print(nodesDict)
# print(nodesDict.get((255, 0, 0)))
curNode = nodesDict.get((255, 0, 0))
while(curNode != None):
    print(curNode)
    curNode = curNode.pastNode
# Quit Pygame
pygame.quit()