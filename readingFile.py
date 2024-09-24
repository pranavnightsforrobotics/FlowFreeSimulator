import pygame

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

typeGrid = [[]]
colorGrid = [[]]
for i in range(xSize):
    typeGrid.append([])
    colorGrid.append([])
    for j in range(ySize):
        typeGrid[i].append(0)
        colorGrid[i].append([black])

for i in points:
    typeGrid[i[0]][i[1]] = 2
    colorGrid[i[0]][i[1]] = i[2]

print(points)

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

running = True

while(running):

    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()