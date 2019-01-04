import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from markov2.model import Model
from PIL import Image as Img


# https://github.com/TheVGLC/TheVGLC

class Generator:
    def __init__(self, model: Model):
        self.model = model
        self.original_matrix = model.matrix
        self.working_matrix = np.array(self.original_matrix)
        self.possible_rows = np.unique(np.nonzero(self.original_matrix))
        self.height = model.data.shape[1]
        self.color_dict = model.unique_pixels
        self.width = model.data.shape[2]
        if (len(model.data_shape) > 3):
            self.channels = model.data_shape[3]
        else:
            self.channels = 1
        self.pixels_count = self.width * self.height
        self.putted = []
        self.pixel_variance = model.unique_pixel_count

    def generate(self, number_of_samples=10, folder="markov2", bg_color=155):
        print("generating...")
        for i in range(0, number_of_samples):
            self.restart_matrix()
            image = np.full((self.height, self.width, self.channels), bg_color, 'uint8')
            pixels = 0
            new_line = True
            row = self.get_random_row()
            added_start = []
            while (self.possible_rows.size >0):
                old_pixels = pixels
                target = self.pick_random(row)
                if new_line and target:
                    self.put_pixel(row, image)
                    added_start.append(row)
                    pixels += 1
                    new_line = False
                if (target != False):
                    self.put_pixel(target[1], image)
                    self.remove_possibility([row])
                    pixels += 1
                    row = target[1]
                else:
                    row = self.get_random_row()
                    new_line = True
                if (old_pixels == pixels):
                    print("Error")
                print(self.possible_rows.size)
            print("sample " + str(i))
            self.print_chars(image)
        print("done generating")


        # Showing
        if (self.channels == 3):
            img = Img.fromarray(image, 'RGB')
            plt.subplot(2, 1, 1)
            print(image)
            plt.subplot(2, 1, 2)
            plt.imshow(self.matrix)
            img.save("result.bmp")
            plt.show()

        if (self.channels == 1):
            self.print_chars(image)

    def remove_possibility(self, row, debug = False):
        for row in row:
            to_remove = self.get_sector_indexes(row)
            for i in range(to_remove[0], to_remove[1] + 1):
                self.working_matrix[i, :] = 0
                self.working_matrix[:, i] = 0

        self.possible_rows = np.unique(np.nonzero(self.working_matrix))
        if(debug):
            print(self.possible_rows)
            self.show_matrix()

    def get_random_row(self):
        index = int(random.uniform(0, len(self.possible_rows)))
        item = self.possible_rows[index]
        return item

    def restart_matrix(self):
        self.working_matrix = np.array(self.original_matrix)
        self.possible_rows = np.unique(np.nonzero(self.original_matrix))

    def generate_follow(self):
        pass

    def print_chars(self, image):
        for y in range(0, self.height):
            row = ""
            for x in range(0, self.width):
                row += chr(image[y][x])
            print(row)

    def put_pixel(self, index, image, debug=False):
        self.putted.append(index)
        color = np.array(self.get_color(index))
        img_coordinates = self.get_image_coordinates(index)
        image[img_coordinates[1]][img_coordinates[0]] = np.array(color)


        if debug and self.channels == 3:
            plt.subplot(2, 1, 1)
            img = Img.fromarray(image, 'RGB')
            plt.imshow(img)
            plt.subplot(2, 1, 2)
            plt.imshow(self.working_matrix)
            print("putting at " + str(img_coordinates) + " row: " + str(index))

        if debug and self.channels == 1:
            self.print_chars(image)
            print("putting at " + str(img_coordinates) + " row: " + str(index))
            plt.imshow(self.working_matrix)
            plt.show()

    def get_sector(self, index):
        return math.floor((index / self.pixel_variance) + 1)

    def get_sector_indexes(self, index):
        sector = self.get_sector(index)
        sector_start = (sector * self.pixel_variance) - self.pixel_variance
        sector_end = (sector * self.pixel_variance) - 1
        return [sector_start, sector_end]

    def get_image_coordinates(self, index):
        sector = math.floor((index / self.pixel_variance) + 1)
        y = max(0, math.ceil(sector / self.width) - 1)
        x = max(0, ((sector - 1) % self.width))
        return [x, y]

    def get_color(self, index):
        return self.color_dict[index % len(self.color_dict)]

    def pick_random(self, row):
        randomWeight = random.uniform(0, 1)
        non_zero = np.nonzero(self.working_matrix[row])
        if len(non_zero[0]) == 0: return False
        while (True):
            for column in non_zero[0]:
                randomWeight = randomWeight - self.working_matrix[row][column]
                if randomWeight < 0:
                    return [row, column]

    def show_matrix(self):
        plt.imshow(self.working_matrix)
        ind = np.arange(self.model.matrix_size)
        plt.xticks(ind, self.get_ticks())
       # plt.yticks(ind, self.get_ticks())
        plt.show()

    def get_ticks(self):
        ticks = []
        for i in range(0, self.model.matrix_size):
            for j in range(0, self.model.unique_pixel_count):
                ticks.append(chr(int(self.model.unique_pixels[j])))
        return ticks
