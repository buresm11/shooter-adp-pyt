import math

from abc import ABC, abstractmethod

from ..model.data import Vector

class CannonState(ABC):

	@abstractmethod
	def create_missiles(self, image, playground_size, cannon):
		pass

	@abstractmethod
	def move_missiles(self, cannon , playground_size):
		pass

	@abstractmethod
	def rotate_missiles(self, cannon):
		pass


class OneMissileCannonState(CannonState):

	def create_missiles(self, image, playground_size, cannon):
		missiles = []

		location = Vector(cannon.x, cannon.y)
		missiles.append(cannon.factory.create_missile(image, playground_size, location, cannon.rotation))

		return missiles

	def move_missiles(self, cannon, playground_size):
		
		if len(cannon.prepared_missiles) == 1:
			cannon.prepared_missiles[0].x = cannon.x
			cannon.prepared_missiles[0].y = cannon.y

	def rotate_missiles(self, cannon):

		if len(cannon.prepared_missiles) == 1:
			cannon.prepared_missiles[0].rotation = cannon.rotation

	def fire_missiles(self, cannon):
		pass

class TwoMissileCannonState(CannonState):

	def create_missiles(self, image, playground_size, cannon):
		missiles = []

		location = Vector(cannon.x, cannon.y - 20)
		location2 = Vector(cannon.x, cannon.y + 20)

		missiles.append(cannon.factory.create_missile(image, playground_size, location, cannon.rotation))
		missiles.append(cannon.factory.create_missile(image, playground_size, location2, cannon.rotation))	
		return missiles

	def move_missiles(self, cannon , playground_size):
		
		if len(cannon.prepared_missiles) == 2:
			cannon.prepared_missiles[0].x = cannon.x
			cannon.prepared_missiles[0].y = cannon.y - 20

			cannon.prepared_missiles[1].x = cannon.x
			cannon.prepared_missiles[1].y = cannon.y + 20

	def rotate_missiles(self, cannon):

		if len(cannon.prepared_missiles) == 2:
			cannon.prepared_missiles[0].rotation = cannon.rotation
			cannon.prepared_missiles[1].rotation = cannon.rotation

	def fire_missiles(self, cannon):
		pass
		