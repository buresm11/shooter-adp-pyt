import pyglet
import os
from abc import ABC, abstractmethod

from ..pattern.observer import Observable
from ..pattern.factory import SmartFactory
from ..pattern.factory import SimpleFactory
from .objects import Cannon
from .objects import SimpleEnemy
from .objects import SmartEnemy
from .data import Situation
from .data import CannonSituation

DEFAULT_SITUATION = Situation.SIMPLE
DEFAULT_CANONN_SITUATION = CannonSituation.TWO_MISSILE

class Model(Observable):

	def __init__(self, size):
		super().__init__()
		self.size = size
		self.images = Images()
		self.cannon = Cannon(self.images.cannon_image(),size)
		self.enemies = []
		self.missiles = []
		self.score = 0
		self.gravity = 0
		self.situation = DEFAULT_SITUATION

		if self.situation == Situation.SMART:
			self.factory = SmartFactory()
		elif self.situation == Situation.SIMPLE:
			self.factory = SimpleFactory()

		self.make_enemies()

	def tick(self):

		for enemy in self.enemies:
			enemy.move()

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
			self.enemies.append(self.factory.createEnemy(self.images.enemy_image(), self.size))

	def order_to_fire(self):
		self.cannon.ignition_fire()

	def change_gravity(self, gravity_offset):
		if self.gravity + gravity_offset > 0 and self.gravity + gravity_offset < 20:
			self.gravity += gravity_offset

	def go_back(self):
		pass

	def switch_mode(self):
		pass

	def switch_cannon_mode(self):
		pass

	def get_hud(self):
		hud = []

		s = 'Mode: '
		if self.situation == Situation.SIMPLE:
			s += 'simple'
		elif self.situation == Situation.SMART:
			s += 'smart'

		hud.append(s)
		hud.append('Gravity: ' + str(self.gravity))
		hud.append('Firepower: ' + str(self.cannon.fire_power))
		hud.append('Score: ' + str(self.score))

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

