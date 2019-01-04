import glob
import numpy as np

from markov2.generator import Generator
from markov2.model import Model

shape = (15, 14, 40)
data = np.zeros(shape)
files = glob.glob("levelData/*.txt")

i, j, k = -1, -1, -1
for file in files:
    with open(file) as txt:
        i += 1
        j = -1
        for line in txt:
            it = 0
            j += 1
            for char in range(0, shape[2]):
                if (char != '\n'):
                    data[i][j][it] = ord(line[char])
                    it += 1

parsed_data = np.array(np.array(data))
print(parsed_data)

model = Model(data)
model.compile()

generator = Generator(model)
generator.generate()
