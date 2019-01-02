import numpy as np
import imageio

from markov2.generator import Generator
from markov2.model import Model
import matplotlib.pyplot as plt

# obj1 = np.array([[[255, 255, 255], [0, 0, 0], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
# obj4 = np.array([[[255, 255, 255], [0, 0, 0], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
# obj2 = np.array([[[0, 0, 0], [0, 0, 0], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
# obj3 = np.array([[[0, 0, 0], [0, 0, 0], [255, 255, 255]], [[0, 0, 0], [255, 255, 255], [0, 0, 0]]])
# #


# data = np.array([obj1,obj2,obj3,obj4])



import glob

data = []
files = glob.glob("troo/*.jpg")

for i in range(0, 20):
	image = imageio.imread(files[i])
	data.append(np.array(image))

model = Model(data)
model.compile()
generator = Generator(model)
generator.generate()
