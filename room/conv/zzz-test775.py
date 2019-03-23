import numpy as np

from room.conv.Generator import Generator

# Testujeme zidle kolem stolu

default_space_3 = np.array([
	[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 3, 2, 3, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
	[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
	[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
], int)

unique_object_with_symbols = np.array([0, 1, 2, 3, 4, 5, 6, 9])
convolutional_cores = [(3, 3), (4, 4), (5, 5), (6, 6)]

generator = Generator("4", unique_object_with_symbols)

# najit souradnice na placement matici
test_space = np.copy(default_space_3)
test_space = generator.generate_one(5, test_space, convolutional_cores, False, visualise="both")
print("EXAMPLE: ")
print(test_space)
