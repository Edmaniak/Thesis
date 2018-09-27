class Object:
	constraint = ['LAST', 'FIRST']

	def __init__(self, title, val=0):
		self.val = min(max(val, 0), 255)
		self.title = title
		self.logical_const = list()
		self.object_const = list()
		self.possibilities = []

	def __str__(self):
		return self.title

	def set_logical_const(self, key_word):
		if key_word in self.constraint:
			self.logical_const.append(key_word)

	def set_object_const(self, object, type):
		pass
