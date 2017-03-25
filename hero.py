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

champion = Hero('Karen')