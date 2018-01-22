
class Memento:

	def __init__(self, cannon, enemies, factory, gravity, situation, score):
		self.cannon = cannon
		self.enemies = enemies
		self.factory = factory
		self.gravity = gravity
		self.situation = situation
		self.score = score

class ModelCareTaker:

	def __init__(self):
		self.mementos = []

	def add(self, Memento):
		self.mementos.append(Memento)

	def get_last(self):
		if len(self.mementos) > 0:
			return self.mementos.pop()
		else:
			return None