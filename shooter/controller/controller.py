import pyglet
from pyglet.window import key
from abc import ABC, abstractmethod
import contextlib
import os

from ..model.data import Vector
from ..pattern.memento import Memento
from ..pattern.memento import ModelCareTaker
from ..pattern.visitor import Visitor

class Controller():

	def __init__(self, view, model):
		self.view = view
		self.model = model
		self.keys_pressed = {}
		self.commands = []
		self.model_care_taker = ModelCareTaker()

		self.keys_pressed['space'] = False
		self.keys_pressed['up'] = False
		self.keys_pressed['down'] = False
		self.keys_pressed['left'] = False
		self.keys_pressed['right'] = False

		self.view.push_handlers(
			on_key_press=self.key_pressed,
			on_key_release=self.key_released
		)

	def key_pressed(self, symbol, modifiers):
		if symbol == key.SPACE:
			if self.keys_pressed['space'] == False:
				self.commands.append(OrderToFireCommand(self.model))
			self.keys_pressed['space'] = True
		elif symbol == key.UP:
			self.keys_pressed['up'] = True
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, Vector(0,5)))
		elif symbol == key.DOWN:
			self.keys_pressed['down'] = True
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, Vector(0,-5)))
		elif symbol == key.LEFT:
			self.keys_pressed['left'] = True
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, -0.1))
		elif symbol == key.RIGHT:
			self.keys_pressed['right'] = True
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, 0.1))
		elif symbol == key.A:
			self.commands.append(ChangeGravityCommand(self.model_care_taker, self.model,-1))
		elif symbol == key.S:
			self.commands.append(ChangeGravityCommand(self.model_care_taker, self.model,1))
		elif symbol == key.U:
			self.commands.append(GoBackCommand(self.model_care_taker, self.model))
		elif symbol == key.Q:
			self.commands.append(SwitchModeCommand(self.model_care_taker, self.model))
		elif symbol == key.W:
			self.commands.append(SwitchCannonModeCommand(self.model_care_taker, self.model))
		elif symbol == key.R:
			self.commands.append(ResetCommand())
		elif symbol == key.E:
			self.commands.append(LoadCommand(self.model))
		elif symbol == key.T:
			self.commands.append(SaveCommand(self.model))

	def key_released(self, symbol, modifiers):
		if symbol == key.SPACE:
			self.commands.append(FireCommand(self.model))
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

		if self.keys_pressed['up'] == True:
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, Vector(0,5)))

		if self.keys_pressed['down'] == True:
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, Vector(0,-5)))

		if self.keys_pressed['left'] == True:
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, -0.1))

		if self.keys_pressed['right'] == True:
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, 0.1))

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

	def execute(self):
		self.model.fire()

class OrderToFireCommand():

	def __init__(self, model):
		self.model = model

	def execute(self):
		self.model.order_to_fire()

class MoveCannonCommand():

	def __init__(self, model_care_taker, model, offset):
		self.model_care_taker = model_care_taker
		self.model = model
		self.offset = offset

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.move_cannon(self.offset)

class RotateCannonCommand():

	def __init__(self, model_care_taker, model, rotation_offset):
		self.model_care_taker = model_care_taker
		self.model = model;
		self.rotation_offset = rotation_offset

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.rotate_cannon(self.rotation_offset)

class ChangeGravityCommand():

	def __init__(self, model_care_taker, model, gravity_offset):
		self.model_care_taker = model_care_taker
		self.model = model;
		self.gravity_offset = gravity_offset

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.change_gravity(self.gravity_offset)

class GoBackCommand():

	def __init__(self,model_care_taker, model):
		self.model_care_taker = model_care_taker
		self.model = model;

	def execute(self):
		memento = self.model_care_taker.get_last();
		if memento is not None:
			self.model.get_from_memento(memento);

class SwitchModeCommand():

	def __init__(self, model_care_taker, model):
		self.model_care_taker = model_care_taker
		self.model = model;

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.switch_mode()

class SwitchCannonModeCommand():

	def __init__(self, model_care_taker, model):
		self.model_care_taker = model_care_taker
		self.model = model;

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.switch_cannon_mode()

class LoadCommand():

	def __init__(self, model):
		self.model = model

	def execute(self):
		self.model.load_from_file()

class SaveCommand():

	def __init__(self, model):
		self.model = model
		
	def execute(self):

		visitor = Visitor()

		drawables = self.model.get_drawables()

		for d in drawables:
			d.accept(visitor)

		self.model.accept(visitor)
		visitor.save()

class ResetCommand():

	def execute(self):
		path = os.path.dirname(__file__) + '/../res/save'
		with contextlib.suppress(FileNotFoundError):
			os.remove(path)