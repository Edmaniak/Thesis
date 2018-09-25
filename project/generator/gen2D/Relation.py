from project.generator.gen2D.Object2D import Object2D


class Relation:
	def __init__(self, title: str, variance: float, object1: Object2D, object2: Object2D):
		self.title = title
		self.variance = variance
		self.object1 = object1
		self.object2 = object2
