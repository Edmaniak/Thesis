from project.generator.gen2D.Relation import RelationType, Relation


class Object2D:
    def __init__(self, title: str, min_x: int = 0, max_x: int = 0, min_y: int = 0, max_y: int = 0):
        self.title = title
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.relations = list()

    def add_relation(self, object2: Object2D, relationType: RelationType):
        self.relations.append(Relation(self, relationType, object2))
        object2.relations.append(Relation(self, relationType, object2).get_reverse())
