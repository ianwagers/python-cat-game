import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coraline's Laser Chase")

# Colors
GRAY = (200, 200, 200)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Load Cat Image
cat_image = pygame.image.load('C:\Project_Workspace\Coraline_Game\Cora_1.png').convert_alpha()
cat_scale_factor = 0.3
cat_image = pygame.transform.scale(cat_image, (int(cat_image.get_width() * cat_scale_factor), int(cat_image.get_height() * cat_scale_factor)))
cat_rect = cat_image.get_rect(center=(WIDTH//2, HEIGHT//2))

# Colors
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Cat and Laser settings
cat_speed = 5
laser_speed = 5
laser = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, 10)
score = 0

# Font for displaying the score
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def move_laser():
    # Move the laser away from Coraline
    if cat_rect.x < laser.x:
        laser.x += laser_speed
    else:
        laser.x -= laser_speed

    if cat_rect.y < laser.y:
        laser.y += laser_speed
    else:
        laser.y -= laser_speed

    # Keep the laser within the screen bounds
    laser.x = max(0, min(laser.x, WIDTH - laser.width))
    laser.y = max(0, min(laser.y, HEIGHT - laser.height))

def check_catch():
    global score
    if cat_rect.colliderect(laser):
        score += 1
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cat_rect.x -= cat_speed
    if keys[pygame.K_RIGHT]:
        cat_rect.x += cat_speed
    if keys[pygame.K_UP]:
        cat_rect.y -= cat_speed
    if keys[pygame.K_DOWN]:
        cat_rect.y += cat_speed

    if check_catch():
        laser.x = random.randint(0, WIDTH - laser.width)
        laser.y = random.randint(0, HEIGHT - laser.height)

    move_laser()

    # Rendering
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, laser)
    screen.blit(cat_image, cat_rect)

    # Display the score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
