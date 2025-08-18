import pygame
from player import PlayerSprite
from enemy import EnemySprite

SIZE = 800,600

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
		self.player = PlayerSprite((300,300))
		self.enemy = EnemySprite((500,500))
	def load(self):
		pygame.init()
		self.screen = pygame.display.set_mode(SIZE)
		self.clock = pygame.time.Clock()
		self.player.load()
		self.enemy.load()
		return self
	def update(self,dt,events):
		if self.screen is None:
			return
		self.screen.fill("purple")
		self.player.update(dt,events,self.screen)
		self.enemy.update(dt, events, self.screen, self.player.position)
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
	for _ in range(0,3):
		print("hello")
	g = Game().load()
	g.run_game_loop()
	print("goodbye")

if __name__ == "__main__":
	run_game()