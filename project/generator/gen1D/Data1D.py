from random import randint
from random import shuffle
import csv

from project.generator.gen1D.Object1D import Object1D


class Data1D:
	def __init__(self, data=list()):
		self.data = data
		self.hierarchies = list()

	def add_data(self, object: Object1D):
		self.data.append(object)

	def set_data(self, data):
		self.data = data

	def generate(self, number_of_samples: int = 1000, format: str = "csv", ratio: int = 50, do_shuffle=True,
	             label_it=True):

		positive = self.generate_positive(number_of_samples, "array")
		negative = self.generate_random(number_of_samples, "array")

		# Check if there are nor equivalent records in the random array as they are in the positive
		for record_negative in negative:
			for record_positive in positive:
				if len(record_negative) == len(record_positive):
					for i in range(0, len(record_negative)):
						if record_negative[i].title == record_positive[i].title:
							continue
						else:
							break
						negative.remove(record_negative)

		if label_it:
			for record in positive:
				record.append("1")
			for record in negative:
				record.append("0")

		if do_shuffle:
			shuffle(positive)
			shuffle(negative)

		merged_result = positive + negative

		if do_shuffle:
			shuffle(merged_result)

		if format == "print":
			self.print_data(merged_result)

		if format == "array":
			return merged_result

		if format == "csv":
			with open('toast_data.csv', 'w', newline='') as f:
				writer = csv.writer(f)
				for record in merged_result:
					writer.writerow(record)

	def generate_positive(self, number_of_samples=10, format: str = "print"):
		results = []
		i = 0
		while i < number_of_samples:

			record = []
			data_ok = True
			r1 = randint(0, len(self.data) - 1)

			while len(self.data[r1].is_above) == 0 and len(self.data[r1].is_under) == 0:
				r1 = randint(0, len(self.data) - 1)

			root = self.data[r1]
			dir = randint(0, 1)

			if dir == 1 and len(root.is_above) > 0:
				record.append(root)
				end = randint(0, 10)
				while len(root.is_above) > 0 and end > 2:
					r2 = randint(0, len(root.is_above) - 1)
					root = root.is_above[r2]
					record.append(root)
				record.reverse()

			if dir == 0 and len(root.is_under) > 0:
				record.append(root)
				end = randint(0, 10)
				while len(root.is_under) > 0 and end > 2:
					r2 = randint(0, len(root.is_under) - 1)
					root = root.is_under[r2]
					record.append(root)

			for object in self.data:
				if object.obligatory and object not in record:
					data_ok = False

			if len(record) > 0 and data_ok:
				results.append(record)
				i += 1

		if format == "print":
			self.print_data(results)

		if format == "array":
			return results

	def generate_random(self, number_of_samples=10, format: str = "print"):
		results = []
		i = 0
		while i < number_of_samples:
			record = []
			count = randint(1, len(self.data))
			for r in range(0, count):
				rand = randint(0, len(self.data) - 1)
				if self.data[rand] not in record:
					record.append(self.data[rand])
			results.append(record)
			i += 1

		if format == "print":
			self.print_data(results)

		if format == "array":
			return results

	@staticmethod
	def print_data(result_array):
		for r in result_array:
			print("[ ", end="")
			for d in range(0, len(r)):
				print(str(r[d]) + ", ", end="")
			print("] \n")
