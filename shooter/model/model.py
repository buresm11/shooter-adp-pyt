import pyglet
import os
from abc import ABC, abstractmethod
from copy import deepcopy
import pickle

from ..pattern.observer import Observable
from ..pattern.factory import SmartFactory
from ..pattern.factory import SimpleFactory
from ..pattern.memento import Memento
from .objects import Cannon
from .objects import SimpleEnemy
from .objects import SmartEnemy
from .data import Situation
from .data import CannonSituation
from .data import Vector
from .data import Rect

DEFAULT_SITUATION = Situation.SIMPLE
DEFAULT_CANONN_SITUATION = CannonSituation.TWO_MISSILE
DEFAULT_GRAVITY = 10

class Model(Observable):

	def __init__(self, size):
		super().__init__()
		self.size = size
		self.images = Images()
		self.enemies = []
		self.missiles = []
		self.blasts = []
		self.score = 0
		self.gravity = DEFAULT_GRAVITY
		self.situation = DEFAULT_SITUATION
		self.set_situation()

		self.cannon = Cannon(self.images.cannon_image(), self.images.missile_image(), size, DEFAULT_CANONN_SITUATION, self.factory, self.gravity)
		self.make_enemies()

	def set_situation(self):
		if self.situation == Situation.SMART:
			self.factory = SmartFactory()
		elif self.situation == Situation.SIMPLE:
			self.factory = SimpleFactory()

	def tick(self):

		for enemy in self.enemies:
			enemy.move()

		for missile in self.missiles:
			self.score += missile.move(self.enemies, self.blasts, self.images.blast_image())

		for blast in self.blasts:
			blast.increase_lifetime()

		if self.cannon.ignition_phase == True:
			self.cannon.add_fire_power()

		self.remove_non_active_blasts()
		self.remove_out_of_bound_missiles()

		if len(self.enemies) == 0:
			self.make_enemies()

		self.notify_observers()

	def get_drawables(self):
		drawables = []
		drawables.append(self.cannon)
		drawables.extend(self.enemies)	
		drawables.extend(self.cannon.prepared_missiles)
		drawables.extend(self.missiles)
		drawables.extend(self.blasts)

		return drawables

	def fire(self):
		self.missiles.extend(self.cannon.fire())

	def move_cannon(self, offset):
		self.cannon.move(offset)

	def rotate_cannon(self, rotation_offset):
		self.cannon.rotate_cannon(rotation_offset)

	def make_enemies(self):
		for i in range(15):
			self.enemies.append(self.factory.create_enemy(self.images.enemy_image(), self.size))

	def order_to_fire(self):
		self.cannon.ignition_fire()

	def remove_out_of_bound_missiles(self):
		self.missiles = [m for m in self.missiles if m.get_rect().intersect(Rect(Vector(0,0), Vector(self.size.x, self.size.y)))]

	def remove_non_active_blasts(self):
		self.blasts = [b for b in self.blasts if b.is_active()]
		
	def change_gravity(self, gravity_offset):
		if self.gravity + gravity_offset > 0 and self.gravity + gravity_offset < 20:
			self.gravity += gravity_offset
			self.cannon.gravity = self.gravity

	def set_situation(self):
		if self.situation == Situation.SMART:
			self.factory = SmartFactory()
		elif self.situation == Situation.SIMPLE:
			self.factory = SimpleFactory()

	def switch_mode(self):

		if self.situation == Situation.SMART:
			self.factory = SimpleFactory()
			self.situation = Situation.SIMPLE
		elif self.situation == Situation.SIMPLE:
			self.factory = SmartFactory()
			self.situation = Situation.SMART

		self.cannon.factory = self.factory

		enemies_size = len(self.enemies)
		self.enemies.clear()

		for i in range(enemies_size):
			self.enemies.append(self.factory.create_enemy(self.images.enemy_image(), self.size))

	def switch_cannon_mode(self):
		self.cannon.switch_mode()

	def get_hud(self):
		hud = []

		s = 'Mode: '
		if self.situation == Situation.SIMPLE:
			s += 'simple'
		elif self.situation == Situation.SMART:
			s += 'smart'

		if self.cannon.situation == CannonSituation.ONE_MISSILE:
			s += ' | one missile'
		elif self.cannon.situation == CannonSituation.TWO_MISSILE:
			s += ' | two missile'

		hud.append(s)
		hud.append('Gravity: ' + str(self.gravity))
		hud.append('Firepower: ' + str(self.cannon.fire_power))
		hud.append('Score: ' + str(self.score))

		return hud

	def save_to_memento(self):

		enemies_copy = []

		for e in self.enemies:
			enemies_copy.append(e.copy())

		return Memento(self.cannon.copy(),enemies_copy, self.factory, self.gravity, self.situation, self.score)

	def get_from_memento(self, memento):
		self.cannon = memento.cannon
		self.enemies = memento.enemies
		self.factory = memento.factory
		self.gravity = memento.gravity
		self.situation = memento.situation
		self.score = memento.score

		self.missiles.clear()
		self.blasts.clear()

		self.notify_observers()

	def load_from_file(self):
		print("load")
		data = self.get_data_from_file()

		self.blasts.clear()
		self.missiles.clear()

		self.gravity = data['gravity']
		self.score = data['score']
		self.situation = data['situation']
		self.set_situation()

		cannon_situation = data['cannon_situation']
		self.cannon = Cannon(self.images.cannon_image(), self.images.missile_image(), self.size, cannon_situation, self.factory, self.gravity)

		enemies = data['enemies']
		self.enemies.clear()

		for e in enemies:
			enemy = self.factory.create_enemy(self.images.enemy_image(), self.size)
			enemy.x = e[0]
			enemy.y = e[1]
			self.enemies.append(enemy)

		self.notify_observers()
	
	def get_data_from_file(self):

		path = os.path.dirname(__file__) + '/../res/save'
		with open(path, 'rb') as f:
			return pickle.load(f)

		print("loaded")

	def accept(self, visitor):
		visitor.visit_model(self)

class Images():

	def cannon_image(self):
		cannon = pyglet.image.load(os.path.dirname(__file__) + '/../res/cannon.png')
		return cannon

	def enemy_image(self):
		enemy = pyglet.image.load(os.path.dirname(__file__) + '/../res/enemy1.png')
		return enemy

	def missile_image(self):
		missile = pyglet.image.load(os.path.dirname(__file__) + '/../res/missile.png')
		return missile

	def blast_image(self):
		blast = pyglet.image.load(os.path.dirname(__file__) + '/../res/blast.png')
		return blast

