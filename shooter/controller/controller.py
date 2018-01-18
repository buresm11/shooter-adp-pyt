import pyglet
from pyglet.window import key

from ..model.model import Vector

from abc import ABC, abstractmethod

class Controller():

	def __init__(self, view, model):
		self.view = view
		self.model = model
		self.keys_pressed = {}
		self.commands = []

		self.view.push_handlers(
			on_key_press=self.key_pressed,
			on_key_release=self.key_released
		)

		self.space_pressed = False

	def key_pressed(self, symbol, modifiers):
		if symbol == key.SPACE:
			self.keys_pressed['space'] = True
		elif symbol == key.UP:
			self.keys_pressed['up'] = True
			self.commands.append(MoveCannonCommand(self.model, Vector(0,5)))
		elif symbol == key.DOWN:
			self.keys_pressed['down'] = True
			self.commands.append(MoveCannonCommand(self.model, Vector(0,-5)))
		elif symbol == key.LEFT:
			self.keys_pressed['left'] = True
		elif symbol == key.RIGHT:
			self.keys_pressed['right'] = True
		elif symbol == key.A:
			pass 		

	def key_released(self, symbol, modifiers):
		if symbol == key.SPACE:
			self.keys_pressed['space'] = False
		elif symbol == key.UP:
			self.keys_pressed['up'] = False
		elif symbol == key.DOWN:
			self.keys_pressed['down'] = False
		elif symbol == key.LEFT:
			self.keys_pressed['left'] = False
		elif symbol == key.RIGHT:
			self.keys_pressed['right'] = False

	def run(self):
		pyglet.clock.schedule_interval(self.tick, 1/30)
		pyglet.app.run()

	def tick(self, t):

		if 'up' in self.keys_pressed:
			if self.keys_pressed['up'] == True:
				self.commands.append(MoveCannonCommand(self.model, Vector(0,5)))
				
		if 'down' in self.keys_pressed:
			if self.keys_pressed['down'] == True:
				self.commands.append(MoveCannonCommand(self.model, Vector(0,-5)))

		for command in self.commands:
			command.execute()

		self.commands.clear()

		self.model.tick()


class Command(ABC):

	@abstractmethod
	def execute():
		pass

class FireCommand():

	def __init__(self, model):
		self.model = model

	def execute():
		self.model.fire()

class MoveCannonCommand():

	def __init__(self, model, offset):
		self.model = model
		self.offset = offset

	def execute(self):
		self.model.move_cannon(self.offset)


