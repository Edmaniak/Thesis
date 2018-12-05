from keras.layers import Dense
from keras.utils import plot_model
from keras.models import Sequential, load_model
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np


class Neural1D:
	def __init__(self, file):
		self.dataset = pd.read_csv(file, delimiter=',', error_bad_lines=False)
		self.columns = self.dataset.shape[1] - 1
		self.model = Sequential()


	def load(self):
		self.model = load_model('model.h5')

	def preprocess(self):
		X = self.dataset.iloc[:, 0:self.columns].values
		Y = self.dataset.iloc[:, self.columns].values
		# Dummy variable trap???

		self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

		# Standardization
		self.sc = StandardScaler()
		self.X_train = self.sc.fit_transform(self.X_train)
		self.X_test = self.sc.transform(self.X_test)

	def train(self):

		self.preprocess()

		# NN
		self.model = Sequential()

		self.model.add(
			Dense(units=int(self.columns / 2), kernel_initializer='uniform', activation='relu', input_dim=self.columns))
		self.model.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

		self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

		self.model.fit(self.X_train, self.Y_train, batch_size=10, epochs=10)

		self.model.save('model.h5')

	def predict(self, data: list()):
		test_data = []


		for i in range(len(data)):
			test_data.append(data[i].val)

		if len(data) < self.columns:
			for i in range(len(data), self.columns):
				test_data.append(0)
		test_data = self.sc.transform([test_data])

		test_data = np.array(test_data)


		return self.model.predict(test_data)
