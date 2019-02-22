import numpy as np
from keras import Sequential
from keras.layers import Dense


class DataPreparator:
    def __init__(self, data: np.array, convolution_cores=(), special_symbols=(0, 1)):
        self.data = data
        self.data_shape = data.shape
        self.data_width = data.shape[1]
        self.data_height = data.shape[2]
        self.data_count = data.shape[0]
        self.convolution_cores = convolution_cores
        self.special_symbols = special_symbols
        # Unique objects without wall (1) and empty (0)
        self.unique_objects = self.clean_special_symbols(np.unique(self.data), self.special_symbols)
        # Unique objects without empty space (0)
        self.unique_objects_with_symbols = np.delete(np.unique(self.data), np.where(np.unique(self.data) == 0))

    def prepare(self):
        X = {}
        Y = {}
        core = (3, 3)
        for unique_object in self.unique_objects:
            X[unique_object] = []
            Y[unique_object] = []
        for i in range(0, self.data_count):
            tmp_data = self.iterate_array(self.data[i], core)
            for data in tmp_data:
                x_vector = self.spread_objects_to_vector(data, core)
                for unique_object in self.unique_objects:
                    # Consider this condition TODO
                    if unique_object in data:

                        unique_indexes_x = self.get_unique_object_indexes(unique_object, x_vector)
                        for unique_index in unique_indexes_x:
                            x_vector[unique_index] = 0
                            X[unique_object].append(x_vector)

                        unique_indexes_y = np.where(data == unique_object)[0]
                        for unique_index in unique_indexes_y:
                            y = self.get_y_vector(unique_index, core)
                            Y[unique_object].append(y)
                    # else:
                    #     x = x_vector
                    #     y = np.zeros(core[0] * core[1])
                    #     X[unique_object].append(x)
                    #     Y[unique_object].append(y)
        return [X, Y]

    def prepare_and_fit(self, epochs=200, ratio=1.25):
        data = self.prepare()
        self.learn(data[0], data[1], epochs, ratio)

    def learn(self, X, Y, epochs=200, ratio=1.25):

        # Defining model
        for i_x in X:
            print("Training class " + str(i_x))
            x = np.array(X[i_x])
            y = np.array(Y[i_x])

            model = Sequential()
            model.add(Dense(int(x.shape[1] * 1), input_dim=x.shape[1], activation='relu'))
            model.add(Dense(int(x.shape[1] * 1), input_dim=x.shape[1], activation='relu'))
            model.add(Dense(y.shape[1], activation='softmax'))
            model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
            model.fit(x, y, epochs=epochs, verbose=2)
            print("Training class " + str(i_x) + " done")


            # Saving model to array
            model.save_weights("networks/class" + str(i_x) + '.h5')
            model_json = model.to_json()
            with open("networks/class" + str(i_x) + '.json', "w") as json_file:
                json_file.write(model_json)

    def get_y_vector(self, position_index, shape):
        v = np.zeros(shape[0] * shape[1])
        v[position_index] = 1
        return v

    def get_unique_objects_from_array(self, array):
        array = np.unique(array)
        unique_objects = []
        for i in range(0, len(array)):
            if array[i] in self.unique_objects:
                unique_objects.append(array[i])
        return unique_objects

    def spread_objects_to_vector(self, data, core_shape):
        vector_size = core_shape[0] * core_shape[1] * self.unique_objects_with_symbols.size
        vector = np.zeros(vector_size, int)
        for i in range(0, len(data)):
            # Floor
            if data[i] != 0:
                offset = np.where(self.unique_objects_with_symbols == data[i])[0][0]
                object_position = (i * self.unique_objects_with_symbols.size) + offset
                vector[object_position] = 1
        return vector

    def get_unique_object_indexes(self, unique_object, x_vector):
        start = np.where(self.unique_objects_with_symbols == unique_object)[0][0]
        iterator = self.unique_objects_with_symbols.size
        indexes = []
        i = start
        while i < x_vector.size:
            if x_vector[i] == 1:
                indexes.append(i)
            i = i + iterator
        return indexes

    def iterate_array(self, example, core: tuple):
        width = core[0]
        height = core[1]
        results_x = []
        iterator = -1
        for c_y in range(0, self.data_height - height + 1):
            for c_x in range(0, self.data_width - width + 1):
                iterator += 1
                results_x.append([])
                for i in range(0, height):
                    for j in range(0, width):
                        results_x[iterator].append(example[i + c_y][j + c_x])
        return np.array(results_x)

    def clean_special_symbols(self, original_unique_objects, special_symbols):
        indexes_to_clear = []
        for i in range(0, len(special_symbols)):
            indexes_to_clear.append(np.where(original_unique_objects == special_symbols[i]))
        return np.delete(original_unique_objects, indexes_to_clear)

    def copy_array(self, array):
        result = []

        for item in array:
            result.append(item)

        return result
