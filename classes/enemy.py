class Enemy:
	""" Properties """
	health = 100
	armor = 100
	damage = 2
	skill = 5
	level = 1
	name = "Enemy"
	
	""" Constructor """
	def __init__(self, name):
		self.name = name
		print(name, "sighted!")
	
	""" Methods """
	def attack(self, target):
		target.health -= self.damage
		print("Enemy attacks", target.name, "with", self.damage, "DMG!")