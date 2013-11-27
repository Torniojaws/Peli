class Player:
	""" Properties """
	health = 100
	armor = 100
	damage = 5
	skill = 5
	level = 1
	experience = 0
	name = "Player"
	
	""" Constructor """
	def __init__(self, name):
		self.name = name
		print(name, " (Level ", self.level,") has entered the game!")
	
	""" Methods """
	def attack(self, target):
		target.health -= self.damage
		print(self.name, "attacks", target.name, "with", self.damage, "DMG!")
		print(target.name, "now has", target.health, "HP left")