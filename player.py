import circleshape, pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0  # Rotation angle in degrees

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360  # Keep the rotation within [0, 360) degrees

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right
        if keys[pygame.K_w]:
            self.move(dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward
    
    def move(self, dt: float) -> None:
        # Move the player in the direction it's facing
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
