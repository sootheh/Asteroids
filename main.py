import pygame
from asteroidfield import AsteroidField
from player import Player
from constants import *
from asteroid import Asteroid
from shots import Shot

def main():
    pygame.init()
    area = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(area)
    clock = pygame.time.Clock()
    dt = 0
    
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, shots, drawable)
    AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    

    while pygame.display.get_init:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.detect_collision(player):
                print("Game Over")
                pygame.quit()
        for draw in drawable:
            draw.draw(screen) 

     
        pygame.display.flip()
        dt = clock.tick(60)
        dt = dt/1000
        
    
if __name__ == "__main__":
    main()