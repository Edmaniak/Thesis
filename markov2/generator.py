import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from markov2.model import Model
from PIL import Image as Img


class Generator:
	def __init__(self, model: Model):
		self.model = model
		self.matrix = model.matrix
		self.possible_rows = np.unique(np.nonzero(self.matrix))
		self.height = model.data.shape[1]
		self.width = model.data.shape[2]
		self.channels = model.data_shape[3]
		self.pixels_count = self.width * self.height
		self.putted = []
		self.pixel_variance = model.data_pixel_count

	def generate(self, folder="markov2", bg_color=155):
		print("generating...")
		plt.imshow(self.matrix)
		plt.show()
		image = np.full((self.height, self.width, self.channels), bg_color, 'uint8')
		row = self.get_random_row()
		new_line = True
		pixels = 0
		w = 0
		while (pixels < 2420):
			target = self.pick_random(row)
			if new_line and target:
				self.put_pixel(row, image)
				pixels += 1
				w += 1
				new_line = False
			if (target != False):
				self.put_pixel(target[1], image)
				self.remove_possibility([row])
				pixels += 1
				row = target[1]
			else:
				row = self.get_random_row()
				new_line = True
			if (pixels == 5):
				pass
			print(pixels)

		print(w)
		print("done generating")
		img = Img.fromarray(image, 'RGB')
		plt.subplot(2, 1, 1)
		plt.imshow(img)
		plt.subplot(2, 1, 2)
		plt.imshow(self.matrix)
		img.save("result.bmp")
		plt.show()

	def remove_possibility(self, row):
		for row in row:
			to_remove = self.get_sector_indicies(row)
			for i in range(to_remove[0], to_remove[1] + 1):
				self.matrix[i, :] = 0
				self.matrix[:, i] = 0
				index = np.where(self.possible_rows == i)
				if (len(index[0]) > 0):
					self.possible_rows = np.delete(self.possible_rows, index[0])

	def get_random_row(self):
		index = int(random.uniform(0, len(self.possible_rows)))
		item = self.possible_rows[index]
		return item

	def generate_follow(self):
		pass

	def put_pixel(self, index, image, debug=False):
		self.putted.append(index)

		color = np.array(self.get_color(index))
		img_coords = self.get_image_coords(index)
		image[img_coords[1]][img_coords[0]] = np.array(color)
		if debug:
			plt.subplot(2, 1, 1)
			img = Img.fromarray(image, 'RGB')
			i = plt.imshow(img)
			plt.subplot(2, 1, 2)
			i2 = plt.imshow(self.matrix)


	def get_sector(self, index):
		return math.floor((index / self.pixel_variance) + 1)

	def get_sector_indicies(self, index):
		sector = self.get_sector(index)
		sector_start = (sector * self.pixel_variance) - self.pixel_variance
		sector_end = (sector * self.pixel_variance) - 1
		return [sector_start, sector_end]

	def get_image_coords(self, index):
		sector = math.floor((index / self.pixel_variance) + 1)
		y = max(0, math.ceil(sector / self.width) - 1)
		x = max(0, ((sector - 1) % self.width))
		return [x, y]

	def get_color(self, index):
		if (index % 2 == 0):
			return [255, 255, 255]
		return [0, 0, 0]

	def pick_random(self, row):
		randomWeight = random.uniform(0, 1)
		non_zero = np.nonzero(self.matrix[row])
		if len(non_zero[0]) == 0: return False
		while (True):
			for column in non_zero[0]:
				randomWeight = randomWeight - self.matrix[row][column]
				if randomWeight < 0:
					return [row, column]
