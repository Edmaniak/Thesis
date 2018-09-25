from project.generator.gen2D.Object2D import Object2D


class Space2D:
	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height
		self.objects = list()

	def add_object(self, object: Object2D):
		self.objects.append(object)

	def remove_object(self, object: Object2D):
		self.objects.remove(object)


