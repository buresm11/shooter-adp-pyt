import pyglet
import os

class Drawable(pyglet.sprite.Sprite):

	def __init__(self, image, playground_size):
		super().__init__(image)
		self.playground_size = playground_size

	def get_rect(self):
		pass

	def move_freely(self, offset):
		self.x += offset.x
		self.y += offset.y

	def move(self, offset):

		accident = False

		if self.x + offset.x < 0:
			self.x = 0
			accident = True
		elif self.x + offset.x + self.width >= self.playground_size.x:
			self.x = self.playground_size.x - self.width
			accident = True
		else:
			self.x += offset.x

		if self.y + offset.y < 0:
			self.y = 0
			accident = True
		elif self.y + offset.y + self.height >= self.playground_size.y:
			self.y = self.playground_size.y - self.height
			accident = True
		else:
			self.y += offset.y

		return accident


class Cannon(Drawable):

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

		print(self.x)
		print(self.y)

class Enemy(Drawable):

	def __init__(self):
		pass

class Blast(Drawable):

	def __init__(self):
		pass

class Missile(Drawable):

	def __init__(self):
		pass
