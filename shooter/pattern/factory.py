from abc import ABC, abstractmethod


class Factory(ABC):

	@abstractmethod
	def createEnemy(self, playground_size):
		pass

	@abstractmethod
	def createMissile(self, cannon):
		pass

class SimpleFactor(Factory):

	def createEnemy(self, playground_size):
		return SimpleEnemy(playground_size)

	def createMissile(self, cannon):
		pass

class SmartFactory(Factory):

	def createEnemy(self, playground_size):
		return SmartEnemy(playground_size)

	def createMissile(self, cannon):
		pass