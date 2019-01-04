import math
import matplotlib.pyplot as plt
from PIL import Image as Img

import numpy as np


class Model:
    def __init__(self, data):
        self.data = np.array(data)
        self.data_shape = self.data.shape
        self.data_count = self.data.shape[0]
        self.data_height = self.data.shape[1]
        self.data_width = self.data.shape[2]
        self.unique_pixels = np.unique(self.data)
        self.unique_pixel_count = np.unique(self.data).size
        self.matrix_size = self.data_width * self.data_height * self.unique_pixel_count
        self.matrix = np.zeros((self.matrix_size, self.matrix_size))

    def compile(self, visualise=False):
        for data in range(0, self.data_count):
            for y in range(0, self.data_height):
                for x in range(0, self.data_width):
                    around = self.get_around(x, y, self.data_width, self.data_height)
                    for a in range(0, len(around)):
                        source_color = self.data[data][y][x]
                        target_color = self.data[data][around[a][1]][around[a][0]]
                        self.write_relationship([x, y], source_color, target_color, around[a])
            print(data)
        self.normalize_matrix()

        if visualise: self.show_matrix()

        print("done")

    def write_relationship(self, source, source_color, target_color, target):

        source_offset = self.get_color_offset(source_color)
        target_offset = self.get_color_offset(target_color)

        final_source = (source[0] * self.unique_pixel_count) + source_offset + (
                source[1] * self.data_width * self.unique_pixel_count)
        final_target = (target[0] * self.unique_pixel_count) + target_offset + (
                target[1] * self.data_width * self.unique_pixel_count)

        self.set_edge(final_source, final_target)

    def get_ticks(self):
        ticks = []
        for i in range(0, self.matrix_size):
            for j in range(0, self.unique_pixel_count):
                ticks.append(chr(int(self.unique_pixels[j])))
        return ticks

    def show_matrix(self):
        plt.imshow(self.matrix)
        ind = np.arange(self.matrix_size)
        plt.xticks(ind, self.get_ticks())
        plt.yticks(ind, self.get_ticks())
        plt.show()

    def get_color_offset(self, color):
        for item in range(0, self.unique_pixels.size):
            if (color == self.unique_pixels[item]):
                return item

    def set_edge(self, row, column):
        self.matrix[row][column] += 1

    def is_the_same_color(self, color1, color2):
        for c in range(0, 3):
            if (color1[c] is not color2[c]):
                return False
        return True

    def normalize_matrix(self):
        for y in range(0, self.matrix.shape[0]):
            if np.sum(self.matrix[y] > 0):
                p = 1 / np.sum(self.matrix[y])
            else:
                p = 0
            self.matrix[y, :] *= p

    def get_around(self, x, y, w, h, type="eight"):
        coordinates = []
        coordinates.append([x + 1, y])
        coordinates.append([x - 1, y])
        coordinates.append([x, y + 1])
        coordinates.append([x, y - 1])
        if type == "eight":
            coordinates.append([x - 1, y + 1])
            coordinates.append([x + 1, y + 1])
            coordinates.append([x - 1, y - 1])
            coordinates.append([x + 1, y - 1])

        i = 0
        while i < len(coordinates):
            if (coordinates[i][0] < 0):
                coordinates.pop(i)
                i -= 1
            if (coordinates[i][0] >= w):
                coordinates.pop(i)
                i -= 1
            if (coordinates[i][1] < 0):
                coordinates.pop(i)
                i -= 1
            if (coordinates[i][1] >= h):
                coordinates.pop(i)
                i -= 1
            i += 1

        return coordinates

    def get_connection_count(self, row):
        count = 0
        for x in range(0, self.data_width):
            if (self.matrix[row][x] > 0):
                count += 1
        return count

    def refresh_probabilities(self):
        pass

    def get_image_coords(self, index):
        sector = math.floor((index / self.unique_pixel_count) + 1)
        y = max(0, math.ceil(sector / self.data_width) - 1)
        x = max(0, ((sector - 1) % self.data_width))
        return [x, y]

    def get_color(self, index):
        if (index % 2 == 0):
            return [255, 255, 255]
        return [0, 0, 0]
