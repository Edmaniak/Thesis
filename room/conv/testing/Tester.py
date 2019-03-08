import numpy as np


class Tester:

    def __init__(self, generator, convolutional_cores):
        self.generator = generator
        self.convolutional_cores = convolutional_cores
        pass

    # Testujeme přítomnost židlí kolem stolů
    # 0 3 0
    # 3 2 3
    # 0 3 0
    def test_one(self):
        default_space = np.array([
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
        ], int)

        x_start = 3
        x_end = 7
        y_start = 3
        y_end = 7

        for y_i in range(x_start, x_end):
            for x_i in range(y_start, y_end):
                test_space = np.copy(default_space)
                test_space[y_i][x_i] = 2
                for i in range(0, 4):
                    test_space = self.generator.generate_one(3, test_space, self.convolutional_cores)
                print("-EXAMPLE-" + " " + str(y_i + x_i + 1))
                print(test_space)

    # testing multiple tables in the scene
    def test_two(self):
        pass
