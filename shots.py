from circleshape import CircleShape
import pygame
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.velocity = PLAYER_SHOOT_SPEED
        self.rotation = rotation
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 1)

    def update(self, dt):
        vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += vector * PLAYER_SHOOT_SPEED * dt