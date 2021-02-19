class Warrior:
	def __init__(self):
		self.health = 50
		self.attack = 5

	@property
	def is_alive(self):
		return self.health > 0


@property
def max_health(self):
	return 50


def damage_taken(self, unit):
	self.health -= unit.attack


def damage_dealt(self, unit):
	unit.damage_taken(self)


def lanced(self, lancer):
	self.health -= 0.5 * lancer.attack


class Knight(Warrior):
	def __init__(self):
		super().__init__()
		self.attack = 7


class Defender(Warrior):
	def __init__(self):
		self.health = 60
		self.attack = 3
		self.defense = 2


	@property
	def max_health(self):
		return 60

	def damage_taken(self, unit):
		if unit.attack > self.defense:
			self.health -= unit.attack - self.defense

	def lanced(self, unit):
		if unit.attack * 0.5 > self.defense:
			self.health -= unit.attack * 0.5 - self.defense


class Vampire(Warrior):
	def __init__(self):
		super().__init__()
		self.health = 40
		self.attack = 4
		self.vampirism = 50


	@property
	def max_health(self):
		return 40

	def damage_dealt(self, unit):
		defense = 0
		if isinstance(unit, Defender):
			defense = unit.defense

	if unit.health < self.attack:
		self.health = min(40, self.health + (unit.health - defense) * self.vampirism / 100)
	else:
		self.health = min(40, self.health + (self.attack - defense) * self.vampirism / 100)
	unit.damage_taken(self)


class Lancer(Warrior):
	def __init__(self):
		super().__init__()
		self.attack = 6


class Healer(Warrior):
	def __init__(self):
		super().__init__()
		self.health = 60
		self.attack = 0

	@property
	def max_health(self):
		return 60

	def damage_dealt(self, unit):
		pass

	def heal(self, ally):
		ally.health = min(ally.max_health, ally.health + 2)


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
			if fight(army_1.units[i], army_2.units[j], army_1, army_2, i, j):
				j += 1
			else:
		i += 1

		return True if j == length2 else False


def straight_fight(self, army_1, army_2):
	copy_army_1 = Army()
	copy_army_1.units = [unit for unit in army_1.units]
	copy_army_2 = Army()
	copy_army_2.units = [unit for unit in army_2.units]

	while len(copy_army_1.units) != 0 and len(copy_army_2.units) != 0:
		i = 0
		print("-----")
		print(copy_army_1.units)
		print(" ")
		print(copy_army_2.units)
		print("-----")
		while i < len(copy_army_1.units) and i < len(copy_army_2.units):
			print(type(copy_army_1.units[i]))
			print(type(copy_army_2.units[i]))
			fight(copy_army_1.units[i], copy_army_2.units[i], copy_army_1, copy_army_2, i, i)
			i += 1

		print("CLASS 1")
		copy_army_1.units = [unit for unit in army_1.units if unit.is_alive]
		copy_army_2.units = [unit for unit in army_2.units if unit.is_alive]

	return True if copy_army_1.units else False


def fight(unit_1, unit_2, army_1=None, army_2=None, i=None, j=None):
	print("INDEX: " + str(i))
	while True:
		print(unit_1.health)
		print(unit_2.health)

		unit_1.damage_dealt(unit_2)
		if army_1:
			if len(army_2.units) > j + 1 and isinstance(army_1.units[i], Lancer):
				army_2.units[j + 1].lanced(army_1.units[i])
			if len(army_1.units) > i + 1 and isinstance(army_1.units[i + 1], Healer):
				army_1.units[i + 1].heal(army_1.units[i])

				if not unit_2.is_alive:
			print("WINNER: " + str(1))
			return True

		unit_2.damage_dealt(unit_1)
		if army_1:
			if len(army_1.units) > i + 1 and isinstance(army_2.units[j], Lancer):
				army_1.units[i + 1].lanced(army_2.units[j])
			if len(army_2.units) > j + 1 and isinstance(army_2.units[j + 1], Healer):
				army_2.units[j + 1].heal(army_2.units[j])

				if not unit_1.is_alive:
			print("WINNER: " + str(2))
			return False

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	army_1 = Army()
	army_2 = Army()
	army_1.add_units(Lancer, 7)
	army_1.add_units(Vampire, 3)
	army_1.add_units(Healer, 1)
	army_1.add_units(Warrior, 4)
	army_1.add_units(Healer, 1)
	army_1.add_units(Defender, 2)
	army_2.add_units(Warrior, 4)
	army_2.add_units(Defender, 4)
	army_2.add_units(Healer, 1)
	army_2.add_units(Vampire, 6)
	army_2.add_units(Lancer, 4)
	battle = Battle()
	assert battle.straight_fight(army_1, army_2) == False