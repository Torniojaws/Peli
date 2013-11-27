from classes.player import Player
from classes.enemy import Enemy
import random

class Game:
	""" Properties """
	status = 0
	isRunning = False
	
	""" Constructor """
	def __init__(self):
		print("Ready to go!")
	
	""" Methods """
	def start(self):
		game.isRunning = True
		print("We have lift-off!")
	
	def generateOpponent(self, player):
		enemyType = random.randint(0, 2)
		enemySkill = player.skill * random.randint(1, 4) * 0.12
		return Enemy(enemyType, enemySkill)
		
	def playerLevelUp(self, player):
		player.level += 1
		player.experience == 0 # Experience is per level
		player.skill += 5
		player.maxHealthAndArmor()
		print("!! You have leveled up to level", player.level, "!!")
		
game = Game()
game.start()
player = Player("Juha")

while game.isRunning:
	enemy = game.generateOpponent(player)
	pick = input("Do you wish to attack? Y/N")
	if pick == "Y":
		while enemy.health >= 1:
			player.attack(enemy)
			if enemy.health >= 1:
				enemy.attack(player)
			else:
				experience = enemy.damage * 2
				print(enemy.name, "is defeated! You have earned", experience, "XP!")
				player.experience += experience
				if player.experience >= player.level * 10:
					game.playerLevelUp(player)
				player.showStatistics()
			if player.health <= 0:
				print(player.name, "has died! Game over, man!")
				game.isRunning = False
				break
	else:
		continue