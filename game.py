import pygame

for i in range(0,3):
	print("hello")

def quit_game(events):
	for event in events:
		if event.type == pygame.QUIT:
			return True
	return False



class Game():
	def __init__(self) -> None:
		self.screen = None
		self.clock = None
		self.text_surface = None
	def load(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))
		self.clock = pygame.time.Clock()
		return self
	def update(self,dt,events):
		if self.screen is None:
			return
		self.screen.fill("purple")
		pygame.display.flip()
	def run_game_loop(self):
		if self.screen is None or self.clock is None:
			return
		while True:
			events = pygame.event.get()
			if quit_game(events):
				break
			dt = self.clock.tick(60)
			self.update(events,dt)
		pygame.quit()

def run_game():
	g = Game().load()
	g.run_game_loop()

if __name__ == "__main__":
	run_game()