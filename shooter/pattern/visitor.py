
class Visitor(ABC):

    def visit_simple_enemy(self, simple_enemy):
    	print("senemy")

    def visit_smart_enemy(self, smart_enemy):
    	print("enemy")

    def visit_cannon(self, cannon):
    	print("cannon")

    def visit_missile(self, missile):
    	print("missile")

    def visit_blast(self, blast):
    	print("blast")

    def visit_model(self, model):
    	print("model")

