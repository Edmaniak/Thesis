from project.generator.gen2D.Object2D import Object2D
from project.generator.gen2D.Relation import Relation


class Space2D:
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height
        self.relations = list()
        self.objects = list()

    def add_relation(self, relation: Relation):
        self.relations.append(relation)

        self.add_object(relation.object1)
        self.add_object(relation.object2)

    def add_object(self, object: Object2D):
        if(not self.objects.__contains__(object)):
            self.objects.append(object)
