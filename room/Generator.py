import numpy as np
from keras import Model, Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import model_from_json
from random import randint
import pandas as pd


class Generator:
    def __init__(self, unique_classes_count, default_shape, dictionary: dict):
        self.unique_classes_count = unique_classes_count
        self.unique_classes = np.arange(1, unique_classes_count + 1, 1, int)
        self.default_shape = default_shape
        self.learned = False
        self.dictionary = dictionary
        self.models = []
        self.results = []

    def learn_and_fit(self, learning_rate=0.001, epochs=200):
        for i in range(1, self.unique_classes_count + 1):
            print("Learning model " + str(i))

            # Loading the data
            X = np.array(pd.read_csv("model/x" + str(i) + ".csv", delimiter=";"), dtype=int)
            Y = np.array(pd.read_csv("model/y" + str(i) + ".csv", delimiter=";"), dtype=int)

            # Defining checkpoints
            mc = ModelCheckpoint("networks/class" + str(i) + '.h5', save_best_only=True, verbose=1, mode='min')

            # Defining model
            model = Sequential()
            model.add(Dense(int(X.shape[1] / 2), input_dim=X.shape[1], activation='relu'))
            model.add(Dense(int(X.shape[1] / 2), input_dim=X.shape[1], activation='relu'))
            model.add(Dense(Y.shape[1], activation='sigmoid'))
            model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
            model.fit(X, Y, epochs=epochs, callbacks=[mc])

            # Saving model to array
            model.save_weights("networks/class" + str(i) + '.h5')
            model_json = model.to_json()
            with open("networks/class" + str(i) + '.json', "w") as json_file:
                json_file.write(model_json)
        # self.models.append(model)
        self.learned = True

    def generate(self, iterations, user_input=False, to_predict=[]):
        # Pick random start space
        if len(to_predict) <= 0:
            random_class = self.get_random_object_class_number()

            # Loading random start file
            start = np.array(pd.read_csv('model/x' + str(random_class) + '.csv', ';'), dtype=int)
            random_start_from_class = randint(0, start.shape[0] - 1)
            to_predict = start[random_start_from_class]

        # Generating random object class for number of iterations
        vector_shape = to_predict.shape[0]
        final_result = np.copy(to_predict)

        self.print_2d(final_result, " DEFAULT SITUATION ")

        for i in range(1, iterations + 1):

            if user_input:
                random_class = input()
            else:
                random_class = self.get_random_object_class_number()

            to_predict_class_name = self.get_object_name(random_class)
            self.print_2d(to_predict, "Iteration " + str(i) + " predicting " + to_predict_class_name)

            # Loading the right model
            json_file = open('networks/class' + random_class + '.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            loaded_model.load_weights('networks/class' + random_class + '.h5')

            # Predicting
            prediction = loaded_model.predict(np.reshape(to_predict, (1, vector_shape)))
            self.print_2d(prediction, "Raw prediction")

            # TODO randomness
            # TEMPORARY
            likely_position = np.argmax(prediction)
            final_result[likely_position] = random_class

            # Printing temporary result and providing recursion at the end
            # Final results becomes the predicted vector
            self.print_2d(final_result, " ADDING THE " + " PREDICTED: ")
            to_predict = np.copy(final_result)

    def learn_and_generate(self, iterations, to_predict=[], learning_rate=0.001, epochs=200, save=False):
        self.learn_and_fit(learning_rate, epochs, save)
        self.generate(iterations, to_predict)

    def get_random_object_class_number(self):
        return randint(1, self.unique_classes_count)

    def print_2d(self, array, text=""):
        print(text)
        print("--------------------------------------------")
        print(np.reshape(array, self.default_shape))

    def get_object_name(self, key):
        return self.dictionary.get(int(key))

    def get_object_id(self, index):
        return self.unique_classes[index]
