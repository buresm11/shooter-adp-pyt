import pyglet
import os
import math
import random

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

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

		self.angle = 0
		self.x = self.width / 2
		self.y = self.playground_size.y / 2 - self.height / 2
 
	def rotate_cannon(self, rotation_offset):
		self.angle = math.atan2(math.sin(self.angle + rotation_offset),math.cos(self.angle + rotation_offset))
		self.rotation = math.degrees(self.angle)

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

class Blast(Drawable):

	def __init__(self):
		pass

class Missile(Drawable):

	def __init__(self):
		pass
