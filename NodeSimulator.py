class DoubleNode:
    def __init__(self, x, y, pastNode):
        self.x = x
        self.y = y
        self.pastNode = pastNode

    def __str__(self):
        return f"{self.x}{self.y}"
    

def cutBack(node):
    cut = []
    curX = node.x
    curY = node.y
    cut.append([curX, curY])
    cur = node.pastNode
    cut.append([cur.x, cur.y])
    while(cur.x != curX or cur.y != curY):
        cur = cur.pastNode
        cut.append([cur.x, cur.y])

    cut.append(cur)
    return cut

currentNode = DoubleNode(0, 0, None)
currentNode = DoubleNode(1, 0, currentNode)
currentNode = DoubleNode(2, 0, currentNode)
currentNode = DoubleNode(3, 0, currentNode)
currentNode = DoubleNode(3, 1, currentNode)
currentNode = DoubleNode(3, 2, currentNode)
currentNode = DoubleNode(3, 3, currentNode)
currentNode = DoubleNode(2, 3, currentNode)
currentNode = DoubleNode(1, 3, currentNode)
currentNode = DoubleNode(1, 2, currentNode)
currentNode = DoubleNode(1, 1, currentNode)
currentNode = DoubleNode(1, 0, currentNode)

arr = cutBack(currentNode)
currentNode = arr[-1]
arr.pop(-1)
print(arr)
print(currentNode)
print(currentNode.pastNode)


