import math

class Enemy:
	""" Properties """
	health = 21
	damage = 2
	skill = 5
	level = 1
	name = "Enemy"
	
	""" Constructor """
	def __init__(self, type, skill):
		names = ["Snake", "Rat", "Spider"]
		self.name = names[type]
		self.skill = skill
		self.updateStats(skill)
		print(self.name, "sighted! It is", self.skill, "x stronger than normal!")
	
	""" Methods """
	def attack(self, target):
		finalDamage = self.armorEffect(target)
		print(self.name, "attacks", target.name, 
			  "with", finalDamage, "DMG! Armor condition:", target.armor)
		print(target.name, "now has", target.health, "HP left.")
		
	def armorEffect(self, target):
		if target.armor >= 1:
			finalDamage = self.damage / 2 	# Armor reduces damage by 50 percent
			target.armor -= self.damage 	# Full damage amount is reduced from armor
		else:
			finalDamage = self.damage
		target.health -= math.ceil(finalDamage)
		return finalDamage
		
	def updateStats(self, skill):
		self.health *= skill
		self.damage *= skill