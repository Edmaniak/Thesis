import numpy as np

d1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 4, 0, 0, 4, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 2, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 2, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 5, 0, 1],
    [1, 0, 4, 0, 0, 4, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 3, 0, 0, 3, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 2, 3, 0, 0, 5, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 2, 0, 3, 0, 0, 1],
    [1, 4, 0, 0, 0, 3, 2, 3, 0, 1],
    [1, 4, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 2, 3, 0, 0, 5, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 5, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 2, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 3, 2, 1],
    [1, 0, 3, 2, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d5 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 4, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 4, 0, 0, 3, 2, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 5, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d6 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 5, 0, 4, 1],
    [1, 0, 2, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 5, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 3, 0, 0, 0, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 4, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d7 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 3, 0, 3, 2, 3, 0, 1],
    [1, 0, 3, 0, 3, 0, 3, 0, 0, 1],
    [1, 0, 0, 3, 2, 3, 0, 0, 4, 1],
    [1, 0, 3, 0, 3, 0, 3, 0, 0, 1],
    [1, 0, 2, 3, 0, 3, 2, 3, 0, 1],
    [1, 0, 3, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 4, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d8 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 4, 0, 4, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 2, 3, 0, 0, 1],
    [1, 4, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 5, 0, 1],
    [1, 0, 0, 4, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d9 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 4, 0, 0, 4, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 2, 3, 0, 0, 1],
    [1, 2, 3, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
    [1, 4, 0, 5, 0, 0, 3, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d10 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 4, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 2, 3, 0, 0, 1],
    [1, 4, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 3, 0, 0, 3, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d11 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 0, 0, 0, 4, 0, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 3, 2, 3, 0, 4, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 5, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d12 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 0, 2, 3, 0, 0, 3, 0, 0, 1],
    [1, 0, 3, 0, 0, 3, 2, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 4, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 2, 3, 0, 2, 0, 4, 1],
    [1, 4, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 4, 0, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d13 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 5, 0, 0, 0, 5, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 2, 0, 0, 3, 0, 0, 1],
    [1, 0, 2, 3, 0, 3, 2, 3, 0, 1],
    [1, 4, 0, 2, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d14 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 4, 0, 4, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 3, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 2, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 5, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 4, 0, 4, 0, 4, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d15 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 4, 0, 4, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 4, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 2, 3, 0, 0, 4, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 4, 0, 0, 0, 3, 2, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d16 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 4, 0, 4, 0, 4, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 3, 0, 1],
    [1, 0, 3, 2, 3, 0, 3, 2, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 3, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 4, 0, 0, 3, 2, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d17 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 4, 0, 0, 0, 0, 4, 4, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 4, 0, 3, 2, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 5, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d18 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 4, 4, 1],
    [1, 0, 2, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 2, 3, 0, 4, 1],
    [1, 4, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 0, 3, 0, 1],
    [1, 0, 2, 3, 0, 0, 3, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d19 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 4, 0, 4, 4, 0, 4, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 2, 0, 3, 2, 3, 0, 4, 1],
    [1, 0, 3, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 5, 0, 0, 0, 5, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

d20 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 4, 0, 0, 4, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 2, 3, 0, 2, 3, 0, 0, 1],
    [1, 0, 3, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 2, 3, 0, 2, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

data = np.array([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20])