import random

import numpy as np

from room.conv.Generator import Generator

# Testujeme zidle kolem stolu
from room.conv.Visualiser import Visualiser

default_space = np.array([
	[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
	[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
])

default_space_placement = np.array([
	[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 8, 0, 1, 1, 1, 1, 1, 1, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 8, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 8, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 8, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 8, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 8, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 8, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 8, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 8, 0, 0, 0, 0, 0, 1, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
	[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
])


def test_x(array):
	last = array[0][0]
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			current = array[i][j]
			if last == 1 and current == 3:
				return False
			if last == 3 and current == 1:
				return False
			last = array[i][j]
	return True


def test_y(array):
	last = array[0][0]
	for j in range(array.shape[1]):
		for i in range(array.shape[0]):
			current = array[i][j]
			if last == 1 and current == 3:
				return False
			if last == 3 and current == 1:
				return False
			last = array[i][j]
	return True


unique_object_with_symbols = np.array([0, 1, 2, 3, 4, 5, 6, 9])
convolutional_cores = [(3, 3), (4, 4), (5, 5), (6, 6)]

generator = Generator("4", unique_object_with_symbols)
visualiser = Visualiser()
visualiser.visualise_space(default_space)
# najit souradnice na placement matici
coordinates = np.where(default_space_placement == 8)
for t in range(0, 20):
	test_space = np.copy(default_space)
	for j in range(0, 100):
		r = random.randint(0, len(coordinates[0]) - 1)
		test_space[coordinates[0][r]][coordinates[1][r]] = 2
		tables = np.where(test_space == 2)
		if tables[0].size == 4:
			break
	visualiser.visualise_space(test_space)
	for i in range(0, 4 * 4):
		test_space = generator.generate_one(3, test_space, convolutional_cores, False, visualise="both")
		if test_x(test_space) == False or test_y(test_space) == False:
			print("Iteration " + str(i) + " problem")
			break
