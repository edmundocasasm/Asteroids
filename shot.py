from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_SHOOT_VELOCITY
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Update the position based on velocity and delta time
        self.position += self.velocity * dt