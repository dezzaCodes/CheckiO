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

	def equip_weapon(self, weapon_name):
		self.health += weapon_name.health
		self.attack += weapon_name.attack


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

	def equip_weapon(self, weapon_name):
		super().equip_weapon(weapon_name)
		self.defense += weapon_name.defense


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


def equip_weapon(self, weapon_name):
	super().equip_weapon(weapon_name)
	self.vampirism += weapon_name.vampirism


class Lancer(Warrior):
	def __init__(self):
		super().__init__()
		self.attack = 6


class Healer(Warrior):
	def __init__(self):
		super().__init__()
		self.health = 60
		self.attack = 0
		self.heal_power = 2

	@property
	def max_health(self):
		return 60

	def damage_dealt(self, unit):
		pass

	def heal(self, ally):
		ally.health = min(ally.max_health, ally.health + self.heal_power)

	def equip_weapon(self, weapon_name):
		super().equip_weapon(weapon_name)
		self.heal_power += weapon_name.heal_power


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

	@property
	def alive_units(self):
		return [unit for unit in self.units if unit.is_alive]


class Battle:
	def fight(self, army_1, army_2):
		while army_1.is_alive and army_2.is_alive:
			unit_1 = army_1.first_alive_unit
			unit_1_next = army_1.next_unit(unit_1)
			unit_2 = army_2.first_alive_unit
			unit_2_next = army_2.next_unit(unit_2)

			fight(unit_1, unit_2, unit_1_next, unit_2_next)
		return army_1.is_alive

	def straight_fight(self, army_1, army_2):
		while army_1.is_alive and army_2.is_alive:
			for unit_1, unit_2 in zip(army_1.alive_units, army_2.alive_units):
				fight(unit_1, unit_2)
		return army_1.is_alive


class Weapon:
	def __init__(self, health, attack, defense=0, vampirism=0, heal_power=0):
		self.health = health
		self.attack = attack
		self.defense = defense
		self.vampirism = vampirism
		self.heal_power = heal_power


class Sword(Weapon):
	def __init__(self):
		super().__init__(health=5, attack=2)


class Shield(Weapon):
	def __init__(self):
		super().__init__(health=20, attack=-1, defense=2)


class GreatAxe(Weapon):
	def __init__(self):
		super().__init__(health=-15, attack=5, defense=-2, vampirism=10)


class Katana(Weapon):
	def __init__(self):
		super().__init__(health=-20, attack=6, defense=-5, vampirism=50)


class MagicWand(Weapon):
	def __init__(self):
		super().__init__(health=30, attack=3, heal_power=3)


def fight(unit_1, unit_2, next_unit_1=None, next_unit_2=None):
	while True:
		unit_1.damage_dealt(unit_2)
		if next_unit_2 and isinstance(unit_1, Lancer):
			next_unit_2.lanced(unit_1.attack)
		if next_unit_1 and isinstance(next_unit_1, Healer):
			next_unit_1.heal(unit_1)
		if not unit_2.is_alive:
			return True

		unit_2.damage_dealt(unit_1)
		if next_unit_1 and isinstance(unit_2, Lancer):
			next_unit_1.lanced(unit_2.attack)
		if next_unit_2 and isinstance(next_unit_2, Healer):
			next_unit_2.heal(unit_2)
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

	army_5 = Army()
	army_5.add_units(Warrior, 10)

	army_6 = Army()
	army_6.add_units(Warrior, 6)
	army_6.add_units(Lancer, 5)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == False
	assert battle.fight(army_3, army_4) == True
	assert battle.straight_fight(army_5, army_6) == False
	print("Coding complete? Let's try tests!")

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing

	ogre = Warrior()
	lancelot = Knight()
	richard = Defender()
	eric = Vampire()
	freelancer = Lancer()
	priest = Healer()

	sword = Sword()
	shield = Shield()
	axe = GreatAxe()
	katana = Katana()
	wand = MagicWand()
	super_weapon = Weapon(50, 10, 5, 150, 8)

	ogre.equip_weapon(sword)
	ogre.equip_weapon(shield)
	ogre.equip_weapon(super_weapon)
	lancelot.equip_weapon(super_weapon)
	richard.equip_weapon(shield)
	eric.equip_weapon(super_weapon)
	freelancer.equip_weapon(axe)
	freelancer.equip_weapon(katana)
	priest.equip_weapon(wand)
	priest.equip_weapon(shield)

	ogre.health == 125
	lancelot.attack == 17
	richard.defense == 4
	eric.vampirism == 200
	freelancer.health == 15
	priest.heal_power == 5

	fight(ogre, eric) == False
	fight(priest, richard) == False
	fight(lancelot, freelancer) == True

	my_army = Army()
	my_army.add_units(Knight, 1)
	my_army.add_units(Lancer, 1)

	enemy_army = Army()
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 1)

	my_army.units[0].equip_weapon(axe)
	my_army.units[1].equip_weapon(super_weapon)

	enemy_army.units[0].equip_weapon(katana)
	enemy_army.units[1].equip_weapon(wand)

	battle = Battle()

	battle.fight(my_army, enemy_army) == True
	print("Coding complete? Let's try tests!")