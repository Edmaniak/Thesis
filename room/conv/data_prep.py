import numpy as np


class DataPreparator:
    def __init__(self, data: np.array, convolution_cores=(), special_symbols=(0, 1)):
        self.data = data
        self.data_shape = data.shape
        self.data_width = data.shape[1]
        self.data_height = data.shape[2]
        self.data_count = data.shape[0]
        self.convolution_cores = convolution_cores
        self.special_symbols = special_symbols
        self.unique_objects_keys = np.unique(self.data)


    def prepare(self):
        results_x = []
        for i in range(0, self.data_count):
            results_x.append(self.iterate_array(self.data[i], (3, 3)))

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
