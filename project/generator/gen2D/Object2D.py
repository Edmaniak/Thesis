class Object2D:
	def __init__(self, title: str, min_x: int, max_x: int, min_y: int, max_y: int):
		self.title = title
		self.min_x = min_x
		self.max_x = max_x
		self.min_y = min_y
		self.max_y = max_y
		self.relations = list()
