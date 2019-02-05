import numpy as np

r1 = [[0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 1, 2, 1, 0],
      [0, 0, 1, 0, 0],
      [8, 0, 0, 0, 0],
      ]

r2 = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      ]

r3 = [[0, 1, 0, 0, 0],
      [1, 2, 1, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [8, 0, 0, 0, 0],
      ]

r4 = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0],
      ]

r5 = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 2, 1],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      ]

r6 = [[0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 1, 2, 1],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      ]

r7 = [[0, 0, 0, 0, 0],
      [0, 2, 1, 0, 0],
      [0, 2, 1, 0, 0],
      [0, 2, 1, 0, 0],
      [0, 0, 0, 0, 0],
      ]

r8 = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 2, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      ]

r9 = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 2, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      ]

r10 = [[0, 0, 0, 0, 0],
       [0, 0, 0, 2, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       ]
r11 = [[0, 0, 0, 0, 0],
       [0, 0, 1, 2, 1],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       ]
r12 = [[0, 0, 0, 0, 0],
       [0, 0, 1, 2, 1],
       [0, 1, 0, 0, 0],
       [1, 2, 1, 0, 0],
       [0, 1, 0, 0, 0],
       ]

data = np.array([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12], dtype=int)
