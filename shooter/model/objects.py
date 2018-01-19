import pyglet
import os
import math
import random

from ..pattern.factory import Factory
from .data import CannonSituation
from .data import Direction
from .data import Vector


class Drawable(pyglet.sprite.Sprite):

	def __init__(self, image, playground_size):
		super().__init__(image)

		self.image.anchor_x = self.width / 2
		self.image.anchor_y = self.height / 2

		self.playground_size = playground_size

	def get_rect(self):
		pass

	def move_freely(self, offset):
		self.x += offset.x
		self.y += offset.y

	def move(self, offset):

		accident = False

		if self.x + offset.x - self.width / 2  < 0:
			self.x = self.width / 2
			accident = True
		elif self.x + offset.x + self.width / 2 > self.playground_size.x:
			self.x = self.playground_size.x - self.width / 2
			accident = True
		else:
			self.x += offset.x

		if self.y + offset.y - self.height / 2 < 0:
			self.y = self.height / 2
			accident = True
		elif self.y + offset.y + self.height / 2 > self.playground_size.y:
			self.y = self.playground_size.y - self.height / 2
			accident = True
		else:
			self.y += offset.y

		return accident

class Cannon(Drawable):

	max_fire_power = 100
	min_fire_power = 20
	default_cannon_situation = CannonSituation.TWO_MISSILE

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

		self.angle = 0
		self.fire_power = Cannon.min_fire_power
		self.ignition_phase = False
		self.x = self.width / 2
		self.y = self.playground_size.y / 2 - self.height / 2

		self.prepared_missiles = []
		self.situation = CannonSituation.ONE_MISSILE
 
	def rotate_cannon(self, rotation_offset):
		self.angle = math.atan2(math.sin(self.angle + rotation_offset),math.cos(self.angle + rotation_offset))
		self.rotation = math.degrees(self.angle)

	def ignition_fire(self):
		self.reset_fire_power()
		self.ignition_phase = True

	def fire(self):
		self.ignition_phase = False

	def reset_fire_power(self):
		self.fire_power = Cannon.min_fire_power

	def add_fire_power(self):
		if self.fire_power < Cannon.max_fire_power:
			self.fire_power += 1

class Enemy(Drawable):

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

		lowx = int(self.width / 2)
		lowy = int(self.height / 2)

		highx = int(self.playground_size.x - self.width / 2)
		highy = int(self.playground_size.y - self.height / 2)

		self.x = random.randint(lowx, highx)
		self.y = random.randint(lowy, highy)

class SimpleEnemy(Enemy):

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

class SmartEnemy(Enemy):

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

		self.set_random_direction()

	def move(self):

		accident = False

		if self.direction == Direction.EAST:
			accident = super().move(Vector(3,0))
		if self.direction == Direction.NORTH:
			accident = super().move(Vector(0,3))
		if self.direction == Direction.SOUTH:
			accident = super().move(Vector(0,-3))
		if self.direction == Direction.WEST:
			accident = super().move(Vector(-3,0))  

		if accident == True:
			self.set_random_direction()
		else:
			value = random.randint(0, 500)

			if value < 20:
				self.set_random_direction()
		

	def set_random_direction(self):
		value = random.randint(0, 500)

		if value < 125:
			self.direction = Direction.EAST
		elif value < 250:
			self.direction = Direction.NORTH
		elif value < 375:
			self.direction = Direction.SOUTH
		else:
			self.direction = Direction.WEST


class Missile(Drawable):

	def __init__(self, image, playground_size, location):
		super().__init__(image, playground_size)

		self.x = location.x
		self.y = location.y

class Blast(Drawable):

	def __init__(self):
		pass

