import numpy as np
import itertools
from sklearn import preprocessing


class DataPreparator():
    def __init__(self, data, empty_space=0):
        self.size = data.shape[0]
        self.item_count = data.shape[1] * data.shape[2]
        self.data = data
        self.empty_space = empty_space

    def prepare(self, normalize=True):
        data = self.vectorize(self.data, self.size, self.item_count)

        # Pro kazdy zaznam vytvorim dict
        X = []
        Y = []
        for i_item in range(0, self.size):

            dictionary = []
            combinations = []

            for i_placeholder in range(0, self.item_count):
                if data[i_item][i_placeholder] != self.empty_space:
                    dictionary.append([i_placeholder, data[i_item][i_placeholder]])

            for s_i in range(1, len(dictionary)):
                combinations.append(list(itertools.combinations(self.get_indicies(dictionary), s_i)))

            for c in combinations:
                for c_i in c:
                    x = []
                    for item in c_i:
                        x.append(self.get_by_key(item, dictionary))
                    y = self.get_y(dictionary, x)
                    x = self.fill_empty(x, self.empty_space, self.item_count)
                    for y_i in range(0, len(y)):
                        X.append(x)
                        Y.append(y[y_i])
        if normalize:
            normalized = self.normalize(X, Y)
            X = normalized['x']
            Y = normalized['y']
        return {'x': np.array(X), 'y': np.array(Y)}

    def normalize(self, x, y):
        normalized_X = preprocessing.normalize(np.array(x))
        return {'x': normalized_X, 'y': y}

    def vectorize(self, data, data_size, item_count):
        return np.reshape(data, (data_size, item_count))

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
            y.append(self.fill_empty(tmp_y, self.empty_space, self.item_count))

        return y

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
# Generating combinations
