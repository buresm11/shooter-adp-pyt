from ..pattern.observer import Observer
from ..model.model import Model

import pyglet

class View(pyglet.window.Window,Observer):

	def __init__(self, playground_size):
		super().__init__(playground_size.x,playground_size.y);

	def update(self, x):
		self.clear()
		
		if isinstance(x, Model):
			drawables = x.get_drawables()
			for drawable in drawables:
				drawable.draw()
			


			