import numpy as np
from keras import Sequential
from keras.layers import Dense
import itertools

from room.conv.Statistics import TrainingStatistics, StatisticalRecord


class DataPreparator:
    def __init__(self, data: np.array, convolution_cores=[], special_symbols=(0, 1)):
        self.data = data
        self.data_shape = data.shape
        self.data_width = data.shape[1]
        self.data_height = data.shape[2]
        self.data_count = data.shape[0]
        self.convolution_cores = convolution_cores
        self.special_symbols = special_symbols
        self.unique_objects = self.clean_special_symbols(np.unique(self.data), self.special_symbols)
        self.training_statistics = TrainingStatistics(convolution_cores, self.unique_objects)

    def get_y_vector(self, position_indexes, unique_indexes, shape):
        v = np.zeros(shape[0] * shape[1], int)
        v[position_index] = 1
        return v

    def prepare(self):
        prepared_data = []
        cores = self.convolution_cores
        for core_i in range(0, len(cores)):

            # Generating placeholders
            prepared_data.append([])
            for unique_object in self.unique_objects:
                prepared_data[core_i].append([[], []])


            # Generating x and y data
            for i in range(0, self.data_count):
                tmp_data = self.iterate_array(self.data[i], cores[core_i])
                for data in tmp_data:
                    for u_obj_i in range(0, len(self.unique_objects)):
                        if self.unique_objects[u_obj_i] in data:
                            unique_object = self.unique_objects[u_obj_i]
                            unique_indexes = np.where(data == unique_object)[0]
                            combinations = []
                            for c_i in range(0, len(unique_indexes)):
                                a = list(itertools.combinations(unique_indexes, c_i))
                                combinations.append(a)
                            for unique_index in unique_indexes:
                                x = np.copy(data)
                                x[unique_index] = 0
                                y = self.get_y_vector(unique_index, cores[core_i])
                                prepared_data[core_i][u_obj_i][0].append(x)
                                prepared_data[core_i][u_obj_i][1].append(y)

        return prepared_data

    def prepare_and_fit(self, epochs=1000, ratio=2):
        data = self.prepare()
        for core_i in range(0, len(data)):
            for class_i in range(0, len(data[core_i])):
                print("Training model class " + str(self.get_unique_object_key(class_i)) + "( core > " + str(
                    self.convolution_cores[core_i]) + " )")

                x = np.array(data[core_i][class_i][0])
                y = np.array(data[core_i][class_i][1])

                model = Sequential()
                model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(y.shape[1], activation='softmax'))

                model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
                result = model.fit(x, y, epochs=epochs, verbose=2)

                print("Training model class " + str(self.get_unique_object_key(class_i)) + "( core > " + str(
                    self.convolution_cores[core_i]) + " )" + " - DONE")
                accuracy = result.history.get('acc')[len(result.history.get('acc')) - 1]
                self.training_statistics.add_core_class(StatisticalRecord(core_i, class_i), accuracy)
                print("statistics: " + str(self.training_statistics.get_average_accuracy()))

                # Saving model to array
                model.save_weights("networks/class" + str(self.get_unique_object_key(class_i)) + str(core_i) + '.h5')
                model_json = model.to_json()
                with open("networks/class" + str(self.get_unique_object_key(class_i)) + str(core_i) + '.json',
                          "w") as json_file:
                    json_file.write(model_json)

        self.training_statistics.print_summary()



    def get_unique_object_key(self, index):
        return self.unique_objects[index]

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

    def clean_special_symbols(self, objects, special_symbols):
        indexes_to_clear = []
        for i in range(0, len(special_symbols)):
            indexes_to_clear.append(np.where(objects == special_symbols[i]))
        return np.delete(objects, indexes_to_clear)

    def copy_array(self, array):
        result = []

        for item in array:
            result.append(item)

        return result
