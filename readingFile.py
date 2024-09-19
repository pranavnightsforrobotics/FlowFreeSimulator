possibleColors = []
points = []

xSize = 0
ySize = 0

f = open("map2.txt", "r")
for x in f:
    if(x[0:1] == "g"):
        x = x[2:]
        xSize = int(x[0:1])
        x = x[2:]
        ySize = int(x[0:1])
        continue
    space = x.find(" ")
    red = int(x[0:space])
    x = x[space+1:]
    space = x.find(" ")
    green = int(x[0:space])
    x = x[space+1:]
    space = x.find(" ")
    blue = int(x[0:space])
    possibleColors.append((red, green, blue))
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
    

print(xSize)
print(ySize)


print(possibleColors)

print(points)