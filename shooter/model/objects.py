import pyglet
import os
import math
import random

from .data import CannonSituation, Direction, Vector, Rect
from ..pattern.state import OneMissileCannonState, TwoMissileCannonState

class Drawable(pyglet.sprite.Sprite):
	""" game object that can be drawn on window """

	def __init__(self, image, playground_size):
		super().__init__(image)

		self.image.anchor_x = self.width // 2
		self.image.anchor_y = self.height // 2

		self.playground_size = playground_size

	def get_rect(self):
		return Rect(Vector(self.x - self.width  // 2, self.y - self.height // 2),
			Vector(self.x + self.width  // 2, self.y + self.height // 2))

	def move_freely(self, offset):
		self.x += offset.x
		self.y += offset.y

	def move_bounded(self, offset):

		accident = False

		if self.x + offset.x - self.width // 2  < 0:
			self.x = self.width // 2
			accident = True
		elif self.x + offset.x + self.width // 2 > self.playground_size.x:
			self.x = self.playground_size.x - self.width // 2
			accident = True
		else:
			self.x += offset.x

		if self.y + offset.y - self.height // 2 < 0:
			self.y = self.height // 2
			accident = True
		elif self.y + offset.y + self.height // 2 > self.playground_size.y:
			self.y = self.playground_size.y - self.height // 2
			accident = True
		else:
			self.y += offset.y

		return accident

DEFAULT_MAX_FIRE_POWER = 25
DEFAULT_MIN_FIRE_POWER = 10

class Cannon(Drawable):
	""" game object cannon that shoot missiles  """
	
	def __init__(self, image, missile_image, playground_size, default_situation, factory, gravity):
		super().__init__(image, playground_size)

		self.angle = 0
		self.fire_power = DEFAULT_MIN_FIRE_POWER
		self.ignition_phase = False
		self.x = self.width // 2
		self.y = self.playground_size.y // 2
		self.factory = factory
		self.missile_image = missile_image
		self.gravity = gravity

		self.prepared_missiles = []
		self.situation = default_situation

		if self.situation == CannonSituation.ONE_MISSILE:
			self.state = OneMissileCannonState()
		elif self.situation == CannonSituation.TWO_MISSILE:
			self.state = TwoMissileCannonState()

	def move(self, offset):
		self.move_bounded(offset)
		self.state.move_missiles(self, self.playground_size)
 
	def rotate_cannon(self, rotation_offset):
		self.angle = math.atan2(math.sin(self.angle + rotation_offset),math.cos(self.angle + rotation_offset))
		self.rotation = math.degrees(self.angle)

		self.state.rotate_missiles(self)

	def ignition_fire(self):
		self.reset_fire_power()
		self.ignition_phase = True

		self.prepared_missiles.extend(self.state.create_missiles(self.missile_image, self.playground_size, self))

	def fire(self):
		return self.state.fire_missiles(self)

	def reset_fire_power(self):
		self.fire_power = DEFAULT_MIN_FIRE_POWER

	def add_fire_power(self):
		if self.fire_power < DEFAULT_MAX_FIRE_POWER:
			self.fire_power += 1

	def switch_mode(self):
		self.prepared_missiles.clear()

		if self.situation == CannonSituation.ONE_MISSILE:
			self.state = TwoMissileCannonState()
			self.situation = CannonSituation.TWO_MISSILE
		elif self.situation == CannonSituation.TWO_MISSILE:
			self.state = OneMissileCannonState()
			self.situation = CannonSituation.ONE_MISSILE

	def copy(self):
		copy = Cannon(self.image, self.missile_image, self.playground_size, self.situation, self.factory, self.gravity)
		copy.ignition_phase = False
		copy.angle = self.angle
		copy.rotation = math.degrees(copy.angle)
		copy.fire_power = self.fire_power
		copy.x = self.x
		copy.y = self.y

		return copy

	def accept(self, visitor):
		visitor.visit_cannon(self)

class Enemy(Drawable):
	""" game object enemy that randomly computes its position """

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

		lowx = self.width // 2
		lowy = self.height // 2

		highx = self.playground_size.x - self.width // 2
		highy = self.playground_size.y - self.height // 2

		self.x = random.randint(lowx, highx)
		self.y = random.randint(lowy, highy)

class SimpleEnemy(Enemy):
	""" game object simple enemy that never moves """

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

	def move(self):
		pass

	def copy(self):
		copy = SimpleEnemy(self.image,self.playground_size.copy())
		copy.x = self.x
		copy.y = self.y

		return copy

	def accept(self, visitor):
		visitor.visit_simple_enemy(self.copy())

class SmartEnemy(Enemy):
	""" game object smart enemy that moves randomly """

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

		self.set_random_direction()

	def move(self):

		accident = False

		if self.direction == Direction.EAST:
			accident = super().move_bounded(Vector(3,0))
		if self.direction == Direction.NORTH:
			accident = super().move_bounded(Vector(0,3))
		if self.direction == Direction.SOUTH:
			accident = super().move_bounded(Vector(0,-3))
		if self.direction == Direction.WEST:
			accident = super().move_bounded(Vector(-3,0))  

		if accident == True:
			self.set_random_direction()
		else:
			value = random.randint(0, 500)

			if value < 20:
				self.set_random_direction()

	def copy(self):
		copy = SmartEnemy(self.image,self.playground_size.copy())
		copy.x = self.x
		copy.y = self.y
			
		return copy

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


	def accept(self, visitor):
		visitor.visit_smart_enemy(self.copy())


class Missile(Drawable):
	""" game object for shooting enemies """

	def __init__(self, image, playground_size, location, angle, strategy):
		super().__init__(image, playground_size)

		self.x = location.x
		self.y = location.y

		self.angle = angle
		self.rotation = math.degrees(self.angle)

		self.strategy = strategy
		self.fired = False

		self.lastx = 0
		self.lasty = 0


	def move(self, enemies, blasts, blast_image):
		if self.fired:
			self.strategy.move(self)

		hits = 0 
		enemies_count = len(enemies)
		
		shot_down = [e for e in enemies if e.get_rect().intersect(self.get_rect())]
		enemies[:] = [e for e in enemies if not e.get_rect().intersect(self.get_rect())]

		for shot in shot_down:
			blasts.append(Blast(blast_image, self.playground_size, Vector(shot.x, shot.y)))

		return len(shot_down)

	def fire(self, fire_power, gravity, angle):
		self.fired_pos = Vector(self.x, self.y)
		self.fired = True
		self.fire_power = fire_power
		self.gravity = gravity
		self.angle = angle
		self.time = 0

	def accept(self, visitor):
		visitor.visit_missile(self)

class Blast(Drawable):
	""" game object that appears after enemy has been shot """

	def __init__(self, image, playground_size, location):
		super().__init__(image, playground_size)

		self.x = location.x
		self.y = location.y

		self.lifetime = 0

	def increase_lifetime(self):
		self.lifetime += 1

	def is_active(self):
		return self.lifetime < 20

	def accept(self, visitor):
		visitor.visit_blast(self)

		

