# import time
# literals = [[False, False], [True, True], [False, True], [True, False]]

# grid = [[1, 0, 2, 3, 0],
#         [0, 2, 4, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [4, 3, 0, 0, 0]]

# nodes = []

# colors = [1, 2, 3, 4]

# class Node():
#     def __init__(self, terminal, blank, xPos, yPos, con1, con2, color):
#         self.terminal = terminal
#         self.blank = blank
#         self.xPos = xPos
#         self.yPos = yPos
#         self.con1 = con1
#         self.con2 = con2
#         self.color = color

#     def __str__(self):
#         return f"{self.color}"

# for i in range(len(grid)):
#     nodes.append([])
#     for j in range(len(grid[i])):
#         term = grid[i][j] != 0
#         blank = grid[i][j] == 0 
#         nodes[i].append(Node(term, blank, i, j, None, None, grid[i][j]))



# def func (literal1, literal2):
#     val = (literal1 or literal2) and (literal1 or not literal2) and (not literal1 or literal2)
#     return val

# for i in literals:
#     if(func(i[0], i[1])):
        # print(i)
    

# print(time.time())
# for i in range(1073741824):
#     if(i % 1000000 == 0):
#         print(i)
# print(time.time())

# for i in colors:
#     for x in range(len(nodes)):
#         for y in range(len(nodes[x])):
#             if(nodes[x][y].blank):
#                 if(x > 0 and nodes[x-1][y].terminal and nodes[x-1][y].color == i and nodes[x-1][y].con1 == None):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x-1][y]
#                     nodes[x-1][y].con1 = nodes[x][y]

#                 elif(y > 0 and nodes[x][y-1].terminal and nodes[x][y-1].color == i and nodes[x][y-1].con1 == None):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x][y-1]
#                     nodes[x][y-1].con1 = nodes[x][y]
                
#                 elif(x > 0 and nodes[x-1][y].color == i and nodes[x-1][y].con2 == None and not nodes[x-1][y].blank and not nodes[x-1][y].terminal):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x-1][y]
#                     nodes[x-1][y].con2 = nodes[x][y]

#                 elif(y > 0 and nodes[x][y-1].color == i and nodes[x][y-1].con2 == None and not nodes[x][y-1].blank and not nodes[x][y-1].terminal):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x][y-1]
#                     nodes[x][y-1].con2 = nodes[x][y]

#                 elif(x < 4 and nodes[x+1][y].terminal and nodes[x+1][y].color == i and nodes[x+1][y].con1 == None):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x+1][y]
#                     nodes[x+1][y].con1 = nodes[x][y]

#                 elif(y < 4 and nodes[x][y+1].terminal and nodes[x][y+1].color == i and nodes[x][y+1].con1 == None):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x][y+1]
#                     nodes[x][y+1].con1 = nodes[x][y]
                
#                 elif(x < 4 and nodes[x+1][y].color == i and nodes[x+1][y].con2 == None and not nodes[x+1][y].blank and not nodes[x+1][y].terminal):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x+1][y]
#                     nodes[x+1][y].con2 = nodes[x][y]

#                 elif(y < 4 and nodes[x][y+1].color == i and nodes[x][y+1].con2 == None and not nodes[x][y+1].blank and not nodes[x][y+1].terminal):
#                     nodes[x][y].blank = False
#                     nodes[x][y].color = i
#                     nodes[x][y].con1 = nodes[x][y+1]
#                     nodes[x][y+1].con2 = nodes[x][y]


            
                
# for i in nodes:
    # for j in i:
        # print(j, end=" ")
    # print()
    # 
  
import pycosat
import itertools


cnf = [[1, -5, 4], [-1, 5, 3, 4], [-3, -4], [2], [3, -4], [-1, 5]]

arr = []

grid = [["h", "h", "h", "h"],
        ["h", "h", "h", "h"],
        ["h", "h", "h", "h"],
        ["h", "h", "h", "h"]]

colors = [1, 2, 3]

def colorClauses(grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            yield(i, j, char)

def colorVar(i, j, color):
    return (i*len(grid) + j)*len(colors) + color + 1

def all_pairs(vars):
    return itertools.combinations(vars, 2)

# print(a for (a,b) in all_pairs(colors))
# print(a)

def no_two(var):
    return ((-a, -b) for (a, b) in all_pairs(var))


for i, j, char in colorClauses(grid):
    arr.append([colorVar(i, j, color) for color in range(len(colors))])

    var = (colorVar(i, j, color) for color in range(len(colors)))

    arr.extend(no_two(var))
    

list = pycosat.solve(arr)
print(list)

# print(arr)

# for sol in pycosat.itersolve(arr):
#     print(sol)