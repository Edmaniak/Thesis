from room.conv.testing.Tester import Tester
from room.conv.data_prep import DataPreparator
from room.conv.generator import Generator
from room.conv.test_data import data

cores = [(2, 2), (3, 3), (4, 4), (5, 5)]

# Tuplets form (rows, columns)
preparator = DataPreparator(data, cores)
preparator.prepare_and_fit()
# preparator.fit(100)

default_space = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

generator = Generator(preparator.unique_objects_with_symbols)
# generator.test_prediction(np.array(to_test_3), 3, 0)
# generator.test_prediction(np.array(to_test_4), 3, 1)
# generator.generate(default_space, 10, [(2, 2), (3, 3), (4, 4), (5, 5)])
tester = Tester(generator, cores)
tester.test_one()
