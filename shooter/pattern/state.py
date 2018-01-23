import math
from abc import ABC, abstractmethod

from ..model.data import Vector

DEFAULT_MISSILE_POS_DIFF = 20
DEFAULT_MISSILE_ROT_DIFF = 0.2

class OneMissileCannonState():
	""" keeps state of cannon when one missile is used. It is responsible for creating, moving, rotating and firing that one missile """

	def create_missiles(self, image, playground_size, cannon):
		missiles = []

		location = Vector(cannon.x, cannon.y)
		missiles.append(cannon.factory.create_missile(image, playground_size, location, cannon.angle))

		return missiles

	def move_missiles(self, cannon, playground_size):
		
		if len(cannon.prepared_missiles) == 1:
			cannon.prepared_missiles[0].x = cannon.x
			cannon.prepared_missiles[0].y = cannon.y

	def rotate_missiles(self, cannon):

		if len(cannon.prepared_missiles) == 1:
			cannon.prepared_missiles[0].rotation = cannon.rotation

	def fire_missiles(self, cannon):

		fired = list(cannon.prepared_missiles)
		cannon.prepared_missiles.clear()

		if len(fired) == 1:
			fired[0].fire(cannon.fire_power, cannon.gravity, cannon.angle)

		cannon.ignition_phase = False
		cannon.reset_fire_power()

		return fired

class TwoMissileCannonState():
	""" keeps state of cannon when two missile is used. It is responsible for creating, moving, rotating and firing those two missiles """

	def create_missiles(self, image, playground_size, cannon):
		missiles = []

		location = Vector(cannon.x, cannon.y - DEFAULT_MISSILE_POS_DIFF)
		location2 = Vector(cannon.x, cannon.y + DEFAULT_MISSILE_POS_DIFF)

		missiles.append(cannon.factory.create_missile(image, playground_size, location, cannon.angle + DEFAULT_MISSILE_ROT_DIFF))
		missiles.append(cannon.factory.create_missile(image, playground_size, location2, cannon.angle - DEFAULT_MISSILE_ROT_DIFF))	
		return missiles

	def move_missiles(self, cannon , playground_size):
		
		if len(cannon.prepared_missiles) == 2:
			cannon.prepared_missiles[0].x = cannon.x
			cannon.prepared_missiles[0].y = cannon.y - DEFAULT_MISSILE_POS_DIFF

			cannon.prepared_missiles[1].x = cannon.x
			cannon.prepared_missiles[1].y = cannon.y + DEFAULT_MISSILE_POS_DIFF

	def rotate_missiles(self, cannon):

		if len(cannon.prepared_missiles) == 2:
			cannon.prepared_missiles[0].rotation = math.degrees(cannon.angle + DEFAULT_MISSILE_ROT_DIFF)
			cannon.prepared_missiles[1].rotation =  math.degrees(cannon.angle - DEFAULT_MISSILE_ROT_DIFF)

	def fire_missiles(self, cannon):
		
		fired = list(cannon.prepared_missiles)
		cannon.prepared_missiles.clear()

		if len(fired) == 2:
			fired[0].fire(cannon.fire_power, cannon.gravity, cannon.angle + DEFAULT_MISSILE_ROT_DIFF)
			fired[1].fire(cannon.fire_power, cannon.gravity, cannon.angle - DEFAULT_MISSILE_ROT_DIFF)

		cannon.ignition_phase = False
		cannon.reset_fire_power()

		return fired

		
		