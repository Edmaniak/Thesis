from project.generator.gen1D import Object1D


class Constraint1D:
	types = ['UNDER', "ABOVE", "UNDER_CLOSE", "ABOVE_CLOSE"]

	def __init__(self, object: Object1D, type: str):
		if type in self.types:
			self.object = object
			self.type = type

	def __str__(self):
		return super().__str__()