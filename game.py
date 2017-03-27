"""Game story:

You wake up in a bright white room. You are dizzy and blended 
but you feel better after a while. You don't remember anything
and you a trapped in a chair. Now you need to escape, find out
what's happening and get memory fragments to remember your
story. You will need to go through rooms, fight bosses,
collect memory fragments and when you have all of the memory
fragments, you are ready for the final mission. You will also
find notes on the way that will tell you things about what's
happening.
You are going to have a name, health bar, weapons, abilitys.
The user is going to be able to get help for knowing that the
options are, the abilitys he have and the things he can do.
Try to find good modules for intresting stuff, maybe open gif's
for different scenes.
There will be different rooms and each room is going to have an
own class. You are going to run the game through an engine.
The person can enter a room only once but he can choose to enter
the rooms in any order he wants to.
From LPTHW: Your runner will need to know about these rooms, 
so make a class that runs them and knows about them. There's 
plenty of ways to do this, but consider having each room return 
what room is next or setting a variable of what room is next.
Plot: Stealing intellectual abilitys, the manager is your father. 
They did this to create a highly intelligent person who could solver world problems.
That person is your sister. They needed to transfer it succesive.
"""
"""
* Map 
    - next_scene
    - opening_scene
* Engine
    - play
* Scene
    - Enter
    - Current scene
    - Help for that room
    * Death
    * White room
    * Central corridor
    * Room with people wired in + Memory fragment
    * Boss with notes that explains things + Memory fragment
    * Manager + Memory fragment
"""
from sys import exit
from random import randint

prompt = '--> '

class Scene(object): # Add things here for the subclasses
	
	the_scene = None
	enter_scene = Engine(the_scene).play()

class Engine(object): # Running the rooms
	
	def __init__(self, scene_map):
		self.scene_map = scene_map # Set this to the string name of the room
		self.final_scene = Final_room() # Set self.final_scene to the final_room class
		self.class_scene = Map(self.scene_map).next_room()

	def play(self):
		self.class_scene.enter()

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

		if choice is 'take':
			print("You pull the keys from her and she looks chocked and tries to grab them back")
			print("You push her away and barely manage to open your handcuffs but you somehow do it.")
			print("Now she comes charging at you with the needle and tries to stab you with it.")
			print("Are you going to (flee) by running out of the door or try to (disarm) her?.")
			choice = input(prompt)

		elif choice is 'inject':
			print("You feel a sting in your arm and fall asleep. You never woke up again...")
			the scene = 'death'
			enter_scene
		
		else:
			print("There is no command of that choice.")
			the_scene = 'white_room'
			enter_scene

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

	def __init__(self, the_scene):
		self.the_scene = the_scene

	def next_room(self):
		scenes = {
		'white_room': White_room(),
		'central_corridor': Central_corridor(),
		'wired_room': Wired_room(),
		'lab': Lab(),
		'doctors': Doctors(),
		'final_room': Final_room(),
		'death': Death()
		}

		return scenes.get(self.the_scene)


Engine('white_room').play()

# Figure out the return thing, make the engine work!