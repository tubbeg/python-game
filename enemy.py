
import pygame
from player import direction_to_position
from collections import namedtuple
from dataclasses import dataclass
import math



# maybe A* pathfinding?? What's the easiest option?
def player_pos_to_direction(enemy_pos, player_pos, direction):
	print("TBD")
	return (0,0)



def get_neighbours(position):
	x,y = position
	up_y = y + 1
	up_x = x + 1
	down_y = y - 1
	down_x = x - 1
	top = (x,up_y)
	down = (x,down_y)
	left = (x,up_y)
	right = (x,down_y)
	topright = (up_x, up_y)
	topleft = (down_x,up_y)
	downright = (down_y, up_x)
	downleft = (down_x, down_y)
	return [top,down,left,right,topright,topleft,downright,downleft]



@dataclass
class Node():
	value : int
	position : tuple[int,int]


def pos_to_node(pos):
	return Node(-1, pos)

def is_neighbour(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	if x1 == x2 and  y1 == y2:
		return False
	topleft = (y1 + 1) == y2 and (x1 - 1) == x2
	topright = (y1 + 1) == y2 and (x1 + 1) == x2
	bottomright = (y1 - 1) == y2 and (x1 + 1) == x2
	bottomleft = (y1 - 1) == y2 and (x1 - 1) == x2
	left = y1 == y2 and (x1 - 1) == x2
	right = y1 == y2 and (x1 + 1) == x2
	top = (y1 + 1) == y2 and x1 == x2
	bottom = (y1 - 1) == y2 and x1 == x2
	corners = topleft or topright or bottomleft or bottomright
	horiz = left or right
	ver = top or bottom
	return corners or horiz or ver

def filter_neighbours(nodes, current_node):
	pos = current_node.position
	filter_function = lambda n: is_neighbour(n.position,pos) 
	return list(filter(filter_function,nodes))

def calc_distance(p1,p2):
	# super complicated math right here
	x1,y1 = p1
	x2,y2 = p2
	delta_x = x1 - x2
	delta_y = y1 - y2
	return math.sqrt((delta_x * delta_x) + (delta_y * delta_y))

def calculate_value(current_node, neighbour_node):
	weight = calc_distance(current_node.position, neighbour_node.position)
	v = current_node.value + weight
	return v

def visit_neighbours(nodes, current_node):
	neighbours = filter_neighbours(nodes, current_node=current_node)
	for n in neighbours:
		n.value = calculate_value(current_node=current_node, neighbour_node=n)
	return nodes

def select_node(nodes):
	sel = None
	for node in nodes:
		if sel is None:
			sel = node
		elif sel.value > node.value and sel.value >= 0:
			sel = node
	return sel

def djikstra_search(target_position, starter_position, positions):
	visited_nodes = []
	starter_position = Node(0, starter_position)
	target_node = Node(-1, target_position)
	unvisited_nodes = list(map(pos_to_node, positions))
	unvisited_nodes.append(starter_position)
	unvisited_nodes.append(target_node)
	while len(unvisited_nodes) > 0:
		node = select_node(unvisited_nodes)
		if node is None:
			print("Error! No nodes left!")
			break
		visited_nodes.append(node)
		unvisited_nodes = visit_neighbours(unvisited_nodes, node)
		unvisited_nodes.remove(node)
	return visited_nodes




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
		