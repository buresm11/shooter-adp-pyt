from .model.model import Model
from .model.model import Size
from .controller.controller import Controller
from .view.view import View

import pyglet

def main():
	
	size = Size(800,600)

	model = Model(size)

	window = pyglet.window.Window(size.x, size.y)
	view = View(window, model)

	controller = Controller(pyglet.app, pyglet.clock, view, model)
	controller.run()





