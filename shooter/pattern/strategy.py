from abc import ABC, abstractmethod


class Strategy(ABC):

	@abstractmethod
	def move(missile):
		pass

class SimpleStrategy(Strategy):

	def move(self, missile):
		missile.x += missile.fire_power

class SmartStrategy(Strategy):

	def move(self, missile):
		missile.x += 1
		missile.y += 2