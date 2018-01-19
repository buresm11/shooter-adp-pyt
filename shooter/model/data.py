from enum import Enum


class Situation(Enum):
	SIMPLE = 1
	SMART = 2

class CannonSituation(Enum):
	ONE_MISSILE = 1
	TWO_MISSILE = 2

class Direction(Enum):
	EAST = 1
	WEST = 2
	NORTH = 3
	SOUTH = 4

class Vector():

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

class Size():

	def __init__(self, x, y):
		self.x = x;
		self.y = y;