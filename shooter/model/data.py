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

	def copy():
		return Vector(self.x, self.y)

class Size():

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

	def copy():
		return Size(self.x, self.y)

class Rect():

	def __init__(self, left_bottom, right_top):
		self.left_bottom = left_bottom
		self.right_top = right_top

	def intersect(self, rect):

		res = not (self.left_bottom.x > rect.right_top.x or self.right_top.x < rect.left_bottom.x or \
			self.right_top.y < rect.left_bottom.y or self.left_bottom.y > rect.right_top.y)

		return res
