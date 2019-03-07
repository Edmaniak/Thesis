import numpy as np
import math
import matplotlib.pyplot as plt
from keras.engine.saving import model_from_json
from sklearn import preprocessing
import scipy.stats as stats
import uuid


class Generator:
    def __init__(self, unique_objects_with_symbols=None):
        self.unique_objects_with_symbols = unique_objects_with_symbols

    def generate_one(self, object_class, default_space, convolutional_cores):
        return self.generate(default_space, 1, convolutional_cores, object_class)

    def generate(self, default_space, iterations, convolutional_cores, object_class=None):
        default_space = np.array(default_space, int)
        for i in range(0, iterations):

            if object_class is None:
                print("Add object:")
                random_class = input()
            else:
                random_class = object_class

            probability_predictions = []
            # LOAD MODEL AND MAKE PREDICTION FOR EACH CORE SNIPPET
            for core_i in range(0, len(convolutional_cores)):

                probability_space = np.zeros((default_space.shape[0], default_space.shape[1]))
                probability_space_width = probability_space.shape[0]
                probability_space_height = probability_space.shape[1]
                probability_space_size = probability_space.shape[0] * probability_space.shape[1]

                core_width = convolutional_cores[core_i][1]
                core_height = convolutional_cores[core_i][0]

                model = self.load_model(random_class, core_width, core_height)
                original_space = np.copy(default_space)

                for c_y in range(0, probability_space_height - core_height + 1):
                    for c_x in range(0, probability_space_width - core_width + 1):
                        to_predict = []
                        for x in range(0, core_width):
                            for y in range(0, core_height):
                                to_predict.append(default_space[x + c_x][y + c_y])

                        # Predicting
                        to_predict = self.spread_objects_to_vector(to_predict, (core_width, core_height))
                        prediction = model.predict(np.reshape(to_predict, (1, to_predict.shape[0])))

                        # Updating the probability space
                        prediction = np.reshape(prediction, (core_width, core_height))
                        for x in range(0, core_height):
                            for y in range(0, core_width):
                                probability_space[x + c_x][y + c_y] += prediction[x][y]

                # Adding the prediction for specific core
                probability_predictions.append(probability_space)

            final_prediction_mul = probability_predictions[0]
            final_prediction_sum = probability_predictions[0]

            for i in range(1, len(probability_predictions)):
                final_prediction_mul = np.multiply(final_prediction_mul, probability_predictions[i])
                final_prediction_sum = np.add(final_prediction_sum, probability_predictions[i])

            # choosing the final position
            sorted_probability_space = -np.sort(-np.reshape(final_prediction_mul, (1, probability_space_size)))
            candidate_i = 0
            candidate = sorted_probability_space[0][candidate_i]
            obj_coords = np.where(final_prediction_mul == candidate)

            while default_space[obj_coords[0][0]][obj_coords[1][0]] > 1:
                candidate_i += 1
                candidate = sorted_probability_space[0][candidate_i]
                obj_coords = np.where(final_prediction_mul == candidate)

            obj_coords = np.where(final_prediction_mul == candidate)
            default_space[obj_coords[0][0]][obj_coords[1][0]] = random_class

            if object_class is not None:
                return default_space

            # Plotting results
            images = [original_space]
            for prediction_i in range(0, len(probability_predictions)):
                images.append(probability_predictions[prediction_i])
            images.append(final_prediction_sum)
            images.append(final_prediction_mul)
            images.append(default_space)

            columns = 4
            rows = 2

            ax = []
            fig = plt.figure()

            for i in range(columns * rows):
                ax.append(fig.add_subplot(rows, columns, i + 1))
                ax[-1].set_title("ax:" + str(i))  # set title
                if i < len(images):
                    plt.imshow(images[i])

            plt.savefig("results/" + str(uuid.uuid4()) + ".png")
            print(default_space)
            plt.show()
            return None

    def spread_objects_to_vector(self, data, core_shape):
        vector_size = core_shape[0] * core_shape[1] * self.unique_objects_with_symbols.size
        vector = np.zeros(vector_size, int)
        for i in range(0, len(data)):
            # Floor
            if data[i] != 0:
                offset = np.where(self.unique_objects_with_symbols == data[i])[0][0]
                object_position = (i * self.unique_objects_with_symbols.size) + offset
                vector[object_position] = 1
        return np.array(vector)

    def load_model(self, object_class, core_width, core_height):
        json_file = open('networks/class' + str(object_class) + str(core_width) + str(core_height) + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights('networks/class' + str(object_class) + str(core_width) + str(core_height) + '.h5')
        return loaded_model

    def test_prediction(self, x, object_class, core_width, core_height):
        core = (len(x), len(x))
        model = self.load_model(object_class, core_width, core_height)
        # Predicting
        prediction = model.predict(np.reshape(x, (1, x.size)))
        # Updating the probability space
        prediction = np.reshape(prediction, (core[0], core[1]))
        print(np.round(prediction, 2))
        return prediction
