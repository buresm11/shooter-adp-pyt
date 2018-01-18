import pyglet
import os

class Drawable(pyglet.sprite.Sprite):

	def __init__(self, image, playground_size):
		super().__init__(image)
		self.playground_size = playground_size

	def get_rect(self):
		pass

	def move_freely(self):
		pass

	def move_bounded(self):
		return False


class Cannon(Drawable):

	def __init__(self, image, playground_size):
		super().__init__(image, playground_size)

class Enemy(Drawable):

	def __init__(self):
		pass

class Blast(Drawable):

	def __init__(self):
		pass

class Missile(Drawable):

	def __init__(self):
		pass
