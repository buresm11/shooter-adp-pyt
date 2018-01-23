import os
import pyglet
import contextlib
from pyglet.window import key

from ..model.data import Vector, MoveDirection, RotateDirection
from ..pattern.memento import Memento, ModelCareTaker
from ..pattern.visitor import Visitor

class Controller():
	""" Handles all user input """

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
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, MoveDirection.UP))
		elif symbol == key.DOWN:
			self.keys_pressed['down'] = True
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, MoveDirection.DOWN))
		elif symbol == key.LEFT:
			self.keys_pressed['left'] = True
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, RotateDirection.LEFT))
		elif symbol == key.RIGHT:
			self.keys_pressed['right'] = True
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, RotateDirection.RIGHT))
		elif symbol == key.A:
			self.commands.append(ChangeGravityCommand(self.model_care_taker, self.model, MoveDirection.DOWN))
		elif symbol == key.S:
			self.commands.append(ChangeGravityCommand(self.model_care_taker, self.model, MoveDirection.UP))
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
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, MoveDirection.UP))

		if self.keys_pressed['down'] == True:
			self.commands.append(MoveCannonCommand(self.model_care_taker, self.model, MoveDirection.DOWN))

		if self.keys_pressed['left'] == True:
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, RotateDirection.LEFT))

		if self.keys_pressed['right'] == True:
			self.commands.append(RotateCannonCommand(self.model_care_taker, self.model, RotateDirection.RIGHT))

		for command in self.commands:
			command.execute()

		self.commands.clear()
		self.model.tick()

class FireCommand():
	""" command pattern, executes command that fires missile """

	def __init__(self, model):
		self.model = model

	def execute(self):
		self.model.fire()

class OrderToFireCommand():
	""" command pattern, executes command that orders cannon to fire """

	def __init__(self, model):
		self.model = model

	def execute(self):
		self.model.order_to_fire()

class MoveCannonCommand():
	""" command pattern, executes command that moves cannon """

	def __init__(self, model_care_taker, model, move_direction):
		self.model_care_taker = model_care_taker
		self.model = model
		self.move_direction = move_direction

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.move_cannon(self.move_direction)

class RotateCannonCommand():
	""" command pattern, executes command that rotates cannon """

	def __init__(self, model_care_taker, model, rotate_direction):
		self.model_care_taker = model_care_taker
		self.model = model;
		self.rotate_direction = rotate_direction

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.rotate_cannon(self.rotate_direction)

class ChangeGravityCommand():
	""" command pattern, executes command that changes gravity """

	def __init__(self, model_care_taker, model, gravity_direction):
		self.model_care_taker = model_care_taker
		self.model = model;
		self.gravity_direction = gravity_direction

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.change_gravity(self.gravity_direction)

class GoBackCommand():
	""" command pattern, executes command that goes back one step using memento pattern """

	def __init__(self,model_care_taker, model):
		self.model_care_taker = model_care_taker
		self.model = model;

	def execute(self):
		memento = self.model_care_taker.get_last();
		if memento is not None:
			self.model.get_from_memento(memento);

class SwitchModeCommand():
	""" command pattern, executes command that switches between simple and smart environment """

	def __init__(self, model_care_taker, model):
		self.model_care_taker = model_care_taker
		self.model = model;

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.switch_mode()

class SwitchCannonModeCommand():
	""" command pattern, executes command that switches whether cannon uses one or two missile """

	def __init__(self, model_care_taker, model):
		self.model_care_taker = model_care_taker
		self.model = model;

	def execute(self):
		self.model_care_taker.add(self.model.save_to_memento())
		self.model.switch_cannon_mode()

class LoadCommand():
	""" command pattern, executes command that loads game from file"""

	def __init__(self, model):
		self.model = model

	def execute(self):
		self.model.load_from_file()

class SaveCommand():
	""" command pattern, executes command that save game to file """

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
	""" command pattern, executes command that removes save file """

	def execute(self):
		path = os.path.dirname(__file__) + '/../res/save'
		with contextlib.suppress(FileNotFoundError):
			os.remove(path)