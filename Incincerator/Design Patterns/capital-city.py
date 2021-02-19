# SINGLETON
class Singleton(type):
	instance = None

	def __call__(cls, *args, **kwargs):
		if cls.instance is None:
			cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
		return cls.instance


class Capital(metaclass=Singleton):
	def __init__(self, name):
		self._name = name

	def name(self):
		return self._name


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing

	ukraine_capital_1 = Capital("Kyiv")
	ukraine_capital_2 = Capital("London")
	ukraine_capital_3 = Capital("Marocco")

	assert ukraine_capital_2.name() == "Kyiv"
	assert ukraine_capital_3.name() == "Kyiv"

	assert ukraine_capital_2 is ukraine_capital_1
	assert ukraine_capital_3 is ukraine_capital_1

	print("Coding complete? Let's try tests!")
