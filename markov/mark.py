from random import randint
import numpy as np


class Position:
	def __init__(self, row=0, column=0):
		self.row = row
		self.column = column


class Image:
	def __init__(self, pixels, width, height):
		self.pixels = []
		self.width = width
		self.height = height
		# Transforming pixels to vector
		for y in range(0, height):
			for x in range(0, width):
				self.pixels.append(pixels[y][x])


class Model:
	def __init__(self, data, columns=6):
		self.data = data
		self.size = len(data)
		self.columns = columns
		self.lastAdded = Position()
		self.nodes = []
		for row in range(0, self.size):
			self.nodes.append([])
			for columns in range(0, self.columns):
				self.nodes[row].append(None)

	def addNode(self, row, column, node):
		if (row > 0):
			if (row > 1):
				a =3
				pass
			for r in range(0, self.size):
				if(column == 0):
					if (node.hasTheSameColor(self.getNode(r, column))):
						self.lastAdded = Position(r, column)
						return
					else:
						break
				else:
					if (node.hasTheSameColor(self.getNode(r, column))):
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
		lastNode = None
		name = ""
		rowName = ""
		for row in range(0, self.size):
			if(row == 0): rowName += "A"
			else: rowName = "B"
			for column in range(0, self.columns):
				name = rowName + str(column)
				node = Node(self.data[row].pixels[column],name)
				self.addNode(row, column, node)

	def generate(self):
		image = np.zeros(50, 50)


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

	def hasTheSameColor(self,node, tolerance = 0):

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
