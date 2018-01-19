import pyglet

from .model.model import Model
from .model.data import Size
from .controller.controller import Controller
from .view.view import View

def main():
	
	playground_size = Size(800,600)

	model = Model(playground_size)

	view = View(playground_size)
	model.add_observer(view)

	controller = Controller(view, model)
	controller.run()