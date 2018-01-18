import pyglet
from pyglet.window import key

class Controller():

	def __init__(self, view, model):
		self.view = view
		self.model = model

		self.view.push_handlers(
			on_key_press=self.key_pressed
		)

		self.space_pressed = False

	def key_pressed(self, symbol, modifiers):
		if symbol == key.SPACE:
			print('space')
		elif symbol == key.UP:
			pass
		elif symbol == key.DOWN:
			pass
		elif symbol == key.LEFT:
			pass
		elif symbol == key.RIGHT:
			pass
		elif symbol == key.A:
			pass
		elif symbol == key.S:
			pass
		elif symbol == key.U:
			pass
		elif symbol == key.Q:
			pass
		elif symbol == key.W:
			pass

	def run(self):
		pyglet.clock.schedule_interval(self.tick, 1/30)
		pyglet.app.run()

	def tick(self, t):
		self.model.tick()

