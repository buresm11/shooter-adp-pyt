import pytest
import pyglet

from shooter.model.model import Model
from shooter.model.model import Images
from shooter.model.modelproxy import ModelProxy
from shooter.model.data import Size, Vector, MoveDirection, RotateDirection
from shooter.pattern.factory import SmartFactory, SimpleFactory
from shooter.pattern.state import OneMissileCannonState, TwoMissileCannonState
from shooter.pattern.strategy import SimpleStrategy, SmartStrategy
from shooter.controller.controller import SaveCommand, LoadCommand, ResetCommand

WIDTH = 800
HEIGHT = 600
EPSILON = 0.0005

@pytest.fixture
def model():
	playground_size = Size(WIDTH,HEIGHT)
	model = Model(playground_size)

	return model

@pytest.fixture
def firing_model():
	playground_size = Size(WIDTH,HEIGHT)
	model = Model(playground_size)

	cannon = model.cannon
	model.switch_cannon_mode()

	model.enemies[0].x = 100
	model.enemies[0].y = 100

	cannon.y = 100

	model.order_to_fire()
	model.fire()

	return model

@pytest.fixture
def images():
	images = Images()

	return images

def test_model_initialization(model):

	assert(model.cannon is not None)
	assert(len(model.missiles) == 0)
	assert(len(model.enemies) == 15)
	assert(len(model.blasts) == 0)
	assert(model.score == 0)
	assert(model.gravity == 10)
	assert(isinstance(model.factory, SimpleFactory))
	assert(model.size.x == WIDTH)
	assert(model.size.y == HEIGHT)

def test_model_change_mode(model):

	assert(isinstance(model.factory, SimpleFactory))
	model.switch_mode()
	assert(isinstance(model.factory, SmartFactory))
	model.switch_mode()
	assert(isinstance(model.factory, SimpleFactory))

def test_model_changes_gravity(model):

	assert(model.gravity == 10)
	
	model.change_gravity(MoveDirection.UP)
	assert(model.gravity == 11)

	model.change_gravity(MoveDirection.DOWN)
	model.change_gravity(MoveDirection.UP)
	assert(model.gravity == 11)

	for i in range(30):
		model.change_gravity(MoveDirection.DOWN)
	assert(model.gravity == 1)

	for i in range(30):
		model.change_gravity(MoveDirection.UP)
	assert(model.gravity == 19)

def test_model_is_able_to_save_and_reload_its_state_memento(model):
	
	memento = model.save_to_memento()

	assert(len(model.missiles) == 0)
	assert(model.gravity == 10)
	assert(isinstance(model.factory, SimpleFactory))
	assert(isinstance(model.cannon.state, TwoMissileCannonState))

	model.order_to_fire()
	model.fire()
	model.change_gravity(MoveDirection.UP)
	model.switch_mode()
	model.switch_cannon_mode()

	assert(len(model.missiles) != 0)
	assert(model.gravity != 10)
	assert(not isinstance(model.factory, SimpleFactory))
	assert(not isinstance(model.cannon.state, TwoMissileCannonState))

	model.get_from_memento(memento)

	assert(len(model.missiles) == 0)
	assert(model.gravity == 10)
	assert(isinstance(model.factory, SimpleFactory))
	assert(isinstance(model.cannon.state, TwoMissileCannonState))

def test_model_is_able_to_save_and_reload_its_state_file(model):

	command_save = SaveCommand(model)
	command_save.execute()

	assert(len(model.missiles) == 0)
	assert(model.gravity == 10)
	assert(isinstance(model.factory, SimpleFactory))
	assert(isinstance(model.cannon.state, TwoMissileCannonState))

	model.order_to_fire()
	model.fire()
	model.change_gravity(MoveDirection.UP)
	model.switch_mode()
	model.switch_cannon_mode()

	assert(len(model.missiles) != 0)
	assert(model.gravity != 10)
	assert(not isinstance(model.factory, SimpleFactory))
	assert(not isinstance(model.cannon.state, TwoMissileCannonState))

	command_load = LoadCommand(model)
	command_load.execute()

	assert(len(model.missiles) == 0)
	assert(model.gravity == 10)
	assert(isinstance(model.factory, SimpleFactory))
	assert(isinstance(model.cannon.state, TwoMissileCannonState))

