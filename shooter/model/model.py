from abc import ABC, abstractmethod

from ..pattern.observer import Observable


class Model(Observable):

	def __init__(self, size):
		super().__init__()
		self.size = size

	def tick(self):
		self.notify_observers()



class Drawable(ABC):

	def __init__(self, playground_size, location, size):
		self.playground_size = playground_size
		self.location = location
		self.size = size

	def get_rect(self):
		pass

	def move_freely(self):
		pass

	def move_bounded(self):
		return False
		

class Size():

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

class Location():

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

