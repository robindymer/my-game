"""The main game file.

Do indeed enjoy:)
"""

import webbrowser
from sys import exit
from random import randint, choice
from time import sleep

prompt = '->> '
been_there = ['wired_room', 'lab', 'doctors']
excepting = ['white_room', 'central_corridor', 'final_room', 'death', 'fight']

class Scene(object): # Add things here for the subclasses
	
	pass

class Engine(object): # Running the rooms

	def __init__(self, scene_map):
		self.scene_map = scene_map

		# if wired_room is in been_there
		if self.scene_map in been_there:
			been_there.remove(self.been_there)

		# if wired_room is not in expecting and not in been_there.
		elif self.scene_map not in been_there and self.scene_map not in excepting:
			Engine('death').play()

	def play(self):
		print(self.scene_map)
		input()
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
		print("You look down on your arms and they are as white as the room.")
		print("You also see a number written on your arm, '2'.")
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
			print("\nThere is no command of that choice. Start over.\n")

			return 'central_corridor'

class Wired_room(Scene):

	def enter(self):
		print("\nYou enter the door with the sign that says 'wire'.")
		print("When you open the door you first notice the enormous size of the room.")
		print("Then you see a bunch of people laying down in black machines with wires to their head.")
		print("They are not awake. You become so chocked that you can barely stand on your legs.")
		print("Poor people. Who have done this? What are they doing do them?")
		print("You look around and see a desk with a bunch of maps on it.")
		print("Do you (go) to the maps or (inspect) the machines with the people in it?")
		choice = input(prompt)

		if choice == 'go':
			print("\nYou walk to the desk and pick up one of the papers.")
			print("You start reading")
			input()
			text = open('text.txt').read()
			
			for l in text:
				print(l, end="", flush=True)
				sleep(0.01)
			input()
			print("\nYou look down on your arm and see the same number you saw in the other room, '2'.")
			print("'What is a transfer, who am I, please let me remember!', you burst out.")
			print("You suddenly see someone coming through the door. It is a big muscular doctor that is looking down")
			print("in a folder and going around the machines and checking them.")
			print("Do you (fight) him or do you (hide)?")
			choice = input(prompt)

			if choice == 'fight':
				return 'fight'

			elif choice == 'hide':
				print("\nYou throw yourself down on your knees and try to stay quiet, but the pain from")
				print("hitting the knees hard in the floor makes you scream out in pain. That is not good.")
				print("Now he sees you and comes charging at you. That is the last thing you ever would remember...")

				return 'death'

			else:
				print("\nThere is no command of that choice. Start over.\n")

				return 'wired_room'

		elif choice == 'inspect':
			return 'death'

		else:
			print("\nThere is no command of that choice. Start over.\n")

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
		gif_links = ["https://giphy.com/gifs/love-black-and-white-fail-dkuZHIQsslFfy/tile",
		             "https://giphy.com/gifs/cat-video-game-xn9yw4QWUiC2Y/tile",
		             "https://giphy.com/gifs/kawaii-pixel-pixels-WDsyMtVD8ZH7G/tile",
		             "https://giphy.com/gifs/season-3-the-simpsons-3x8-l2Je1pHtloVlENuJa/tile"]

		print("\nYou died...\n")
		sleep(1)
		webbrowser.open(choice(gif_links))
		exit(0)

class Hero(object): # Put the hero, bosses and everything like that in a module

	def __init__(self, name):
		self.hero_hp = 100
		self.hero_name = hero_name

	def eat(self, food):
		self.food = food

		if self.food == "pie":
			print("Yummy")
			self.hero_hp += 20

		elif self.food == "cookie":
			print("The hero does not like cookies")
			self.hero_hp -= 10

		else:
			print("You don't have that item.")
			# return current_room

class Boss(Hero):

	def __init__(self, hp, name):
		self.hp = hp
		self.name = name

	def boss_1(self):
		super().__init__()
		self.hero_hp = hero_hp
		self.hero_abilitys = {}
		self.boss_weapon = 'shovel'
		self.hero_weapon = 'stick'

		if self.hero_weapon == 'stick':
			self.hero_abilitys = {
				'poke': randint(15, 25),
				'throw': randint(25, 30),
				'hit': randint(10, 15)
				}

class Fight(Boss):

	def __init__(self):
		self.enters = 0

	def enter(self): # Boss parameter? Make it so that you can come back to this scene with different bosses from the boss class
		self.enters += 1
		
		if self.enters == 1:
			super().boss_1()
			print("\nBoss number 1...\n")
			print("Boss weapon: {}".format(self.boss_weapon))
			print("Your weapon: {}".format(self.hero_weapon))
			print("\nType (abilitys) to get a list of your abilitys.")

			while self.hero_hp < 0 or self.boss_hp < 0:
				choice = input("Choose ability: ")

				if choice == 'poke':
					self.boss_hp -= self.hero_abilitys[choice]
					self.hero_hp -= randint(10, 20)
					input()

				elif choice == 'throw':
					pass

				elif choice == 'hit':
					pass

				elif choice == 'abilitys':
					print(self.hero_abilitys.items())

		else:
			return 'death'

class Map(object):

	scenes = {
		'white_room': White_room(),
		'central_corridor': Central_corridor(),
		'wired_room': Wired_room(),
		'lab': Lab(),
		'doctors': Doctors(),
		'final_room': Final_room(),
		'death': Death(),
		'fight': Fight()
		}
    
	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

class Intro(object):

	def explain(self):
		print("\n---- Wiped ----\n")
		print("Welcome to my game called 'Wiped'. A game about finding out the truth...")
		self.name = input("First of all, choose your name: ") # Set a maximun of characters in the name
		self.name = self.name.capitalize()

		print("Are you ready {}? Press ENTER to start or CTRL-SHIFT-C to quit.".format(self.name))
		input()
		print("Let's begin", end="") # Add a delay in here with the time module
		for _ in range(3):
			print(".", end="", flush=True)
			sleep(1)


the_intro = Intro()
the_intro.explain()

a_map = Map('wired_room')
a_game = Engine(a_map)
a_game.play()