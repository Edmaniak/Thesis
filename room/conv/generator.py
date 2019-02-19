import numpy as np
import matplotlib.pyplot as plt
from keras.engine.saving import model_from_json
from sklearn import preprocessing


class Generator:
    def __init__(self):
        pass

    def generate(self, default_space, iterations):
        print("Generating for: ")
        print(default_space)
        core = (3, 3)

        probability_space = np.zeros((default_space.shape[0], default_space.shape[1], int))
        probability_space_width = probability_space.shape[0]
        probability_space_height = probability_space.shape[1]

        for i in range(0, iterations):
            print("Add object:")
            random_class = input()

            core_width = core[0]
            core_height = core[1]
            core_size = core_width * core_height

            # LOAD MODEL AND MAKE PREDICTION FOR EACH CORE SNIPPET
            iterator = -1
            for c_y in range(0, probability_space_height - core_height + 1):
                for c_x in range(0, probability_space_width - core_width + 1):
                    iterator += 1
                    to_predict = []
                    for x in range(0, core_height):
                        for y in range(0, core_width):
                            to_predict.append(default_space[x + c_x][y + c_y])

                    # Loading right model and predicting to_predict
                    model = self.load_model(random_class)
                    prediction = model.predict(np.reshape(to_predict, (1, core_size)))

                    # Updating the probability space
                    prediction = np.reshape(prediction, (core_width, core_height))
                    for x in range(0, core_height):
                        for y in range(0, core_width):
                            probability_space[x + c_x][y + c_y] += prediction[x + c_x][y + c_y]

            # Choosing the option and normalizing
            probability_space = preprocessing.scale(probability_space)
            object_coordination = np.argmax(probability_space)

            # Placing object to the predicted place
            original_space = self.copy_array(default_space)
            default_space[object_coordination[0]][object_coordination[1]] = random_class

            # Plotting results
            fig, axis = plt.subplots(1, 2)
            axis[0, 0].plot(original_space)
            axis[0, 1].plot(default_space)
            axis[1, 1].figtext("Probability space for object class: " + random_class)
            axis[1, 1].plot(probability_space)
            plt.show()

    def load_model(self, object_class):
        json_file = open('networks/class' + object_class + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights('networks/class' + object_class + '.h5')
        return loaded_model

    def copy_array(self, array):
        result = []

        for item in array:
            result.append(item)

        return result
