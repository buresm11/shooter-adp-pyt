from abc import ABC, abstractmethod
from ..pattern.observer import Observable
import pyglet

from .objects import Cannon
import os

class Model(Observable):

	def __init__(self, size):
		super().__init__()
		self.size = size
		self.images = Images()
		self.cannon = Cannon(self.images.cannon_image(),size)

	def tick(self):
		self.notify_observers()

	def get_drawables(self):
		drawables = []
		drawables.append(self.cannon)	

		return drawables

	def fire(self):
		pass

	def move_cannon(self, offset):
		self.cannon.move(offset)


class Images():

	def cannon_image(self):
		cannon = pyglet.image.load(os.path.dirname(__file__) + '/../res/cannon.png')
		return cannon

	def enemy_image(self):
		enemy = pyglet.image.load(os.path.dirname(__file__) + '/../res/enemy.png')
		return enemy

	def missile_image(self):
		missile = pyglet.image.load(os.path.dirname(__file__) + '/../res/missile.png')
		return enemy

	def blast_image(self):
		blast = pyglet.image.load(os.path.dirname(__file__) + '/../res/blast.png')
		return blast

class Size():

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

class Vector():

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

