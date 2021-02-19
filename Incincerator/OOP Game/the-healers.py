# Taken from mission The Lancers

# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

# Taken from mission The Warriors
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
		self.health -= max(unit.attack * 0.5 - self.defense, 0)


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


def fight(unit_1, unit_2, army_1=None, army_2=None, i=None, j=None):
	while True:
		unit_1.damage_dealt(unit_2)
		if army_1:
			if len(army_2.units) > j + 1 and isinstance(army_1.units[i], Lancer):
				army_2.units[j + 1].lanced(army_1.units[i])
			if len(army_1.units) > i + 1 and isinstance(army_1.units[i + 1], Healer):
				army_1.units[i + 1].heal(army_1.units[i])

		if not unit_2.is_alive:
			return True

		unit_2.damage_dealt(unit_1)
		if army_2:
			if len(army_1.units) > i + 1 and isinstance(army_2.units[j], Lancer):
				army_1.units[i + 1].lanced(army_2.units[j])
			if len(army_2.units) > j + 1 and isinstance(army_2.units[j + 1], Healer):
				army_2.units[j + 1].heal(army_2.units[j])

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
	eric = Vampire()
	adam = Vampire()
	richard = Defender()
	ogre = Warrior()

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
	assert fight(eric, richard) == False
	assert fight(ogre, adam) == True

	# battle tests
	my_army = Army()
	my_army.add_units(Defender, 2)
	my_army.add_units(Vampire, 2)
	my_army.add_units(Warrior, 1)

	enemy_army = Army()
	enemy_army.add_units(Warrior, 2)
	enemy_army.add_units(Defender, 2)
	enemy_army.add_units(Vampire, 3)

	army_3 = Army()
	army_3.add_units(Warrior, 1)
	army_3.add_units(Defender, 4)

	army_4 = Army()
	army_4.add_units(Vampire, 3)
	army_4.add_units(Warrior, 2)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == False
	assert battle.fight(army_3, army_4) == True
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
	eric = Vampire()
	adam = Vampire()
	richard = Defender()
	ogre = Warrior()
	freelancer = Lancer()
	vampire = Vampire()

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
	assert fight(eric, richard) == False
	assert fight(ogre, adam) == True
	assert fight(freelancer, vampire) == True
	assert freelancer.is_alive == True

	# battle tests
	my_army = Army()
	my_army.add_units(Defender, 2)
	my_army.add_units(Vampire, 2)
	my_army.add_units(Lancer, 4)
	my_army.add_units(Warrior, 1)

	enemy_army = Army()
	enemy_army.add_units(Warrior, 2)
	enemy_army.add_units(Lancer, 2)
	enemy_army.add_units(Defender, 2)
	enemy_army.add_units(Vampire, 3)

	army_3 = Army()
	army_3.add_units(Warrior, 1)
	army_3.add_units(Lancer, 1)
	army_3.add_units(Defender, 2)

	army_4 = Army()
	army_4.add_units(Vampire, 3)
	army_4.add_units(Warrior, 1)
	army_4.add_units(Lancer, 2)

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
	eric = Vampire()
	adam = Vampire()
	richard = Defender()
	ogre = Warrior()
	freelancer = Lancer()
	vampire = Vampire()
	priest = Healer()

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
	assert fight(eric, richard) == False
	assert fight(ogre, adam) == True
	assert fight(freelancer, vampire) == True
	assert freelancer.is_alive == True
	assert freelancer.health == 14
	priest.heal(freelancer)
	assert freelancer.health == 16

	# battle tests
	my_army = Army()
	my_army.add_units(Defender, 2)
	my_army.add_units(Healer, 1)
	my_army.add_units(Vampire, 2)
	my_army.add_units(Lancer, 2)
	my_army.add_units(Healer, 1)
	my_army.add_units(Warrior, 1)

	enemy_army = Army()
	enemy_army.add_units(Warrior, 2)
	enemy_army.add_units(Lancer, 4)
	enemy_army.add_units(Healer, 1)
	enemy_army.add_units(Defender, 2)
	enemy_army.add_units(Vampire, 3)
	enemy_army.add_units(Healer, 1)

	army_3 = Army()
	army_3.add_units(Warrior, 1)
	army_3.add_units(Lancer, 1)
	army_3.add_units(Healer, 1)
	army_3.add_units(Defender, 2)

	army_4 = Army()
	army_4.add_units(Vampire, 3)
	army_4.add_units(Warrior, 1)
	army_4.add_units(Healer, 1)
	army_4.add_units(Lancer, 2)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == False
	assert battle.fight(army_3, army_4) == True
	print("Coding complete? Let's try tests!")
