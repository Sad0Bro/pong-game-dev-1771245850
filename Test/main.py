import pygame
import sys

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = PongGame()
    game.run()