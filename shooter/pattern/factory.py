from abc import ABC, abstractmethod

from ..model.objects import SimpleEnemy
from ..model.objects import SmartEnemy

class Factory(ABC):

	@abstractmethod
	def createEnemy(self, image, playground_size):
		pass

	@abstractmethod
	def createMissile(self, cannon):
		pass

class SimpleFactory(Factory):

	def createEnemy(self, image, playground_size):
		return SimpleEnemy(image, playground_size)

	def createMissile(self, cannon):
		pass

class SmartFactory(Factory):

	def createEnemy(self, image, playground_size):
		return SmartEnemy(image, playground_size)

	def createMissile(self, cannon):
		pass