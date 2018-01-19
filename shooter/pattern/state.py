from abc import ABC, abstractmethod

from ..model.data import Vector

class State(ABC):

	@abstractmethod
	def createMissiles(self, cannon, factory, playground_size):
		pass

	@abstractmethod
	def fireMissiles(self, cannon):
		pass

	@abstractmethod
	def moveMissiles(self, cannon):
		pass


class OneMissileCannonState(CannonState):

	def createMissiles(self, cannon, factory, playground_size):
		missiles = []

		location = Vector(cannon.x, playground_size // 2)
		missiles.append(factory.createMissiles(location, playground_size))

		return missiles

	def fireMissiles(self, cannon):
		pass

	def moveMissiles(self, cannon):
		pass

class TwoMissileCannonState(CannonState):

	def createMissiles(self, cannon, factory, playground_size):
		missiles = []

		location = Vector(cannon.x, playground_size.y // 2 + 20)
		location2 = Vector(cannon.x, playground_size.y // 2 - 20)

		missiles.append(factory.createMissiles(location, playground_size))
		missiles.append(factory.createMissiles(location2, playground_size))

		return missiles

	def fireMissiles(self, cannon):
		pass

	def moveMissiles(self, cannon):
		pass