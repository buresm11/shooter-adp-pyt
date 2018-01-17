from .model.model import Model
from .model.model import Size
from .controller.controller import Controller
from .view.view import View

import pyglet

def main():
	
	playground_size = Size(800,600)

	model = Model(playground_size)

	window = pyglet.window.Window(playground_size.x, playground_size.y)
	view = View(window, model)
	model.add_observer(view)

	controller = Controller(pyglet.app, pyglet.clock, view, model)
	controller.run()





