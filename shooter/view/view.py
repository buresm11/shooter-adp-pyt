from ..pattern.observer import Observer

class View(Observer):

	def __init__(self, window, model):
		super().__init__();
		self.window = window
		self.model = model

	def update(self):
		print("cds")
