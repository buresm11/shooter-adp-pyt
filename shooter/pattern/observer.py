from abc import ABC, abstractmethod

class Observable(ABC):

	def __init__(self):
		self.obs = []

	def add_observer(self, observer):
		if not isinstance(observer, Observer):
			raise TypeError("must be of type Observer")
		elif observer not in self.obs:
			self.obs.append(observer)	

	def remove_observer(self, observer):
		if not isinstance(observer, Observer):
			raise TypeError("must be of type Observer")
		elif observer not in self.obs:
			self.obs.remove(observer)

	def notify_observers(self):
		for observer in self.obs:
			observer.update(self)

class Observer():
	def update(self):
		pass