def test_cannon_initialization(model, images):

	cannon = model.cannon

	assert(cannon.y == HEIGHT // 2)
	assert(cannon.x == images.cannon_image().width  // 2)
	assert(cannon.angle == 0)
	assert(cannon.ignition_phase == False)
	assert(isinstance(cannon.factory, SimpleFactory))
	assert(cannon.gravity == 10)
	assert(cannon.fire_power == 10)

def test_cannon_move(model, images):

	cannon = model.cannon
	before = Vector(cannon.x, cannon.y)

	model.move_cannon(MoveDirection.UP)
	assert(before.y == cannon.y - 5)
	assert(before.x == cannon.x)

	model.move_cannon(MoveDirection.DOWN)
	assert(before.y == cannon.y)
	assert(before.x == cannon.x)

def test_cannon_does_not_move_outside_screen(model, images):

	cannon = model.cannon

	for i in range(200):
		model.move_cannon(MoveDirection.UP)

	assert(cannon.y == HEIGHT - images.cannon_image().height // 2)
	assert(cannon.x == images.cannon_image().width  // 2)

	for i in range(200):
		model.move_cannon(MoveDirection.DOWN)

	assert(cannon.y == images.cannon_image().height // 2)
	assert(cannon.x == images.cannon_image().width  // 2)

def test_cannon_rotates(model, images):

	cannon = model.cannon

	assert(cannon.angle == 0)
	model.rotate_cannon(RotateDirection.LEFT)
	assert(cannon.angle + 0.1 < EPSILON )
	model.rotate_cannon(RotateDirection.RIGHT)
	assert(cannon.angle - 0.1 < EPSILON)

def test_cannon_mode_change(model):

	cannon = model.cannon
 
	assert(isinstance(cannon.state, TwoMissileCannonState))
	model.switch_cannon_mode()
	assert(isinstance(cannon.state, OneMissileCannonState))
	model.switch_cannon_mode()
	assert(isinstance(cannon.state, TwoMissileCannonState))

def test_cannon_order_to_fire_creates_correct_number_of_missiles(model):

	cannon = model.cannon
 
	assert(isinstance(cannon.state, TwoMissileCannonState))
	model.order_to_fire()
	assert(len(cannon.prepared_missiles) == 2)

	model.fire()
	model.switch_cannon_mode()

	assert(isinstance(cannon.state, OneMissileCannonState))
	model.order_to_fire()
	assert(len(cannon.prepared_missiles) == 1)

def test_cannon_creates_correct_type_of_missile(model):

	cannon = model.cannon
 
	assert(isinstance(cannon.state, TwoMissileCannonState))
	model.order_to_fire()
	assert(len(cannon.prepared_missiles) == 2)

	assert(isinstance(model.factory, SimpleFactory))
	assert(isinstance(cannon.prepared_missiles[0].strategy, SimpleStrategy))

	model.fire()
	model.switch_mode()
	model.order_to_fire()

	assert(len(cannon.prepared_missiles) == 2)
	assert(isinstance(model.factory, SmartFactory))
	assert(isinstance(cannon.prepared_missiles[0].strategy, SmartStrategy))

def test_missiles_are_moved_with_cannon(model):

	model.switch_cannon_mode()
	cannon = model.cannon
	assert(isinstance(cannon.state, OneMissileCannonState))

	model.order_to_fire()
	assert(len(cannon.prepared_missiles) == 1)

	for i in range(5):
		model.move_cannon(MoveDirection.UP)

	assert(cannon.x == cannon.prepared_missiles[0].x)
	assert(cannon.y == cannon.prepared_missiles[0].y)

def test_missiles_are_rotated_with_cannon(model):

	model.switch_cannon_mode()
	cannon = model.cannon
	assert(isinstance(cannon.state, OneMissileCannonState))

	model.order_to_fire()
	assert(len(cannon.prepared_missiles) == 1)

	for i in range(5):
		model.rotate_cannon(RotateDirection.LEFT)

	assert(cannon.angle - cannon.prepared_missiles[0].angle < EPSILON)

def test_cannon_order_to_fire_increases_firepower(model):
	
	cannon = model.cannon

	model.order_to_fire()
	assert(cannon.fire_power == 10)

	for i in range(40):
		model.tick()

	assert(cannon.fire_power == 25)

def test_cannon_fire(model):

	cannon = model.cannon

	model.order_to_fire()
	assert(len(cannon.prepared_missiles) > 0)
	model.fire()
	assert(len(cannon.prepared_missiles) == 0)
	assert(len(model.missiles) > 0)

def test_outlived_missile_get_deleted(model):

	model.order_to_fire()
	model.fire()
	assert(len(model.missiles) > 0)

	for i in range(1000):
		model.tick()

	assert(len(model.missiles) == 0)

def test_simple_missile_do_not_use_gravity(model):

	cannon = model.cannon
	model.switch_cannon_mode()
	assert(cannon.angle == 0)
	assert(isinstance(model.factory, SimpleFactory))
	assert(isinstance(cannon.state, OneMissileCannonState))
	
	model.order_to_fire()
	model.fire()
	assert(len(model.missiles) > 0)

	ypos = model.missiles[0].y

	for i in range(20):
		model.tick()
		assert(ypos == model.missiles[0].y)

def test_smart_missiles_use_gravity(model):

	cannon = model.cannon
	model.switch_cannon_mode()
	assert(cannon.angle == 0)
	model.switch_mode()
	assert(isinstance(model.factory, SmartFactory))
	assert(isinstance(cannon.state, OneMissileCannonState))
	
	model.order_to_fire()
	model.fire()
	assert(len(model.missiles) > 0)

	ypos = model.missiles[0].y

	for i in range(20):
		model.tick()
	
	assert(ypos > model.missiles[0].y)	

def test_missile_kills_enemy(firing_model):
	
	enemies_count = len(firing_model.enemies)

	shot = False
	for i in range(1000):
		firing_model.tick()
		if(len(firing_model.enemies) < enemies_count):
			shot = True
			break

	assert(shot == True)

def test_blast_appears_after_enemy_has_been_killed(firing_model):
	
	enemies_count = len(firing_model.enemies)

	for i in range(1000):
		firing_model.tick()
		if(len(firing_model.enemies) < enemies_count):
			assert(len(firing_model.blasts) > 0)
			break

def test_blast_disappear(firing_model):
	
	enemies_count = len(firing_model.enemies)

	for i in range(1000):
		firing_model.tick()
		if(len(firing_model.enemies) < enemies_count):
			assert(len(firing_model.blasts) > 0)
			break

	for i in range(100):
		firing_model.tick()

	assert(len(firing_model.blasts) == 0)

def test_simple_enemy_does_not_move(model):

	enemies = model.enemies
	before = []

	assert(isinstance(model.factory,SimpleFactory))

	for e in enemies:
		before.append(Vector(e.x,e.y))

	model.tick()

	assert(len(enemies) == len(before))

	for i in range(len(before)):
		assert(before[i].x == enemies[i].x)
		assert(before[i].y == enemies[i].y)

def test_smart_enemy_move(model, images):

	enemies = model.enemies
	before = []

	model.switch_mode()
	assert(isinstance(model.factory,SmartFactory))

	for e in enemies:
		before.append(Vector(e.x,e.y))

	model.tick()

	assert(len(enemies) == len(before))

	for i in range(len(before)):
		if before[i].x != images.enemy_image().width //2 and before[i].x != WIDTH - images.enemy_image().width // 2 and\
			before[i].y != images.enemy_image().height //2 and before[i].y != HEIGHT - images.enemy_image().height // 2:

				changed = before[i].x != enemies[i].x or before[i].y != enemies[i].y
				assert(changed == True)