
import pygame
from player import direction_to_position

def player_pos_to_direction(player_pos, direction):
	print("TBD")
	return (0,0)

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
		self.direction = player_pos_to_direction(playerPosition, self.direction)
	def update(self,dt,events,screen,playerPosition):
		self.draw(screen=screen)
		self.update_direction(playerPosition)
		self.update_position()
		