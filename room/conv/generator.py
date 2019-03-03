import numpy as np
import math
import matplotlib.pyplot as plt
from keras.engine.saving import model_from_json
from sklearn import preprocessing
import scipy.stats as stats
import uuid


class Generator:
    def __init__(self):
        pass

    def generate(self, default_space, iterations, convolutional_cores):
        default_space = np.array(default_space, int)
        print("Generating for: ")
        print(default_space)
        for i in range(0, iterations):
            print("Add object:")
            random_class = input()
            probability_predictions = []
            # LOAD MODEL AND MAKE PREDICTION FOR EACH CORE SNIPPET
            for core_i in range(0, len(convolutional_cores)):

                probability_space = np.zeros((default_space.shape[0], default_space.shape[1]))
                probability_space_width = probability_space.shape[0]
                probability_space_height = probability_space.shape[1]
                probability_space_size = probability_space.shape[0] * probability_space.shape[1]

                core_width = convolutional_cores[core_i][1]
                core_height = convolutional_cores[core_i][0]
                core_size = core_width * core_height

                model = self.load_model(random_class, core_width, core_height)
                original_space = np.copy(default_space)

                for c_y in range(0, probability_space_height - core_height + 1):
                    for c_x in range(0, probability_space_width - core_width + 1):
                        to_predict = []
                        for x in range(0, core_width):
                            for y in range(0, core_height):
                                to_predict.append(default_space[x + c_x][y + c_y])

                        # Predicting
                        prediction = model.predict(np.reshape(to_predict, (1, core_size)))

                        # Updating the probability space
                        prediction = np.reshape(prediction, (core_width, core_height))
                        for x in range(0, core_height):
                            for y in range(0, core_width):
                                probability_space[x + c_x][y + c_y] += prediction[x][y]

                # Adding the prediction for specific core
                probability_predictions.append(probability_space)

            final_prediction_mul = probability_predictions[0]
            final_prediction_sum = probability_predictions[0]

            print(stats.norm(3, 2).pdf(3))

            for i in range(1, len(probability_predictions)):
                multiplier = stats.norm(2, 3).pdf(i)
                multiplier = 1
                final_prediction_mul = np.multiply(final_prediction_mul,
                                                   np.multiply(probability_predictions[i], multiplier))
                final_prediction_sum = np.add(final_prediction_sum, np.multiply(probability_predictions[i], multiplier))

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

             #Plotting results
            images = [original_space]
            for prediction_i in range(0, len(probability_predictions)):
                images.append(probability_predictions[prediction_i])
            images.append(final_prediction_sum)
            images.append(final_prediction_mul)
            images.append(default_space)

            columns = 6
            rows = 4

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

    def load_model(self, object_class, core_width, core_height):
        json_file = open('networks/class' + str(object_class) + str(core_width) + str(core_height) + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights('networks/class' + str(object_class) + str(core_width) + str(core_height) + '.h5')
        return loaded_model

    def copy_array(self, array):
        result = []

        for item in array:
            result.append(item)

        return result

    def test_prediction(self, x, object_class, core_width, core_height):
        core = (len(x), len(x))
        model = self.load_model(object_class, core_width, core_height)
        # Predicting
        prediction = model.predict(np.reshape(x, (1, x.size)))
        # Updating the probability space
        prediction = np.reshape(prediction, (core[0], core[1]))
        print(np.round(prediction, 2))
        return prediction
