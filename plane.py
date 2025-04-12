import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Airplane Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Airplane class
class Airplane:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 4, screen_height // 2)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

# Obstacle class
class Obstacle:
    def __init__(self):
        self.width = 50
        self.height = random.randint(50, 100)
        self.x = random.randint(screen_width, screen_width + 100)
        self.y = random.randint(0, screen_height - self.height)
        self.speed = random.randint(5, 10)

    def move(self):
        self.x -= self.speed

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

# Game loop
def game_loop():
    airplane = Airplane()
    obstacles = []
    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.SysFont('Arial', 30)
    
    # Main game loop
    running = True
    while running:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()
        airplane.move(keys)
        airplane.draw()

        # Create new obstacles
        if random.random() < 0.02:
            obstacles.append(Obstacle())

        # Move and draw obstacles
        for obstacle in obstacles[:]:
            obstacle.move()
            obstacle.draw()
            if obstacle.x < 0:
                obstacles.remove(obstacle)
                score += 1  # Increment score when obstacle moves off-screen

            # Check for collision
            if airplane.rect.colliderect(pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)):
                running = False  # Game over if there is a collision

        # Draw the score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)  # 60 frames per second

    pygame.quit()

# Start the game
game_loop()
