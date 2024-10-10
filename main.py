import pygame
from constants import *

def main():
    print(type(SCREEN_WIDTH))
    pygame.init()
    area = (SCREEN_WIDTH, SCREEN_HEIGHT)
    game = pygame.display.set_mode(area)
    while pygame.display.get_init:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        game.fill((0,0,0))
        pygame.display.flip()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()