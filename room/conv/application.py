from room.conv.data_prep import DataPreparator
from room.conv.generator import Generator
from room.conv.test_data import data

preparator = DataPreparator(data, [(2, 2), (3, 3), (4, 4), (5, 5)])
#preparator.prepare_and_fit()

default_space = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

generator = Generator()
generator.generate(default_space, 10, preparator.convolution_cores)
