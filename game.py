from classes.player import Player
from classes.enemy import Enemy

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
		
game = Game()
game.start()
player = Player("Juha")
enemy = Enemy("Snake")

while game.isRunning:
	player.attack(enemy)
	if enemy.health >= 1:
		enemy.attack(player)
	else:
		experience = enemy.damage * 2
		print(enemy.name, "is defeated! You have earned", experience, "XP!")
		player.experience += experience
		game.isRunning = False
	if player.health <= 0:
		print(player.name, "has died! Game over, man!")
		game.isRunning = False