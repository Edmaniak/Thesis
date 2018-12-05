from project.generator.gen1D.Object import Object


class Object1D(Object):

	def __init__(self, title, val=0):
		super().__init__(title, val)
		self.obligatory = False
		self.is_above = []
		self.is_under = []

	def __str__(self):
		return str(self.val)

	def set_obligatory(self):
		self.obligatory = True

	def set_object_const(self, type: str, object: Object):

		if type == "ABOVE":
			self.set_above(object)
			object.set_under(self)

		if type == "UNDER":
			self.set_under(object)
			object.set_above(self)

	def set_above(self, object):
		self.is_above.append(object)

	def set_under(self, object):
		self.is_under.append(object)
