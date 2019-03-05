import numpy as np
from keras import Sequential
from keras.layers import Dense
import pandas as pd
import itertools
import csv

from room.conv.Statistics import TrainingStatistics, StatisticalRecord


class DataPreparator:
    def __init__(self, data: np.array, convolution_cores=[], special_symbols=(0, 1)):
        self.data = data
        self.data_shape = data.shape
        self.data_width = data.shape[1]
        self.data_height = data.shape[2]
        self.data_count = data.shape[0]
        self.heuristic_limit = 500
        self.convolution_cores = convolution_cores
        self.special_symbols = special_symbols
        self.unique_objects = self.clean_special_symbols(np.unique(self.data), self.special_symbols)
        self.unique_objects_with_symbols = np.delete(np.unique(self.data), np.where(np.unique(self.data) == 0))
        self.training_statistics = TrainingStatistics(convolution_cores, self.unique_objects)

    def combinate_and_save(self, combinations, unique_indexes, shape, data, unique_object_key):
        working_x = []
        count_of_data = 0
        count_of_working_data = 0
        for comb_i in range(0, len(combinations)):
            for tuple_i in range(0, len(combinations[comb_i])):
                working_x.append([])
                count_of_working_data += 1
                for unique_indexes_i in range(0, len(unique_indexes)):
                    if not unique_indexes[unique_indexes_i] in combinations[comb_i][tuple_i]:
                        working_x[tuple_i + comb_i].append(unique_indexes[unique_indexes_i])
            if count_of_working_data > self.heuristic_limit:
                break

        for working_x_i in range(0, len(working_x)):
            v_x = np.copy(data)

            for x_i in range(0, len(working_x[working_x_i])):
                v_x[working_x[working_x_i][x_i]] = self.get_default_background(unique_object_key)
                v_y = np.zeros(shape[0] * shape[1], int)
                v_y[working_x[working_x_i][x_i]] = 1

                count_of_data += 1
                # Saving x
                with open('data/y' + str(shape[0]) + str(shape[1]) + str(unique_object_key) + '.csv', 'a') as y_file:
                    y_writer = csv.writer(y_file, delimiter=";", lineterminator='\n')
                    y_writer.writerow(v_y)

                # Saving y
                with open('data/x' + str(shape[0]) + str(shape[1]) + str(unique_object_key) + '.csv', 'a') as x_file:
                    x_writer = csv.writer(x_file, delimiter=";", lineterminator='\n')
                    x_writer.writerow(self.transform_to_normal_form(v_x, shape))

                if count_of_data > self.heuristic_limit:
                    print("heuristic action")
                    return count_of_data
        return count_of_data

    def prepare(self):
        cores = self.convolution_cores
        for core_i in range(0, len(cores)):
            # Generating x and y data
            for i in range(0, self.data_count):
                example_generated_data_count = 0
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
                            example_generated_data_count += self.combinate_and_save(combinations, unique_indexes,
                                                                                    cores[core_i], data, unique_object)

                print("example " + str(i + 1) + " for core " + str(
                    self.convolution_cores[core_i]) + " DONE - " + str(
                    example_generated_data_count))

            print("core " + str(self.convolution_cores[core_i]) + " DONE")
        print("TRAINING DONE")

    def transform_to_normal_form(self, x_vector, core_shape):
        vector_size = core_shape[0] * core_shape[1] * self.unique_objects_with_symbols.size
        vector = np.zeros(vector_size, int)
        for i in range(0, len(x_vector)):
            # Floor
            if x_vector[i] != 0:
                offset = np.where(self.unique_objects_with_symbols == x_vector[i])[0][0]
                object_position = (i * self.unique_objects_with_symbols.size) + offset
                vector[object_position] = 1
        return vector

    def fit(self, epochs):
        for core_i, core in enumerate(self.convolution_cores):
            for class_i, class_id in enumerate(self.unique_objects):
                data = self.load_data(core[0], core[1], class_id)
                core_width = core[0]
                core_height = core[1]
                x = data[0]
                y = data[1]

                # Printing status
                print("Training model class " + str(class_id) + "( core > " + str(core) + " ) - " + str(x.shape[0]))

                # Defining model
                model = Sequential()
                model.add(Dense(int(x.shape[1]), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(int(x.shape[1]), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(int(x.shape[1]), input_dim=x.shape[1], activation='relu'))
                model.add(Dense(y.shape[1], activation='softmax'))

                # Compiling model
                model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
                result = model.fit(x, y, epochs=epochs, verbose=2)

                # Printing status
                print("Training model class " + str(class_id) + "( core > " + str(core) + " )" + " - DONE")

                # Printing statistics TODO fix
                accuracy = result.history.get('acc')[len(result.history.get('acc')) - 1]
                self.training_statistics.add_core_class(StatisticalRecord(core_i, class_i), accuracy)
                print("statistics: " + str(self.training_statistics.get_average_accuracy()))

                # Saving model to array
                self.save_model(model, core_width, core_height, class_id)

                # Printing statistisc summary
        self.training_statistics.print_summary()

    def load_data(self, core_width, core_height, class_id):
        x = np.array(
            pd.read_csv("data/x" + str(core_width) + str(core_height) + str(class_id) + ".csv", delimiter=";"),
            dtype=int)
        y = np.array(pd.read_csv("data/y" + str(core_width) + str(core_height) + str(class_id) + ".csv", delimiter=";"),
                     dtype=int)
        return [x, y]

    def prepare_and_fit(self, epochs=200, ratio=2):
        self.prepare()
        self.fit(epochs)

    def save_model(self, model, core_width, core_height, class_id):
        model.save_weights("networks/class" + str(class_id) + str(core_width) + str(core_height) + '.h5')
        model_json = model.to_json()
        with open("networks/class" + str(class_id) + str(core_width) + str(core_height) + '.json', "w") as json_file:
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
