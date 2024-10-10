import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (dt * self.velocity)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
         
        angel1 = self.velocity.rotate(random.uniform(20,50))
        angel2 = angel1*-1
        ast1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        ast2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        ast1.velocity = angel1*1.2
        ast2.velocity = angel2*1.2