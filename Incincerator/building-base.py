class Building:
	def __init__(self, south, west, width_WE, width_NS, height=10):
		self.coordinates = [south, west]
		self.horizontal = width_WE
		self.vertical = width_NS
		self.height = height

	def corners(self):
		return {"north-west": [self.coordinates[0] + self.vertical, self.coordinates[1]],
				"north-east": [self.coordinates[0] + self.vertical, self.coordinates[1] + self.horizontal],
				"south-west": [self.coordinates[0], self.coordinates[1]],
				"south-east": [self.coordinates[0], self.coordinates[1] + self.horizontal]
				}

	def area(self):
		return self.horizontal * self.vertical

	def volume(self):
		return self.horizontal * self.vertical * self.height

	def __repr__(self):
		return 'Building({south}, {west}, {width_we}, {width_ns}, {height})'.format(
			south=self.coordinates[0], west=self.coordinates[1],
			width_we=self.horizontal, width_ns=self.vertical,
			height=self.height)


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	def json_dict(d):
		return dict((k, list(v)) for k, v in d.items())


	b = Building(1, 2, 2, 3)
	b2 = Building(1, 2, 2, 3, 5)
	assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
									  'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
	assert b.area() == 6, "Area"
	assert b.volume() == 60, "Volume"
	assert b2.volume() == 30, "Volume2"
	assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
