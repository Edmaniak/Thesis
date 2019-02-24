from room.conv.data_prep import DataPreparator
from room.conv.generator import Generator
from room.conv.test_data import data
import numpy as np
preparator = DataPreparator(data, [(3, 3), (4, 4)])
preparator.prepare_and_fit()

default_space = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
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
generator.test_prediction(np.array(to_test_3), 3, 0)
generator.test_prediction(np.array(to_test_4), 3, 1)
# generator.generate(default_space, 10, [(3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])
