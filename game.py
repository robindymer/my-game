"""The main game file.

Do indeed enjoy:)
"""

from sys import exit
from random import randint

prompt = '--> '

class Scene(object): # Add things here for the subclasses
	
	pass

class Engine(object): # Running the rooms

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('final_room')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()

class White_room(Scene): # Look up a game engine online for inspiration

	def enter(self):
		print("You are dizzy and blended by a strong light source.")
		print("You try to get up but you realize in the same moment")
		print("that you are tied to a chair with handcuffs. What the")
		print("hell is happening?\n")
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
			print("\nYou pull the keys from her and she looks chocked and tries to grab them back")
			print("You push her away and barely manage to open your handcuffs but you somehow do it.")
			print("Now she comes charging at you with the needle and tries to stab you with it.")
			print("Are you going to (flee) by running out of the door or try to (disarm) her?.")
			choice = input(prompt)

			if choice == 'flee':
				return 'central_corridor'

			elif choice == 'disarm':
				print("\nYou grab her hand with the needle in it but you can't hold it for more than")
				print("a couple of seconds because of the dizziness. She manage to inject the needles liquid")

				return 'death'

			else:
				print("\nThere is no command of that choice. Start over.\n")

				return 'white_room'

		elif choice == 'inject':
			print("\nYou feel a sting in your arm and fall asleep. You never woke up again...")
			
			return 'death'
		
		else:
			print("\nThere is no command of that choice. Start over.\n")

			return 'white_room'

class Central_corridor(Scene):

	def enter(self): # Add your weapon in this class or another one
		print("\nYou run out and quickly shut the door so she can't come out. Close one.")
		print("You look around and see a long, white corridor. What is this place?")
		print("You try to remember why you are here but nothing comes up.")
		print("You try to remember your name but you just can't.")
		print("You try to remember who you are and something, just something, but nothing")
		print("comes to your mind.")
		print("\nYou realize that you need to get of here as quickly as you can. This is not")
		print("an ordinary hospital")
		print("You see three doors with different text on each one")
		print("The first door says (wire), the second door says (lab) and the")
		print("last door says (staff). Which one do you enter?")
		choice = input(prompt)

		if choice == 'wire':
			return 'wired_room'

		elif choice == 'lab':
			return 'lab'

		elif choice == 'staff':
			return 'Doctors'

		else:
			print("There is no command of that choice. Start over.")

			return 'central_corridor'

class Wired_room(Scene):

	def enter(self):
		print("You enter the door with the sign that says 'wire'.")
		print("When you open the door you first notice the enormous size of the room.")
		print("Then you see a bunch of people laying down in black machines with wires to their head.")
		print("They are not awake. You become so chocked that you can barely stand on your legs.")
		print("Poor people. Who have done this? What are they doing do them?")
		print("You look around and see a desk with a bunch of maps on it.")
		print("Do you (go) to the maps or (inspect) the machines with the people in it?")
		choice = input(prompt)

		if choice is 'go':
			pass

		elif choice is 'inspect':
			pass

		else:
			print("There is no command of that choice. Start over.")

			return 'wired_room'

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

class Intro(object):

	def __init__(self):
		pass

	def explain(self):
		print("\n---- Wiped ----\n")
		print("Welcome to my game called 'Wiped'. A game about finding out the truth...")
		self.name = input("First of all, choose your name: ") # Set a maximun of characters in the name
		self.name = self.name.capitalize()

		print("Are you ready {}? Press ENTER to start or CTRL-SHIFT-C to quit.".format(self.name))
		input()
		print("Let's begin...\n") # Add a delay in here with the time module


the_intro = Intro()
the_intro.explain()

a_map = Map('white_room')
a_game = Engine(a_map)
a_game.play()

# Figure out the return thing, make the engine work!