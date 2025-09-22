import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock() # create a new clock object
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000


if __name__ == "__main__":
    main()
