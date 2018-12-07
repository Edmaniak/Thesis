from random import randint
import numpy as np

class Position:
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column


class Model:
    def __init__(self, data):
        self.data = data
        self.size = data.size
        self.nodes = []
        self.lastAdded = Position()

    def addNode(self, row, column, node):
        if (row > 0):
            for r in range(0, self.size):
                if (node.color == self.getNodeColor(r, column) and column == 0):
                    self.lastAdded = Position(r, column)
                    return
                if (node.color == self.getNodeColor(r, column) and column > 0):
                    self.getLastAddedNode().addNext(self.getNode(r, column))
                    self.getNode(r, column).addPrevious(self.getLastAddedNode())
                    self.lastAdded = Position(r, column)

    def getNode(self, row, column):
        return self.nodes[row][column]

    def getLastAddedNode(self):
        return self.nodes[self.lastAdded.row][self.lastAdded.column]

    def getNodeColor(self, row, column):
        return self.getNode(row, column).color

    def compile(self):
        lastNode = None
        for row in range(0, self.size):
            for column in range(0, self.columns):
                node = Node(self.data[row].pixels[column])
                self.addNode()

    def generate(self):
        image = np.zeros(50,50)



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
        return self.next[randint(0, len(self.next))]
