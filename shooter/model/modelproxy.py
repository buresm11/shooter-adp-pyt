from .model import Model
from ..pattern.observer import Observable

class ModelProxy(Observable):

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

	def move_cannon(self, offset):
		self.model.move_cannon(offset)

	def rotate_cannon(self, rotation_offset):
		self.model.rotate_cannon(rotation_offset)

	def make_enemies(self):
		self.model.make_enemies()

	def order_to_fire(self):
		self.model.order_to_fire()

	def remove_out_of_bound_missiles(self):
		self.model.remove_out_of_bound_missiles()

	def remove_non_active_blasts(self):
		self.model.remove_non_active_blasts()
		
	def change_gravity(self, gravity_offset):
		self.model.change_gravity(gravity_offset)

	def go_back(self):
		self.model.go_back()

	def switch_mode(self):
		self.model.switch_mode()

	def switch_cannon_mode(self):
		self.model.switch_cannon_mode()

	def get_hud(self):
		self.model.get_hud()
