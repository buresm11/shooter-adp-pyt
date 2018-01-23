from ..model.objects import SimpleEnemy, SmartEnemy, Missile
from ..pattern.strategy import SimpleStrategy, SmartStrategy

class SimpleFactory():
	""" creates simple objects such as simple enemies that do not move and simple missiles that do not use gravity """

	def create_enemy(self, image, playground_size):
		return SimpleEnemy(image, playground_size)

	def create_missile(self, image, playground_size, location, rotation):
		return Missile(image, playground_size, location, rotation, SimpleStrategy())

class SmartFactory():
	""" creates simple objects such as smart enemies that move and smart missiles which use gravity """

	def create_enemy(self, image, playground_size):
		return SmartEnemy(image, playground_size)

	def create_missile(self, image, playground_size, location, rotation):
		return Missile(image, playground_size, location, rotation, SmartStrategy())