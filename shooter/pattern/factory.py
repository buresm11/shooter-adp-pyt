from abc import ABC, abstractmethod

from ..model.objects import SimpleEnemy
from ..model.objects import SmartEnemy
from ..model.objects import Missile

from ..pattern.strategy import SimpleStrategy
from ..pattern.strategy import SmartStrategy


class Factory(ABC):

	@abstractmethod
	def create_enemy(self, image, playground_size):
		pass

	@abstractmethod
	def create_missile(self, image, playground_size, location, rotation):
		pass

class SimpleFactory(Factory):

	def create_enemy(self, image, playground_size):
		return SimpleEnemy(image, playground_size)

	def create_missile(self, image, playground_size, location, rotation):
		return Missile(image, playground_size, location, rotation, SimpleStrategy())

class SmartFactory(Factory):

	def create_enemy(self, image, playground_size):
		return SmartEnemy(image, playground_size)

	def create_missile(self, image, playground_size, location, rotation):
		return Missile(image, playground_size, location, rotation, SmartStrategy())