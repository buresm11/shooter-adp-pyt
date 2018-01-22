
class Memento:

	def __init__(self, cannon, enemies, factory, gravity, situation):
		print("dsfdf")
		self.cannon = cannon
		self.enemies = enemies
		self.factory = factory
		self.gravity = gravity
		self.situation = situation

class ModelCareTaker:

	def __init__(self):
		self.mementos = []

	def add(self, Memento):
		self.mementos.append(Memento)

	def get_last(self):
		return mementos.pop()