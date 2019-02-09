import numpy as np
import itertools
from sklearn import preprocessing
import csv
import operator as op
from functools import reduce


class DataPreparator():
    def __init__(self, data, empty_space=0):
        self.size = data.shape[0]
        self.positions_count = data.shape[1] * data.shape[2]
        self.data = self.vectorize(data, self.size, self.positions_count)
        self.unique_objects = np.unique(data)
        self.unique_count = self.unique_objects.shape[0]
        self.empty_space = empty_space

    def prepare_class(self, object_class):
        # X = []
        # Y = []
        # Pro všechny příklady:
        for i_item in range(0, self.size):
            real_item_id = i_item + 1
            print("Preparing class " + str(object_class) + " for example " + str(real_item_id))
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            dictionary = []
            combinations = []
            # generating dictionary of vector index + value
            # Vytvoř slovník
            for i_position in range(0, self.positions_count):
                # pokud se nejedná o prázdnou tj. nulovou pozici
                if self.data[i_item][i_position] != self.empty_space:
                    dictionary.append([i_position, self.data[i_item][i_position]])

            # HEURISTIKA KVULI KOMBINACIM
            # Nabizi se nahodne rozsekat slovnik na nekolik skupin a v ramci nich nagenerovat kombinace? To asi ne
            # Omezit to na kontext poslednich tri? to bude asi nic moc
            # Omezit to na pocet kombinaci ----> ZKUSME TO

            # Vygeneruj kombinace jednotlivych n-tic
            for s_i in range(1, len(dictionary)):
                combination_count = self.ncr(len(dictionary), s_i)
                if combination_count > 2000:
                    real_n_tice = s_i + 1
                    print("kombinace " + str(real_n_tice) + " skipped")
                    combinations.append(list())
                    continue
                combinations.append(list(itertools.combinations(self.get_indicies(dictionary), s_i)))

            # Nageneruj předpoklady X a vytvoř k nim vektor(y) Y
            for index, n_tice in enumerate(combinations):
                str_counter = index + 1
                print("Processing " + str(str_counter) + "-tice ")
                for c_i in n_tice:
                    x = []
                    for item in c_i:
                        x.append(self.get_by_key(item, dictionary))
                    y = self.get_y_with_limitation(x, dictionary, object_class)
                    x = self.fill_empty(x, self.empty_space, self.positions_count)
                    for y_i in range(0, len(y)):
                        with open('model/x' + str(object_class) + '.csv', 'a') as x_file:
                            x_writer = csv.writer(x_file, delimiter=";", lineterminator='\n')
                            x_writer.writerow(x)
                        with open('model/y' + str(object_class) + '.csv', 'a') as y_file:
                            y_writer = csv.writer(y_file, delimiter=";", lineterminator='\n')
                            y_writer.writerow(y[y_i])
                    # if normalize:
                    #     normalized = self.normalize(X, Y)
                    #     X = normalized['x']
                    #     Y = normalized['y']

                    # return np.array([X, Y])

    def prepare_all(self):
        for i_item in range(1, self.unique_count):
            self.prepare_class(self.unique_objects[i_item])

    def get_y_with_limitation(self, x, data, limitation):
        y = []
        for i_item in range(0, len(data)):
            if data[i_item][1] != limitation or data[i_item] in x:
                continue
            y.append(np.zeros(self.positions_count, dtype=int))
            y[len(y) - 1][data[i_item][0]] = 1
        return y

    def get_y(self, data, x):
        y = []
        not_allowed = []

        for data_x in x:
            not_allowed.append(data_x[0])

        for item in data:
            tmp_y = self.copy_array(x)
            if item[0] in not_allowed:
                continue
            tmp_y.append(item)
            y.append(self.fill_empty(tmp_y, self.empty_space, self.positions_count))

        return y

    def normalize(self, x, y):
        normalized_X = preprocessing.normalize(np.array(x))
        return {'x': normalized_X, 'y': y}

    def vectorize(self, data, data_size, item_count):
        return np.reshape(data, (data_size, item_count))

    def fill_empty(self, data, empty_sign, size):
        array = []

        for i in range(0, size):
            array.append(empty_sign)

        for item in data:
            array[item[0]] = item[1]

        return array

    def copy_array(self, array):
        result = []

        for item in array:
            result.append(item)

        return result

    def get_indicies(self, array):
        result = []

        for item in array:
            result.append(item[0])

        return result

    def get_tmp_selection(self, array, size):
        result = []

        for i in range(0, size):
            result.append(array[i])

        return result

    def get_by_key(self, key, array):
        for i in range(0, len(array)):
            if array[i][0] == key:
                return array[i]
        return None

    def ncr(self, n, r):
        r = min(r, n - r)
        numer = reduce(op.mul, range(n, n - r, -1), 1)
        denom = reduce(op.mul, range(1, r + 1), 1)
        return numer / denom
# Generating combinations
