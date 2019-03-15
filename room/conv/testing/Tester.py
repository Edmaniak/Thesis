import csv
from random import randint
from room.conv.testing.random_multiple_tables import data as random_table_data

import numpy as np


class Tester:

    def __init__(self, generator, convolutional_cores):
        self.generator = generator
        self.convolutional_cores = convolutional_cores
        self.default_space_1 = np.array([
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

        self.default_space_2 = np.array([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])

        self.default_space_3 = np.array([
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
            [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        ], int)

    # Testujeme přítomnost židlí kolem stolů
    # 0 3 0
    # 3 2 3
    # 0 3 0
    def test_one(self):
        default_space = np.copy(self.default_space_1)

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
        data = np.array(random_table_data)
        for i_d in range(0, data.shape[0]):
            test_space = data[i_d]
            for i in range(0, 12):
                print("press")
                input()
                test_space = self.generator.generate_one(3, test_space, self.convolutional_cores)
                print(test_space)
            print("final")
            print(test_space)

    # testing table by wall
    def test_three(self):

        for i in range(2, 8):
            default_space = np.copy(self.default_space_1)
            default_space[2][i] = 2
            self.place_object_n_times(3, 4, False, default_space)

        for i in range(2, 8):
            default_space = np.copy(self.default_space_1)
            default_space[7][i] = 2
            self.place_object_n_times(3, 4, False, default_space)

        for i in range(2, 8):
            default_space = np.copy(self.default_space_1)
            default_space[i][2] = 2
            self.place_object_n_times(3, 4, False, default_space)

        for i in range(2, 8):
            default_space = np.copy(self.default_space_1)
            default_space[i][7] = 2
            self.place_object_n_times(3, 4, False, default_space)

    # Testing object 4 cupboard - to be at sides
    def place_object_n_times(self, object, n_object, inputt=False, default_scene=None):
        if default_scene is None:
            default_space = np.copy(self.default_space_3)
        else:
            default_space = default_scene
        test_space = np.copy(default_space)
        for i_obj in range(0, n_object):
            if inputt:
                print("press key to continue...")
                input()
            test_space = self.generator.generate_one(object, test_space, self.convolutional_cores)
            print("ITERATION RESULT : " + str(i_obj))
            print(test_space)
        print("RESULTS FOR OBJECT 4 PLACING: ")
        print(test_space)

    # generates random scenes with defined object count
    def test_generate_random_scenes(self, n_scenes, n_objects, identificator="data1"):
        default_space = np.copy(self.default_space_1)
        for i in range(0, n_scenes):
            test_space = np.copy(default_space)
            for o_i in range(0, n_objects):
                random_obj = randint(2, 5)
                test_space = self.generator.generate_one(random_obj, test_space, self.convolutional_cores)
            test_space_to_save = np.reshape(test_space, (1, test_space.size))
            with open('testing/random_scenes_data/' + identificator + '.csv', 'a') as x_file:
                x_writer = csv.writer(x_file, delimiter=";", lineterminator='\n')
                x_writer.writerow(test_space_to_save)
            print("RANDOM SCENE " + str(i))
            print(test_space)
