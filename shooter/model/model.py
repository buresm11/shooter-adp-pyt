from abc import ABC, abstractmethod
from ..pattern.observer import Observable
import pyglet

from .objects import Cannon
from .objects import SimpleEnemy
import os

class Model(Observable):

	def __init__(self, size):
		super().__init__()
		self.size = size
		self.images = Images()
		self.cannon = Cannon(self.images.cannon_image(),size)
		self.enemies = []
		self.prepared_missiles = []
		self.fired_missiles = []

		self.make_enemies()

	def tick(self):

		if self.cannon.ignition_phase == True:
			self.cannon.add_fire_power()

		self.notify_observers()

	def get_drawables(self):
		drawables = []
		drawables.append(self.cannon)
		drawables.extend(self.enemies)	

		return drawables

	def fire(self):
		self.cannon.fire()

	def move_cannon(self, offset):
		self.cannon.move(offset)

	def rotate_cannon(self, rotation_offset):
		self.cannon.rotate_cannon(rotation_offset)

	def make_enemies(self):
		for i in range(15):
			self.enemies.append(SimpleEnemy(self.images.enemy_image(), self.size))

	def order_to_fire(self):
		self.cannon.ignition_fire()

	def get_hud(self):
		hud = []

		hud.append("Mode:" )
		hud.append("Gravity:")
		hud.append("Firepower:" + str(self.cannon.fire_power))
		hud.append("Score:")

		return hud

class Images():

	def cannon_image(self):
		cannon = pyglet.image.load(os.path.dirname(__file__) + '/../res/cannon.png')
		return cannon

	def enemy_image(self):
		enemy = pyglet.image.load(os.path.dirname(__file__) + '/../res/enemy1.png')
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

