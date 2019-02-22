import numpy as np
import matplotlib.pyplot as plt
from keras.engine.saving import model_from_json
from sklearn import preprocessing


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

                core_shape = convolutional_cores[core_i]
                core_width = convolutional_cores[core_i][0]
                core_height = convolutional_cores[core_i][1]
                core_size = core_width * core_height

                model = self.load_model(random_class, core_i)
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
                        for x in range(0, core_width):
                            for y in range(0, core_height):
                                probability_space[x + c_x][y + c_y] += prediction[x][y]

                # Adding the prediction for specific core
                probability_predictions.append(probability_space)

            final_prediction_mul = probability_predictions[0]
            final_prediction_sum = probability_predictions[0]
            for i in range(1, len(probability_predictions)):
                final_prediction_mul = np.multiply(final_prediction_mul, probability_predictions[i])
                final_prediction_sum = np.add(final_prediction_sum, probability_predictions[i])

            # object_coordination = np.unravel_index(np.argmax(probability_space), default_space.shape)

            # Placing object to the predicted place

            # default_space[object_coordination[0]][object_coordination[1]] = random_class

            # Plotting results
            fig, axis = plt.subplots(1, len(probability_predictions) + 2)
            for prediction_i in range(0, len(probability_predictions)):
                axis[prediction_i].imshow(probability_predictions[prediction_i])
            axis[len(probability_predictions)].imshow(final_prediction_mul)
            axis[len(probability_predictions) + 1].imshow(final_prediction_sum)
            plt.show()

    def load_model(self, object_class, core):
        json_file = open('networks/class' + str(object_class) + str(core) + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights('networks/class' + str(object_class) + str(core) + '.h5')
        return loaded_model

    def copy_array(self, array):
        result = []

        for item in array:
            result.append(item)

        return result
