# Taken from mission Army Battles

# Taken from mission The Warriors

class Warrior:
	def __init__(self):
		self.health = 50
		self.attack = 5

	@property
	def is_alive(self):
		return self.health > 0

	def damage_taken(self, attack):
		self.health -= attack


class Knight(Warrior):
	def __init__(self):
		super().__init__()
		self.attack = 7


class Defender(Warrior):
	def __init__(self):
		self.health = 60
		self.attack = 3
		self.defense = 2

	def damage_taken(self, attack):
		if attack > self.defense:
			self.health -= attack - self.defense


class Army:
	def __init__(self):
		self.units = []

	def add_units(self, unit, amount):
		for i in range(amount):
			self.units.append(unit())


class Battle:
	def fight(self, army_1, army_2):
		i = 0
		j = 0
		length1 = len(army_1.units)
		length2 = len(army_2.units)
		while i < length1 and j < length2:
			if fight(army_1.units[i], army_2.units[j]):
				j += 1
			else:
				i += 1
		return True if j == length2 else False


def fight(unit_1, unit_2):
	while True:
		unit_2.damage_taken(unit_1.attack)
		if not unit_2.is_alive:
			return True
		unit_1.damage_taken(unit_2.attack)
		if not unit_1.is_alive:
			return False


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing

	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()

	assert fight(chuck, bruce) == True
	assert fight(dave, carl) == False
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False

	print("Coding complete? Let's try tests!")

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing

	# fight tests
	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()

	assert fight(chuck, bruce) == True
	assert fight(dave, carl) == False
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False

	# battle tests
	my_army = Army()
	my_army.add_units(Knight, 3)

	enemy_army = Army()
	enemy_army.add_units(Warrior, 3)

	army_3 = Army()
	army_3.add_units(Warrior, 20)
	army_3.add_units(Knight, 5)

	army_4 = Army()
	army_4.add_units(Warrior, 30)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == True
	assert battle.fight(army_3, army_4) == False
	print("Coding complete? Let's try tests!")

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing

	# fight tests
	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()
	bob = Defender()
	mike = Knight()
	rog = Warrior()
	lancelot = Defender()

	assert fight(chuck, bruce) == True
	assert fight(dave, carl) == False
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False
	assert fight(bob, mike) == False
	assert fight(lancelot, rog) == True

	# battle tests
	my_army = Army()
	my_army.add_units(Defender, 1)

	enemy_army = Army()
	enemy_army.add_units(Warrior, 2)

	army_3 = Army()
	army_3.add_units(Warrior, 1)
	army_3.add_units(Defender, 1)

	army_4 = Army()
	army_4.add_units(Warrior, 2)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == False
	assert battle.fight(army_3, army_4) == True
	print("Coding complete? Let's try tests!")
