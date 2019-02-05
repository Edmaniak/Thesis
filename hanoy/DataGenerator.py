import numpy as np
from sympy.utilities.iterables import multiset_permutations
import itertools


#   ---   2
#  -----  1
# ------- 0
class DataGenerator:

    def __init__(self, n):
        self.n = n
        self.discs = self.generateLetters(n)
        self.x = []
        self.y = []

    def generate(self):
        n = self.n
        for i in range(0, n):
            self.permutate(i)
        print(str(len(self.x)) + " " + str(len(self.y)))
        return np.array([self.x, self.y])

    def permutate(self, n):
        c = itertools.combinations_with_replacement([0, 1], self.n - n - 1)
        d = 0
        for p in list(c):
            a = multiset_permutations(p)
            try:
                for j in list(a):
                    v = self.get_base(n)
                    for k in list(j):
                        v.append(k)
                    self.x.append(v)
                    self.y.append(self.get_y(v))
            except:
                pass

    def get_y(self, v):
        index = 0
        vector = []
        for i in range(0, len(v)):
            vector.append(v[i])

        for i in range(len(vector) - 1, 0, -1):
            if (vector[i] == 1):
                index = i
                break
        for i in range(index, len(vector)):
            vector[i] = 1
        return vector

    def get_base(self, n):
        base = []
        a = n - self.n
        for i in range(0, n):
            base.append(0)
        base.append(1)
        return base

    def generateLetters(self, n):
        letters = []
        # 97 = A
        for letter in range(0, n): letters.append(letter)
        return letters

    def vectorize(self, object):
        v = []

        for i in range(0, self.n):
            v.append(0)

        for i in range(0, self.n):
            if (self.is_in(i, object) != -1):
                v[i] = 1
        return v

    def is_in(self, x, iterable):
        for i, item in enumerate(iterable):
            if item == x:
                return i
        return -1
