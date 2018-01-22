import os
import pickle

class Visitor():

	def __init__(self):
		self.data = {}
		self.path = os.path.dirname(__file__) + '/../res/save'

		self.enemies = []

	def visit_simple_enemy(self, simple_enemy):
		self.enemies.append(('simple', simple_enemy.x, simple_enemy.y))

	def visit_smart_enemy(self, smart_enemy):
		self.enemies.append(('smart', simple_enemy.x, simple_enemy.y))

	def visit_cannon(self, cannon):
		self.data['cannon_x'] = cannon.x
		self.data['cannon_y'] = cannon.y
		self.data['cannon_angle'] = cannon.angle
		self.data['gravity'] = cannon.gravity
		self.data['cannon_situation'] = cannon.situation

	def visit_missile(self, missile):
		pass

	def visit_blast(self, blast):
		pass

	def visit_model(self, model):
		self.data['score'] = model.score
		self.data['situation'] = model.situation

	def save(self):
		self.data['enemies'] = self.enemies
		with open(self.path, 'wb') as f:
			pickle.dump(self.data, f, pickle.HIGHEST_PROTOCOL)

		print("saved")
    	
