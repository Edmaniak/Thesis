from room.Generator import Generator
from room.data_prep import DataPreparator
import room.data as data
import csv
import numpy as np
import math
from room.dictionary import dictionary

# reading the all csv file coded scenes
scene_length = 6
scenes = []
for i in range(0, scene_length):
    with open('data/scene' + str(i) + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            scenes.append(row)

# Two types of data - ONE - imported from Unity - SECOND - imported from data.data
# Supposing we have a square
space_square_dim = int(math.sqrt(len(scenes[0])))
dummy_data = data.data
real_data = np.reshape(np.array(scenes, dtype=int), (scene_length, space_square_dim, space_square_dim))
print(real_data[0])

# preparator = DataPreparator(real_data)

# preparator.prepare_all()
generator = Generator(15, (9, 9), dictionary)
# generator.learn_and_fit(epochs=50)'
generator.generate(10, True)
# a = 5
