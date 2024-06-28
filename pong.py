import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle dimensions
paddle_width = 10
paddle_height = 100

# Ball dimensions
ball_size = 10

# Paddle positions
left_paddle_x = 50
left_paddle_y = screen_height // 2 - paddle_height // 2
right_paddle_x = screen_width - 50 - paddle_width
right_paddle_y = screen_height // 2 - paddle_height // 2

# Ball position and speed
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 3
ball_speed_y = 3

# Paddle speed
paddle_speed = 5

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

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

    # Move left paddle
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
        left_paddle_y += paddle_speed

    # Move right paddle
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
        right_paddle_y += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= left_paddle_x + paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height) or \
       (ball_x >= right_paddle_x - ball_size and right_paddle_y <= ball_y <= right_paddle_y + paddle_height):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball_x <= 0 or ball_x >= screen_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x *= -1

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
