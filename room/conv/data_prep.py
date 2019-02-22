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
        self.unique_objects = np.unique(self.data)
        self.clean_special_symbols(self.special_symbols)

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
                for unique_object in self.unique_objects:
                    if unique_object in data:
                        unique_indexes = np.where(data == unique_object)
                        for ui in unique_indexes:
                            for unique_index in ui:
                                x = np.copy(data)
                                x[unique_index] = 0
                                y = self.get_y_vector(unique_index, core)
                                X[unique_object].append(x)
                                Y[unique_object].append(y)
                    else:
                        x = np.copy(data)
                        y = np.zeros(core[0] * core[1])
                        X[unique_object].append(x)
                        Y[unique_object].append(y)
        return [X, Y]

    def prepare_and_fit(self, epochs=1000, ratio=1.25):
        data = self.prepare()
        self.learn(data[0], data[1], epochs, ratio)

    def learn(self, X, Y, epochs=200, ratio=1.25):

        # Defining model
        for i_x in X:
            x = np.array(X[i_x])
            y = np.array(Y[i_x])

            model = Sequential()
            model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
            model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
            model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
            model.add(Dense(y.shape[1], activation='softmax'))
            model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
            model.fit(x, y, epochs=epochs)

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

    def clean_special_symbols(self, special_symbols):
        indexes_to_clear = []
        for i in range(0, len(special_symbols)):
            indexes_to_clear.append(np.where(self.unique_objects == special_symbols[i]))
        self.unique_objects = np.delete(self.unique_objects, indexes_to_clear)

    def copy_array(self, array):
        result = []

        for item in array:
            result.append(item)

        return result
