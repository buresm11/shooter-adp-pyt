from abc import ABC, abstractmethod


class Factory(ABC):

	@abstractmethod
	def createEnemy(self, playground_size):
		pass

	@abstractmethod
	def createMissile(self, cannon):
		pass