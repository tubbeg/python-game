import pygame

for i in range(0,3):
	print("hello")


SIZE = 800,600

def quit_game(events):
	for event in events:
		if event.type == pygame.QUIT:
			return True
	return False

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
	def __init__(self) -> None:
		self.image = None
		self.key = "sprite.jpg"
		self.position = 300,300
		self.direction = (0,0)
	def load(self):
		self.image = pygame.image.load(self.key)
		self.image = pygame.transform.scale_by(self.image, 0.5).convert()
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
		
		
class Game():
	def __init__(self) -> None:
		self.screen = None
		self.clock = None
		self.text_surface = None
		self.player = PlayerSprite()
	def load(self):
		pygame.init()
		self.screen = pygame.display.set_mode(SIZE)
		self.clock = pygame.time.Clock()
		self.player.load()
		return self
	def update(self,dt,events):
		if self.screen is None:
			return
		self.screen.fill("purple")
		self.player.update(dt,events,self.screen)
		pygame.display.flip()
	def run_game_loop(self):
		if self.screen is None or self.clock is None:
			return
		while True:
			events = pygame.event.get()
			if quit_game(events):
				break
			dt = self.clock.tick(60)
			self.update(dt,events)
		pygame.quit()

def run_game():
	g = Game().load()
	g.run_game_loop()
	print("goodbye")

if __name__ == "__main__":
	run_game()