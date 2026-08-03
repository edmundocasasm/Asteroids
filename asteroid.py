import pygame, random
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Update the position based on velocity and delta time
        self.position += self.velocity * dt

    def split(self) -> None:
        # Split the asteroid into two smaller asteroids
        self.kill()  # Remove the current asteroid from the game
        if self.radius <= ASTEROID_MIN_RADIUS:  # Minimum size to split
            return

        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        asteroid_1_vector = self.velocity.rotate(new_angle)
        asteroid_2_vector = self.velocity.rotate(-new_angle) 

        new_radius = self.radius - ASTEROID_MIN_RADIUS  # Reduce the radius for the new asteroids

        
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = asteroid_1_vector * 1.2
        asteroid_2.velocity = asteroid_2_vector * 1.2
