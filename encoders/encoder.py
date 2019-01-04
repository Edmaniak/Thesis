from keras.layers import Input, Dense
from keras.models import Model, Sequential
from keras.utils import plot_model
from keract import get_activations

import numpy as np

obj1 = np.array([[[0, 0, 0], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
obj2 = np.array([[[0, 0, 0], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
obj3 = np.array([[[255, 255, 255], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [0, 0, 0], [255, 255, 255]]])
obj4 = np.array([[[255, 255, 255], [0, 0, 0], [255, 255, 255]], [[255, 255, 255], [0, 0, 0], [255, 255, 255]]])
obj5 = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])
obj6 = np.array([[[0, 0, 0], [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [255, 255, 255], [255, 255, 255]]])

x = np.array([obj1, obj2, obj3, obj4, obj5, obj6])
x = x.reshape((1, x.size))
print(x.shape)
model = Sequential()

hidden = Dense(3, input_dim=4, activation='relu', name="hidden")

model.add(hidden)
model.add(Dense(4, name="output"))

model.compile(loss='mean_squared_error', optimizer='adam')
plot_model(model)
model.fit(x, x, epochs=1000)

a = get_activations(model, x)
b = list(a.values())
print(model.predict(np.array([[10, 10, 20, 20]])))
mean = np.mean(b[0])
std = np.std(b[0])
gauss = np.random.normal(mean, std, (1, 4))

model2 = Sequential()
model2.add(Dense(4, input_dim=3, weights=model.get_layer("output").get_weights()))

print(model2.predict(list(a.values())[0]))
