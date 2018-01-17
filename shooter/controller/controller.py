

class Controller():

	def __init__(self, app, clock, view, model):
		self.app = app
		self.clock = clock
		self.view = view
		self.model = model

	def run(self):
		self.clock.schedule_interval(self.tick, 1/30)
		self.app.run()

	def tick(self, t):
		print("tick")


