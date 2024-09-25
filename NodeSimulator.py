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
    

def gotCut(nodeCut):
    cut = []
    cut.append([nodeCut.x, nodeCut.y])
    nodeCut = nodeCut.pastNode
    cut.append(nodeCut)
    return cut
    

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

currentNode = DoubleNode(0, 0)
head = currentNode
print(head)
currentNode = DoubleNode(1, 0, currentNode, head)
currentNode = DoubleNode(2, 0, currentNode)
currentNode = DoubleNode(3, 0, currentNode)
currentNode = DoubleNode(3, 1, currentNode)
currentNode = DoubleNode(3, 2, currentNode)
currentNode = DoubleNode(3, 3, currentNode)

newNode = DoubleNode(3, 4)
newNode = DoubleNode(3, 3, newNode)

arr = gotCut(newNode)
newNode = arr[-1]
arr.pop(-1)
print(newNode)
print(arr)


# currentNode = DoubleNode(2, 3, currentNode)
# currentNode = DoubleNode(1, 3, currentNode)
# currentNode = DoubleNode(1, 2, currentNode)
# currentNode = DoubleNode(1, 1, currentNode)
# currentNode = DoubleNode(1, 0, currentNode)
# currentNode = DoubleNode(0, 0, currentNode)


# arr = cutBack(currentNode)
# currentNode = arr[-1]
# arr.pop(-1)
# print(arr)
# print(currentNode)
# print(head)
# print(currentNode.pastNode)


