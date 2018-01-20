from ..pattern.observer import Observer
from ..model.model import Model

import pyglet

class View(pyglet.window.Window,Observer):

	def __init__(self, playground_size):
		super().__init__(playground_size.x,playground_size.y);

		pyglet.gl.glClearColor(1,1,1,1)

		self.label =  pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size =4,
			x=20, y=self.height - 20,
			anchor_x='left', anchor_y='top')

	def update(self, model):
		self.clear()

		if isinstance(model, Model):
			drawables = model.get_drawables()
			for drawable in drawables:
				try:
					drawable.draw()
				except Exception:
					print(type(drawable))


			self.display_hud_info(model.get_hud())
			

	def display_hud_info(self, hud):

		y = self.height - 10
		for h in hud:
			label = pyglet.text.Label(h,
                        font_name='Times New Roman',
                        font_size =10,
						x=10, y=y,
						color=(0,0,0,255),
						anchor_x='left', anchor_y='top')

			label.draw()

			y-=15






			