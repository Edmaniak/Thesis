import numpy as np
import itertools
from sklearn import preprocessing


class DataPreparator():
    def __init__(self, data, empty_space=0):
        self.size = data.shape[0]
        self.positions_count = data.shape[1] * data.shape[2]
        self.data = self.vectorize(data, self.size, self.positions_count)
        self.unique_objects = np.unique(data)
        self.unique_count = self.unique_objects.shape[0]
        self.empty_space = empty_space

    def prepare_class(self, object_class, normalize=False):
        X = []
        Y = []
        # Pro všechny příklady:
        for i_item in range(0, self.size):
            print("Preparing class " + str(object_class) + " for example " + str(i_item));
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            dictionary = []
            combinations = []
            # generating dictionary of vector index + value
            # Vytvoř slovník
            for i_position in range(0, self.positions_count):
                # pokud se nejedná o prázdnou tj. nulovou pozici
                if self.data[i_item][i_position] != self.empty_space:
                    dictionary.append([i_position, self.data[i_item][i_position]])

            for s_i in range(1, len(dictionary)):
                combinations.append(list(itertools.combinations(self.get_indicies(dictionary), s_i)))

            for index, n_tice in enumerate(combinations):
                str_counter = index + 1
                print("Processing " + str(str_counter) + "-tice")
                for c_i in n_tice:
                    x = []
                    for item in c_i:
                        x.append(self.get_by_key(item, dictionary))
                    y = self.get_y_with_limitation(x, dictionary, object_class)
                    x = self.fill_empty(x, self.empty_space, self.positions_count)
                    for y_i in range(0, len(y)):
                        X.append(x)
                        Y.append(y[y_i])
            if normalize:
                normalized = self.normalize(X, Y)
                X = normalized['x']
                Y = normalized['y']

            return np.array([X, Y])

    def prepare_all(self):
        data = []
        # pro všechny jedinečné objekty vybrané ze všech příkladů
        for i_item in range(1, self.unique_count):
            # postupně připrav třídu
            data.append(self.prepare_class(self.unique_objects[i_item]))
        return data

    def prepare(self, normalize=True):
        data = self.vectorize(self.data, self.size, self.positions_count)
        self.prepare_class(1)

        # Pro kazdy zaznam vytvorim dict
        X = []
        Y = []
        for i_item in range(0, self.size):

            dictionary = []
            combinations = []

            for i_placeholder in range(0, self.positions_count):
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
                    x = self.fill_empty(x, self.empty_space, self.positions_count)
                    for y_i in range(0, len(y)):
                        X.append(x)
                        Y.append(y[y_i])
        if normalize:
            normalized = self.normalize(X, Y)
            X = normalized['x']
            Y = normalized['y']
        return {'x': np.array(X), 'y': np.array(Y)}

    def get_y_with_limitation(self, x, data, limitation):
        y = []
        for i_item in range(0, len(data)):
            if data[i_item][1] != limitation or data[i_item] in x:
                continue
            y.append(np.zeros(self.positions_count))
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
# Generating combinations
