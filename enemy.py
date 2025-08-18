
import pygame
from player import direction_to_position
from collections import namedtuple

# maybe A* pathfinding?? What's the easiest option?
def player_pos_to_direction(enemy_pos, player_pos, direction):
	print("TBD")
	return (0,0)


Successor = namedtuple("Successor",["f", "g", "h", "parent"])

def sort_by_f(node):
  return node.f

class Search():
	def __init__(self, target,position, size) -> None:
		starting_node = Successor(0,0,0,None)
		self.target = target
		self.open_list = [starting_node]
		self.closed_list = []
	def add_successors(self,q):
		print("TBD")
		return []
	def get_node_with_lowest_f(self):
		if len(self.open_list) < 1:
			return None
		self.open_list.sort(key=sort_by_f)
		return self.open_list[0]
	def start_search(self):
		while len(self.open_list) > 0:
			q = self.get_node_with_lowest_f()
			if q is None:
				return None
			successors = self.add_successors(q)
			for successor in successors:
				if successor.position == self.target:
					break
			
		
	
		

class EnemySprite():
	def __init__(self, init_pos) -> None:
		self.image = None
		self.key = "banana.png"
		self.position = init_pos
		self.direction = (0,0)
	def load(self):
		self.image = pygame.image.load(self.key)
		self.image = pygame.transform.scale_by(self.image, 2).convert()
	def draw(self,screen):
		if self.image is None:
			return
		screen.blit(self.image, self.image.get_rect(center=self.position))
	def update_position(self):
		self.position = direction_to_position(self.direction, self.position)
	def update_direction(self,playerPosition):
		self.direction = player_pos_to_direction(self.position, playerPosition, self.direction)
	def update(self,dt,events,screen,playerPosition):
		self.draw(screen=screen)
		self.update_direction(playerPosition)
		self.update_position()
		