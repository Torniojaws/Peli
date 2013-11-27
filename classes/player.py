import math

class Player:
	""" Properties """
	level = 1
	health = level * 50
	armor = level * 100
	damage = 5
	skill = level * 5
	experience = 0
	name = "Player"
	
	""" Constructor """
	def __init__(self, name):
		self.name = name
		print(name, "(Level", self.level, ") has entered the game!")
	
	""" Methods """
	def attack(self, target):
		target.health -= math.ceil(self.damage)
		print(self.name, "attacks", target.name, "with", self.damage, "DMG!")
		print(target.name, "now has", target.health, "HP left")
		
	def showStatistics(self):
		print("===")
		print("Level:", self.level)
		print("EXP:", self.experience)
		print("DMG:", self.damage)
		print("HP:", self.health)
		print("Armor:", self.armor)
		print("Skill:", self.skill)
		print("===")
		
	def maxHealthAndArmor(self):
		self.health = self.level * 50
		self.armor = self.level * 100