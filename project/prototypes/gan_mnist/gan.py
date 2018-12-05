from keras.models import Sequential
from keras.layers import Dense, LeakyReLU, BatchNormalization, Reshape, Flatten
from keras.optimizers import Adam
import numpy as np


class GAN:
	def __init__(self, width=28, height=28, channels=1):
		self.WIDTH = width
		self.HEIGHT = height
		self.CHANNELS = channels

		self.SHAPE = (self.WIDTH, self.HEIGHT, self.CHANNELS)

		self.OPTIMIZER = Adam(lr=0.0002, decay=8e-9)

		self.noise_gen = np.random.normal(0, 1, (100,))

		self.Gen = self.generator()
		self.Gen.compile(loss='binary_crossentropy', optimizer=self.OPTIMIZER)

		self.Disc = self.discriminator()
		self.Disc.compile(loss='binary_crossentropy', optimizer=self.OPTIMIZER, metrics=['accuracy'])

		self.stacked_G_D = self.stacked_G_D()
		self.stacked_G_D.compile(loss='binary_crossentropy', optimizer=self.OPTIMIZER)

	def generator(self):
		model = Sequential()
		model.add(Dense(256, input_shape=(100,)))
		model.add(LeakyReLU(alpha=0.2))
		model.add(BatchNormalization(momentum=0.8))
		model.add(Dense(512))
		model.add(LeakyReLU(alpha=0.2))
		model.add(BatchNormalization(momentum=0.8))
		model.add(Dense(1024))
		model.add(LeakyReLU(alpha=0.2))
		model.add(BatchNormalization(momentum=0.8))
		model.add(Dense(self.WIDTH * self.HEIGHT * self.CHANNELS, activation='tanh'))
		model.add(Reshape((self.WIDTH, self.HEIGHT, self.CHANNELS)))

		return model

	def discriminator(self):
		model = Sequential()
		model.add(Flatten(input_shape=self.SHAPE))
		model.add(Dense((self.WIDTH * self.HEIGHT * self.CHANNELS), input_shape=self.SHAPE))

		model.add(LeakyReLU(alpha=0.2))
		model.add(Dense(int((self.WIDTH * self.HEIGHT * self.CHANNELS) / 2)))
		model.add(LeakyReLU(alpha=0.2))

		model.add(Dense(1, activation='sigmoid'))
		model.summary()

		return model

	def stacked_G_D(self):
		# Freezes the weights
		self.Disc.trainable = False

		model = Sequential()
		model.add(self.Gen)
		model.add(self.Disc)

		return model

	def train(self, X_train, epochs=20000, batch=32, save_interval=200):
		for cnt in range(epochs):
			random_index = np.random.randint(0, len(X_train) - batch / 2)
			legit_images = X_train[random_index: random_index + int(batch / 2)].reshape(int(batch / 2), self.WIDTH, self.HEIGHT,
			                                                                    self.CHANNELS)
			# vygenerovat sum
			gen_noise = np.random.normal(0, 1, (int(batch / 2), 100))
			# data ktera se vratila pri predikci --> na 16 obrazku ...100 nahodnych pixelu
			syntetic_images = self.Gen.predict(gen_noise)
			print(syntetic_images)

			x_combined_batch = np.concatenate((legit_images, syntetic_images))

			y_combined_batch = np.concatenate((np.ones((int(batch / 2), 1)), np.zeros((int(batch / 2), 1))))

			d_loss = self.Disc.train_on_batch(x_combined_batch, y_combined_batch)

			noise = np.random.normal(0, 1, (batch, 100))
			y_mislabled = np.ones((batch, 1))

			g_loss = self.stacked_G_D.train_on_batch(noise, y_mislabled)

			print('epoch: %d, [Discriminator :: d_loss: %f], [ Generator :: loss: %f]' % (cnt, d_loss[0], g_loss))


