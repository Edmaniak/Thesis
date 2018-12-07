from project.generator.gen2D.Object2D import Object2D
from enum import Enum


class RelationType(Enum):
    IS_BY_LEFT = 0
    IS_BY_RIGHT = 1
    IN_FRONT = 2
    LEFT = 3
    RIGHT = 4
    IN = 5
    ON = 6


class Relation:
    def __init__(self, object1: Object2D, type: RelationType, object2: Object2D, variance: float = 0):
        self.type = type
        self.variance = variance
        self.object1 = object1
        self.object2 = object2

    def get_reverse(self):
        if (self.type == RelationType.IS_BY_LEFT):
            return RelationType.IS_BY_RIGHT
        if (self.type == RelationType.IS_BY_RIGHT):
            return RelationType.IS_BY_LEFT
        if (self.type == RelationType.IN):
            return RelationType.IN
        if (self.type == RelationType.LEFT):
            return RelationType.RIGHT
        if (self.type == RelationType.RIGHT):
            return RelationType.LEFT


