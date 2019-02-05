import numpy as np
from keras import Model, Sequential
from keras.layers import Dense
from random import randint


class Generator:
    def __init__(self, learned_data, unique_objects, default_shape, dictionary: dict):
        self.data = learned_data
        self.unique_objects = np.delete(unique_objects, 0)
        self.unique_objects_count = self.unique_objects.shape[0]
        self.default_shape = default_shape
        self.learned = False
        self.dictionary = dictionary
        self.models = []

    def learn_and_fit(self, learning_rate=0.001, epochs=200, save=False):
        for i in range(0, len(self.data)):
            print("Learning model " + self.get_object_name(i + 1))
            model = Sequential()
            X = self.data[i][0]
            Y = self.data[i][1]
            # Defining model
            model.add(Dense(int(X.shape[1] / 2), input_dim=X.shape[1], activation='relu'))
            model.add(Dense(Y.shape[1], activation='sigmoid'))
            model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
            model.fit(X, Y, epochs=epochs)
            # saving model to array
            self.models.append(model)
        self.learned = True

    def generate(self, iterations, to_predict=[]):
        if not self.learned:
            return
        # Pick random start space
        if len(to_predict) <= 0:
            random_class = self.get_random_object_class_number()
            random_start_from_class = randint(0, self.data[random_class][0].shape[0] - 1)
            to_predict = self.data[random_class][0][random_start_from_class]

        # generating random object class for number of iterations
        vector_shape = to_predict.shape[0]
        final_result = np.copy(to_predict)
        for i in range(0, iterations):
            random_class = self.get_random_object_class_number()
            predicted_object_name = self.get_object_name(self.unique_objects[random_class])
            self.print_2d(to_predict, "Iteration " + str(i) + " predicting " + predicted_object_name)
            prediction = self.models[random_class].predict(np.reshape(to_predict, (1, vector_shape)))
            self.print_2d(prediction, "Raw prediction")
            # TODO randomness
            # TEMPORARY
            likely_position = np.argmax(prediction)
            final_result[likely_position] = random_class

            # printing temporary result and providing recursion at the end
            # Final results becomes the predicted vector
            self.print_2d(final_result, "ADDING THE" + predicted_object_name + "PREDICTED: ")
            to_predict = np.copy(final_result)

    def learn_and_generate(self, iterations, to_predict=[], learning_rate=0.001, epochs=200, save=False):
        self.learn_and_fit(learning_rate, epochs, save)
        self.generate(iterations, to_predict)

    def get_random_object_class_number(self):
        return randint(0, self.unique_objects_count - 1)

    def print_2d(self, array, text=""):
        print(text)
        print("--------------------------------------------")
        print(np.reshape(array, self.default_shape))

    def get_object_name(self, key):
        return self.dictionary.get(key)
