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

	def damage_taken(self, attack):
		self.health -= attack
		return attack

	def damage_dealt(self, unit):
		return unit.damage_taken(self.attack)

	def lanced(self, attack):
		self.health -= 0.5 * attack


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

	def damage_taken(self, attack):
		self.health -= max(0, attack - self.defense)
		return max(0, attack - self.defense)

	def lanced(self, attack):
		self.health -= max(0, attack * 0.5 - self.defense)


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
		damage = super().damage_dealt(unit)
		self.health = min(40, self.health + damage * self.vampirism // 100)


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

	@property
	def first_alive_unit(self):
		for unit in self.units:
			if unit.is_alive:
				return unit

	def next_unit(self, unit):
		i = self.units.index(unit)
		if i + 1 < len(self.units):
			return self.units[i + 1]
		return False

	@property
	def is_alive(self):
		return self.first_alive_unit is not None


class Battle:
	def fight(self, army_1, army_2):
		while army_1.is_alive and army_2.is_alive:
			unit_1 = army_1.first_alive_unit
			unit_2 = army_2.first_alive_unit
			fight(unit_1, unit_2, army_1, army_2)

		return army_1.is_alive


def fight(unit_1, unit_2, army_1=None, army_2=None):
	army_1_next_unit = None
	army_2_next_unit = None

	if army_1:
		army_1_next_unit = army_1.next_unit(unit_1)
	if army_2:
		army_2_next_unit = army_2.next_unit(unit_2)

	while True:
		unit_1.damage_dealt(unit_2)
		if army_2_next_unit and isinstance(unit_1, Lancer):
			army_2_next_unit.lanced(unit_1.attack)
		if army_1_next_unit and isinstance(army_1_next_unit, Healer):
			army_1_next_unit.heal(unit_1)
		if not unit_2.is_alive:
			return True

		unit_2.damage_dealt(unit_1)
		if army_1_next_unit and isinstance(unit_2, Lancer):
			army_1_next_unit.lanced(unit_2.attack)
		if army_2_next_unit and isinstance(army_2_next_unit, Healer):
			army_2_next_unit.heal(unit_2)
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
