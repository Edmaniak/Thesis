from room.conv.data_prep import DataPreparator
from room.conv.generator import Generator
from room.conv.test_data import data
import numpy as np

cores = [(2, 2), (3, 3), (4, 4), (5, 5)]

# Tuplets form (rows, columns)
preparator = DataPreparator(data, cores)
preparator.prepare_and_fit()

default_space = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

to_test_3 = [
    [0, 0, 0],
    [0, 2, 0],
    [0, 0, 0]
]

to_test_4 = [
    [0, 2, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

generator = Generator()
# generator.test_prediction(np.array(to_test_3), 3, 0)
# generator.test_prediction(np.array(to_test_4), 3, 1)
generator.generate(default_space, 10, [(2, 2), (3, 3), (4, 4)])
