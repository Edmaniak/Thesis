from room.Generator import Generator
from room.data_prep import DataPreparator
import room.data as data
import numpy as np

preparator = DataPreparator(data.data)


prepared_data = preparator.prepare_all()
unique_objects = preparator.unique_objects
generator = Generator(prepared_data, unique_objects, (5, 5), data.dictionary)
generator.learn_and_generate(2)
a = 5
