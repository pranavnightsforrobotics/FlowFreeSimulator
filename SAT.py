import pycosat
import itertools


cnf = [[1, -5, 4], [-1, 5, 3, 4], [-3, -4], [2], [3, -4], [-1, 5]]

arr = []

grid = [["R", " ", "G", "B"],
        [" ", " ", "B", " "],
        [" ", " ", " ", "G"],
        [" ", " ", " ", "R"]]

colors = {"R" : 0,
          "G" : 1,
          "B" : 2}

def colorClauses(grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            yield(i, j, char)
            

def colorVar(i, j, color):
    return (i*len(grid) + j)*len(colors) + color + 1

def all_pairs(vars):
    return itertools.combinations(vars, 2)

def decodeColorVar(num):
    key_list = list(colors.keys())
    val_list = list(colors.values())
    for i, j, char in colorClauses(grid):
        if(colorVar(i, j, (num - 1) % 3) == num):
            # print(num, i, j, char, colorVar(i, j, num -1 % 3))
            colNum = (num - 1) % 3
            # if(colNum == 0):
            #     colNum = 3
            position = val_list.index(colNum)
            col = key_list[position]
            return i, j, col

# print(a for (a,b) in all_pairs(colors))
# print(a)

def no_two(var):
    return ((-a, -b) for (a, b) in all_pairs(var))


for i, j, char in colorClauses(grid):

    # adding the color, if its a start color is mandated otherwise, it can be any of the options
    if(char != " "):
        arr.append([colorVar(i, j, colors.get(char))])
    else:
        arr.append([colorVar(i, j, color) for color in range(len(colors))])
        var = (colorVar(i, j, color) for color in range(len(colors)))

        # negate any combination of variables that lets 2 colors be true on 1 square
        arr.extend(no_two(var))
    
# print(arr)
sol = pycosat.solve(arr)
print(sol)

for i in (sol):
    if(i > 0):
        x, y, z = decodeColorVar(i)
        print(z, x, y)