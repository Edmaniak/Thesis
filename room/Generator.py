import numpy as np


class Generator:
    def __init__(self, data):
        self.set_data(data)

    def set_data(self, data):
        self.data = np.array(data)
        self.unique_objects = np.unique(self.data)
        self.unique_objects_count = np.size(self.unique_objects)

    def generate(self, learning_rate):
        pass

    def generate_class(self, object_class, learning_rate, state=[]):
        pass


