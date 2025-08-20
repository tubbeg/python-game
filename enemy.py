
import pygame
from player import direction_to_position
from collections import namedtuple
from dataclasses import dataclass
import math


@dataclass
class Node():
	value : float
	position : tuple[int,int]

def pos_is_equal(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	return x1 == x2 and y1 == y2

def positions_to_nodes(positions, exclude):
	l = []
	for pos in positions:
		if pos not in exclude:
			l.append(Node(float("inf"), pos))
	return l

def is_neighbour(p1, p2):
	if pos_is_equal(p1,p2):
		return False
	(x1,y1),(x2,y2) = p1,p2
	if (x1 - 1) == x2 and y1 == y2:
		return True
	if (x1 + 1) == x2 and y1 == y2:
		return True
	if x1 == x2 and (y1 - 1) == y2:
		return True
	if x1 == x2 and (y1 + 1) == y2:
		return True###
	if (x1 - 1) == x2 and (y1 - 1) == y2:
		return True
	if (x1 - 1) == x2 and (y1 + 1) == y2:
		return True
	if (x1 + 1) == x2 and (y1 - 1) == y2:
		return True
	return (x1 + 1) == x2 and (y1 + 1) == y2

def get_neighbours(position, nodes):
	l = []
	for node in nodes:
		if is_neighbour(node.position, position):
			l.append(node)
	return l


def get_dist(p1,p2):
	# Should I use Pythagoras as weight?
	(x1,y1),(x2,y2) = p1,p2
	dtx = x1 - x2
	dty = y1 - y2
	dtxsq = dtx * dtx 
	dtysq = dty * dty
	res = math.sqrt(dtxsq + dtysq)
	return math.ceil(res * 10)

# an attempt to implement djikstra's algorithm
class Search():
	def __init__(self, target, source, positions) -> None:
		self.nodes = positions_to_nodes(positions=positions, exclude=[target,source])
		self.source = Node(0,source)
		self.target = Node(float("inf"), target)
		self.nodes.append(self.target)
		self.nodes.append(self.source)
		self.visited_nodes = []
	def visit_node(self, node):
		if node is None:
			print("Error!")
			return
		self.visited_nodes.append(node)
		self.eval_neighbours(node)
		self.nodes.remove(node)
	def eval_neighbour(self,neighbour, node):
		weight = get_dist(neighbour.position, self.target.position)
		val = node.value + weight
		if val < neighbour.value:
			neighbour.value = val
	def eval_neighbours(self,node):
		if node is None:
			return
		for n in get_neighbours(node.position, self.nodes):
			self.eval_neighbour(n, node)
	def select_node(self):
		n = None
		for node in self.nodes:
			if n is None:
				n = node
			if node.value < n.value:
				n = node
		return n
	def run_djikstra_search(self):
		while len(self.nodes) > 0:
			node = self.select_node()
			if node is None:
				return None
			if pos_is_equal(node.position, self.target.position):
				return self.visited_nodes
			self.visit_node(node)
		return self.visited_nodes
	
def generate_positions(x,y):
	l = []
	for i in range(0,x):
		for j in range(0,y):
			l.append((i,j))
	return l

def run_test_case():
	positions = generate_positions(10,10)
	print(len(positions))
	target = (3,9)
	source = (1,6)
	s = Search(target, source, positions)
	result = s.run_djikstra_search()
	if result is None:
		print("ERROR!")
		return
	print(len(result))
	print(result)
	

class EnemySprite():
	def __init__(self, init_pos, target_pos) -> None:
		self.image = None
		self.key = "banana.png"
		self.position = init_pos
		self.direction = (0,0)
		self.target  = target_pos
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
		self.direction = "Something??"
	def update(self,dt,events,screen,playerPosition):
		self.draw(screen=screen)
		self.update_direction(playerPosition)
		self.update_position()
		