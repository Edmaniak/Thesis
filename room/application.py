from room.data_prep import DataPreparator
import room.data as data
from keras.models import Model, Sequential
from keras.layers import Dense
import numpy as np

generator = DataPreparator(data.data)

prepared_data = generator.prepare(normalize=False)
model = Sequential()
X = prepared_data.get('x')
to_predict_x = X[100]
Y = prepared_data.get('y')
to_predict_result = Y[100]
model.add(Dense(int(X.shape[1] / 2), input_dim=X.shape[1], activation='relu', name='hidden1'))

model.add(Dense(Y.shape[1], name="output"))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])

