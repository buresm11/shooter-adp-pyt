import math

from abc import ABC, abstractmethod

class Strategy(ABC):

	@abstractmethod
	def move(missile):
		pass

class SimpleStrategy(Strategy):

	def move(self, missile):
		missile.time += 0.2

		missile.x += (missile.fire_power) * math.cos(missile.angle)
		missile.y -= (missile.fire_power) * math.sin(missile.angle)

class SmartStrategy(Strategy):

	def move(self, missile):
		missile.time += 0.2
		gra = -9.8

		missile.lastx = missile.x
		missile.lasty = missile.y

		missile.x =  missile.fired_pos.x + missile.fire_power * missile.time * math.cos(missile.angle)
		missile.y =	 missile.fired_pos.y - missile.fire_power * missile.time * math.sin(missile.angle) + 1/2*gra*missile.time*missile.time

		x = missile.x - missile.lastx
		y =  missile.lasty - missile.y

		missile.rotation = math.degrees(math.atan2(y,x))
