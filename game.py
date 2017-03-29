"""The main game file.

Do indeed enjoy:)
"""

from sys import exit
from random import randint

prompt = '--> '

class Scene(object): # Add things here for the subclasses
	
	def enter(self):
		print("Error.")
		exit(1)

class Engine(object): # Running the rooms

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('final_room')

		while current_scene != last_scene:
			print(current_scene)
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()

class White_room(Scene): # Look up a game engine online for inspiration

	def enter(self):
		print("You are dizzy and blended by a strong light source.")
		print("You try to get up but you realize in the same moment")
		print("that you are tied to a chair with handcuffs. What the")
		print("hell is happening?")
		print("Someone comes through the door and the first thing you")
		print("notice is the key chain attached to the persons waist.")
		print("You then look up and you see that it is a person with white")
		print("clothes and looks much like a doctor. You decide to ask the")
		print("doctor where you are but she doesn't reply. You repeat yourself")
		print("but still no answer. She now takes a needle rolls up your sleeve.")
		print("You notice that you can reach the keys. Do you (take) them or let her")
		print("(inject) the liquid in the needle?")
		choice = input(prompt)

		if choice == 'take':
			print("You pull the keys from her and she looks chocked and tries to grab them back")
			print("You push her away and barely manage to open your handcuffs but you somehow do it.")
			print("Now she comes charging at you with the needle and tries to stab you with it.")
			print("Are you going to (flee) by running out of the door or try to (disarm) her?.")
			choice = input(prompt)

			if choice == 'flee':
				return 'wired_room'

			elif choice == 'disarm':
				return 'death'

			else:
				return 'death'

		elif choice == 'inject':
			print("You feel a sting in your arm and fall asleep. You never woke up again...")
			
			return 'death'
		
		else:
			print("There is no command of that choice.")

			return 'white_room'

class Central_corridor(Scene):

	def enter(self):
		print("You are now in the central corridor.")

class Wired_room(Scene):

	def enter(self):
		print("You are now in the wired room.")

class Lab(Scene):
	
	def enter(self):
		print("You are now in the lab.")

class Doctors(Scene):

	def enter(self):
		print("You are now in the doctors room.")

class Final_room(object):
	
	def enter(self):
		print("You are now in the final room.")

class Death(Scene):

	def enter(self):
		print("Game over.")
		exit(0)

class Boss(object):

	def __init__(self, hp, name):
		self.hp = hp
		self.name = name

	def boss_1(self, weapon):
		self.weapon = 'Shovel'

class Hero(object):

	def __init__(self, name):
		self.hp = 100
		self.name = name

	def eat(self, food):
		self.food = food

		if self.food == "pie":
			print("Yummy")
			self.hp += 20

		elif self.food == "cookie":
			print("The hero does not like cookies")
			self.hp -= 10

		else:
			print("You don't have that item.")
			# return current_room

class Map(object):

	scenes = {
		'white_room': White_room(),
		'central_corridor': Central_corridor(),
		'wired_room': Wired_room(),
		'lab': Lab(),
		'doctors': Doctors(),
		'final_room': Final_room(),
		'death': Death()
		}
    
	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('white_room')
a_game = Engine(a_map)
a_game.play()

# Figure out the return thing, make the engine work!