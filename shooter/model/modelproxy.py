from .model import Model
from ..pattern.observer import Observable

class ModelProxy(Observable):
	""" proxy pattern for model """

	def __init__(self, size):
		super().__init__()

		self.model = Model(size)

	def add_observer(self, observer):
		self.model.add_observer(observer)

	def remove_observer(self, observer):
		self.model.remove_observer(observer)

	def notify_observers(self):
		self.model.notify_observers(observer)

	def tick(self):
		self.model.tick()

	def get_drawables(self):
		return self.model.get_drawables()

	def fire(self):
		self.model.fire()

	def move_cannon(self, move_direction):
		self.model.move_cannon(move_direction)

	def rotate_cannon(self, rotate_direction):
		self.model.rotate_cannon(rotate_direction)

	def make_enemies(self):
		self.model.make_enemies()

	def order_to_fire(self):
		self.model.order_to_fire()

	def remove_out_of_bound_missiles(self):
		self.model.remove_out_of_bound_missiles()

	def remove_non_active_blasts(self):
		self.model.remove_non_active_blasts()
		
	def change_gravity(self, gravity_direction):
		self.model.change_gravity(gravity_direction)

	def switch_mode(self):
		self.model.switch_mode()

	def switch_cannon_mode(self):
		self.model.switch_cannon_mode()

	def get_hud(self):
		self.model.get_hud()

	def save_to_memento(self):
		return self.model.save_to_memento()
		
	def get_from_memento(self, memento):
		self.model.get_from_memento(memento)

	def load_from_file(self):
		self.model.load_from_file()

	def accept(self, visitor):
		self.model.accept(visitor)
