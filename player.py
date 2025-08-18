
import pygame

def is_key_press(events):
	for event in events:
		if event.type == pygame.KEYDOWN:
			return event
	return None

def is_key_up(events):
	for event in events:
		if event.type == pygame.KEYUP:
			return True
	return False

def direction_to_position(direction,position):
	if direction == (0,0):
		return position
	a,b = direction
	x,y = position
	if a == 1:
		x += 10
	if a == -1:
		x -= 10
	if b == 1:
		y += 10
	if b == -1:
		y -= 10
	return x,y

def key_press_to_direction(events, direction):
	keys = pygame.key.get_pressed()
	if is_key_up(events):
		return (0,0)
	a,b = direction
	if keys[pygame.K_a]:
		a = -1
	if keys[pygame.K_d]:
		a = 1
	if keys[pygame.K_s]:
		b = 1
	if keys[pygame.K_w]:
		b = -1
	return a,b


class PlayerSprite():
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
	def update_direction(self,events):
		self.direction = key_press_to_direction(events, self.direction)
	def update(self,dt,events,screen):
		self.draw(screen=screen)
		self.update_direction(events)
		self.update_position()
		