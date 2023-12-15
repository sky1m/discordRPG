import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic

    # Drawing code
    screen.fill((0, 0, 0))  # Fill the screen with black
    # Add your drawing code here

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
