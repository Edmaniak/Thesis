from hanoy.DataGenerator import DataGenerator
from keras.models import Model, Sequential
from keras.layers import Dense
import numpy as np

n = 10
gen = DataGenerator(n)
data = gen.generate()

model = Sequential()
X = data[0]
Y = data[1]

model.add(Dense(int(data.shape[1] / 2), input_dim=X.shape[1], activation='relu', name="hidden"))
# model.add(Dense(int(data.shape[1] / 3), input_dim=data.shape[1], activation='relu', name="second_hidden"))
model.add(Dense(Y.shape[1], name="output"))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])

model.fit(X, Y, epochs=200)

t = np.array([0, 0, 1, 0, 1, 0, 0, 0, 0, 0])
t = np.reshape(t, (1, n))

p = model.predict(t)
print(p)
print(np.round(p, 0))
