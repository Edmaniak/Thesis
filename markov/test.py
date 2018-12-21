import numpy as np


from markov.mark import Image
from markov.mark import Model

obj1 = np.array([[[0, 0, 0], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
obj2 = np.array([[[0, 0, 0], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
obj3 = np.array([[[255, 255, 255], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [0, 0, 0], [255, 255, 255]]])
obj4 = np.array([[[255, 255, 255], [0, 0, 0], [255, 255, 255]], [[255, 255, 255], [0, 0, 0], [255, 255, 255]]])
obj5 = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
obj6 = np.array([[[0, 0, 0], [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])

z = np.zeros((2,3))

img1 = Image(obj1)
img2 = Image(obj2)
img3 = Image(obj3)
img4 = Image(obj4)
img5 = Image(obj5)
img6 = Image(obj6)

data = []

data.append(img1)
data.append(img2)
data.append(img3)
data.append(img4)
data.append(img5)
data.append(img6)

model = Model(data)
model.compile()
picture = model.generate(1)



a = 5


