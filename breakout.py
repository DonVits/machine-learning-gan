import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Paddle dimensions
paddle_width = 100
paddle_height = 10
paddle_speed = 7

# Ball dimensions and speed
ball_size = 10
ball_speed_x = 3
ball_speed_y = -3

# Brick dimensions
brick_rows = 6
brick_cols = 10
brick_width = 60
brick_height = 20
brick_padding = 10
brick_offset_top = 50
brick_offset_left = 35

# Initialize paddle position
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 30

# Initialize ball position
ball_x = screen_width // 2
ball_y = screen_height - 50

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')

# Create bricks
bricks = []
for row in range(brick_rows):
    brick_row = []
    for col in range(brick_cols):
        brick_x = brick_offset_left + col * (brick_width + brick_padding)
        brick_y = brick_offset_top + row * (brick_height + brick_padding)
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_row.append(brick_rect)
    bricks.append(brick_row)

# Clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= screen_width - ball_size:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # Ball collision with paddle
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
    if ball_rect.colliderect(paddle_rect):
        ball_speed_y *= -1

    # Ball collision with bricks
    for row in bricks:
        for brick in row:
            if ball_rect.colliderect(brick):
                ball_speed_y *= -1
                row.remove(brick)
                break

    # Ball out of bounds
    if ball_y > screen_height:
        ball_x = screen_width // 2
        ball_y = screen_height - 50
        ball_speed_x = 3 * random.choice([1, -1])
        ball_speed_y = -3

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle_rect)
    pygame.draw.ellipse(screen, white, ball_rect)
    for row in bricks:
        for brick in row:
            pygame.draw.rect(screen, blue, brick)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
