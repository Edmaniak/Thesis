import matplotlib.image as img
from markov.mark import Image as IMG, Model
import imageio

from PIL import Image
import numpy as np
import image_slicer
import glob
data = []
files = glob.glob("troo/*.jpg")

for a in range(0,10):
    for i in range(0, 19):
        image = imageio.imread(files[i])
        data.append(IMG(image))
        print(str(i) + " read")




model = Model(data,0)
model.compile()
model.generate(20)

a = 5
# print("ahoj")
