# STRATEGY PATTERN
from math import pi, tan, sqrt


class Parameters:
	def __init__(self, parameter):
		self.parameter = parameter
		self.figure = ''

	def choose_figure(self, figure):
		self.figure = figure

	def area(self):
		result = self.figure.area(self.parameter)
		return round(result, 2) if result != round(result) else int(result)

	def perimeter(self):
		result = self.figure.perimeter(self.parameter)
		return round(result, 2) if result != round(result) else int(result)

	def volume(self):
		result = self.figure.volume(self.parameter)
		return round(result, 2) if result != round(result) else int(result)


class Circle:
	def area(self, radius):
		return radius ** 2 * pi

	def perimeter(self, radius):
		return radius * 2 * pi

	def volume(self, radius):
		return 0


class Triangle:
	def area(self, side):
		return sqrt(3) / 4 * side ** 2

	def perimeter(self, side):
		return side * 3

	def volume(self, side):
		return 0


class Square:
	def area(self, side):
		return side ** 2

	def perimeter(self, side):
		return side * 4

	def volume(self, side):
		return 0


class Pentagon:
	def area(self, side):
		return 2.5 * side ** 2 / (tan(36 * pi / 180) * 2)

	def perimeter(self, side):
		return side * 5

	def volume(self, side):
		return 0


class Hexagon:
	def area(self, side):
		return sqrt(3) * 6 / 4 * side ** 2

	def perimeter(self, side):
		return side * 6

	def volume(self, side):
		return 0


class Cube:
	def area(self, side):
		return side ** 2 * 6

	def perimeter(self, side):
		return side * 12

	def volume(self, side):
		return side ** 3


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing

	figure = Parameters(10)

	figure.choose_figure(Circle())
	assert figure.area() == 314.16

	figure.choose_figure(Triangle())
	assert figure.perimeter() == 30

	figure.choose_figure(Square())
	assert figure.area() == 100

	figure.choose_figure(Pentagon())
	assert figure.perimeter() == 50

	figure.choose_figure(Hexagon())
	assert figure.perimeter() == 60

	figure.choose_figure(Cube())
	assert figure.volume() == 1000

	print("Coding complete? Let's try tests!")
