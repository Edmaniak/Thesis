import glob
import numpy as np

data = []
files = glob.glob("levelData/*.txt")

i, j, k = -1, -1, -1
for file in files:
    data.append([])
    i += 1
    j = -1
    with open(file) as txt:
        for line in txt:
            data[i].append([])
            j += 1
            for char in line:
                data[i][j].append(char)

parsed_data = np.array([np.asarray(data)])
print(parsed_data)
