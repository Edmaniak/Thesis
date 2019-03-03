import numpy as np
from keras import Sequential
from keras.layers import Dense
from keras import backend as K
import tensorflow as tf
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
        K.tensorflow_backend._get_available_gpus()

    def get_x_combination_vector(self, combinations, unique_indexes, shape, data, unique_object_key):
        working_x = []
        result_y = []
        result_x = []
        for comb_i in range(0, len(combinations)):
            for tuple_i in range(0, len(combinations[comb_i])):
                working_x.append([])
                for unique_indexes_i in range(0, len(unique_indexes)):
                    if not unique_indexes[unique_indexes_i] in combinations[comb_i][tuple_i]:
                        working_x[tuple_i + comb_i].append(unique_indexes[unique_indexes_i])

        for working_x_i in range(0, len(working_x)):
            v_x = np.copy(data)

            for x_i in range(0, len(working_x[working_x_i])):
                v_x[working_x[working_x_i][x_i]] = self.get_default_background(unique_object_key)
                v_y = np.zeros(shape[0] * shape[1], int)
                v_y[working_x[working_x_i][x_i]] = 1
                result_y.append(v_y)

            for x_i in range(0, len(working_x[working_x_i])):
                result_x.append(v_x)

        return [result_x, result_y]

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

                            result = self.get_x_combination_vector(combinations, unique_indexes, cores[core_i], data,
                                                                   unique_object)

                            prepared_data[core_i][u_obj_i][0].extend(result[0])
                            prepared_data[core_i][u_obj_i][1].extend(result[1])

        return prepared_data

    def transform_to_normal_form(self,x_vector, y_vector):


    def prepare_and_fit(self, epochs=200, ratio=2):
        data = self.prepare()
        for core_i in range(0, len(data)):
            for class_i in range(0, len(data[core_i])):
                # Getting x and y data
                x = np.array(data[core_i][class_i][0])
                y = np.array(data[core_i][class_i][1])

                # Printing status
                print("Training model class " + str(self.get_unique_object_key(class_i)) + "( core > " + str(
                    self.convolution_cores[core_i]) + " ) - " + str(data[core_i][class_i][0].size))

                # Defining model
                model = Sequential()
                model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(int(x.shape[1] * ratio), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(y.shape[1], activation='softmax'))

                # Compiling model
                model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
                result = model.fit(x, y, epochs=epochs, verbose=2)

                # Printing status
                print("Training model class " + str(self.get_unique_object_key(class_i)) + "( core > " + str(
                    self.convolution_cores[core_i]) + " )" + " - DONE")

                # Printing statistics TODO fix
                accuracy = result.history.get('acc')[len(result.history.get('acc')) - 1]
                self.training_statistics.add_core_class(StatisticalRecord(core_i, class_i), accuracy)
                print("statistics: " + str(self.training_statistics.get_average_accuracy()))

                # Saving model to array
                self.save_model(model, self.convolution_cores[core_i][0], self.convolution_cores[core_i][1], class_i)

        # Printing statistisc summary
        self.training_statistics.print_summary()

    def save_model(self, model, core_width, core_height, class_i):
        model.save_weights(
            "networks/class" + str(self.get_unique_object_key(class_i)) + str(core_width) + str(core_height) + '.h5')
        model_json = model.to_json()
        with open("networks/class" + str(self.get_unique_object_key(class_i)) + str(core_width) + str(
                core_height) + '.json',
                  "w") as json_file:
            json_file.write(model_json)

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
        width = core[1]
        height = core[0]
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

    # TODO objectify it!
    def get_default_background(self, object_key):
        if object_key == 5 or object_key == 6:
            return 1
        return 0

    def generate_zeros(self, number):
        array = []
        for i in range(0, number):
            array.append(0)
        return array
