from random import randint
from PIL import Image as Img

import numpy as np


class Position:
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column


class Image:
    def __init__(self, pixels):
        self.pixels = []
        self.image = pixels
        self.width = pixels.shape[1]
        self.height = pixels.shape[0]
        # Transforming pixels to vector
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.pixels.append(pixels[y][x])


class Model:
    def __init__(self, data, tolerance=0):
        self.data = data
        self.tolerance = tolerance
        self.defaultWidth = data[0].width
        self.defaultHeight = data[0].height
        self.size = len(data)
        self.columns = self.defaultHeight * self.defaultWidth
        self.lastAdded = Position()
        self.nodes = []
        for row in range(0, self.size):
            self.nodes.append([])
            for columns in range(0, self.columns):
                self.nodes[row].append(None)

    def addNode(self, row, column, node):
        if (row > 0):
            for r in range(0, self.size):
                if (column == 0):
                    if (node.hasTheSameColor(self.getNode(r, column), self.tolerance)):
                        self.lastAdded = Position(r, column)
                        return
                    else:
                        break
                else:
                    if (node.hasTheSameColor(self.getNode(r, column), self.tolerance)):
                        self.getLastAddedNode().addNext(self.getNode(r, column))
                        self.getNode(r, column).addPrevious(self.getLastAddedNode())
                        self.lastAdded = Position(r, column)
                        return

        if (column > 0):
            self.getLastAddedNode().addNext(node)
            node.addPrevious(self.getLastAddedNode())

        self.nodes[row][column] = node
        self.lastAdded = Position(row, column)

    def getNode(self, row, column):
        return self.nodes[row][column]

    def getLastAddedNode(self):
        return self.nodes[self.lastAdded.row][self.lastAdded.column]

    def getNodeColor(self, row, column):
        return self.getNode(row, column).color

    def compile(self):
        rowName = ""
        for row in range(0, self.size):
            rowName += str(row) + "r"
            for column in range(0, self.columns):
                name = rowName + str(column)
                node = Node(self.data[row].pixels[column], name)
                self.addNode(row, column, node)
                print(str(row) + " compiled")

    def generate(self, number=1, folder="res", show=True):
        for n in range(0, number):
            startLocations = []

            for i in range(0, self.size - 1):
                if (self.nodes[i][0] is not None):
                    startLocations.append(self.nodes[i][0])

            startIndex = randint(0, len(startLocations))

            picture = []
            node = self.nodes[0][0]

            for y in range(0, self.defaultHeight):
                picture.append([])
                for x in range(0, self.defaultWidth):
                    picture[y].append(node.color)
                    node = node.getRandomNext()

            img = Img.fromarray(np.asarray(picture), 'RGB')
            img.save(folder + "/" + str(n) + ".jpg")


class Node:
    def __init__(self, color, name=""):
        self.name = name
        self.color = color
        self.next = []
        self.previous = []

    def addNext(self, node):
        self.next.append(node)

    def addPrevious(self, previous):
        self.previous.append(previous)

    def getRandomNext(self):
        if (len(self.next) == 0): return None
        return self.next[randint(0, len(self.next) - 1)]

    def hasTheSameColor(self, node, tolerance=0):

        if (node == None):
            return False

        nodeColor = 0
        selfColor = 0

        for c in range(0, len(self.color)):
            selfColor += self.color[c]
        for c in range(0, len(node.color)):
            nodeColor += node.color[c]

        if (abs(nodeColor - selfColor) > tolerance):
            return False

        return True

    def __str__(self):
        return self.name
