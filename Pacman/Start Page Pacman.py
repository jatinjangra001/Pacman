import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
window_width = 900
window_height = 950

back_music = pygame.mixer.Sound('resources/sounds/pacman_beginning.wav')
back_music.set_volume(0.5)

# Set colors
black = (0, 0, 0)
yellow = (255, 255, 0)

# Load the background image
background_image = pygame.image.load('resources/images/newbck.png')

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pacman")

# Define the start button
start_button = pygame.Rect((window_width/3), (window_height/1.3), 300, 100)

# Set the blinking parameters
blink_speed = 500  # milliseconds
last_blink_time = 0
blink_on = True

# Set the cursor shapes
cursor_normal = pygame.mouse.get_cursor()
cursor_hover = pygame.cursors.tri_left

# Create a font object for the button text
font = pygame.font.SysFont('Arial', 20)

# Main game loop
while True:
    # Check for events
    back_music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the start button was clicked
            if start_button.collidepoint(event.pos):
                import maingame
                back_music.stop()

    # Blit the background image onto the screen
    window.blit(background_image, (0, 0))

    # Draw the start button
    pygame.draw.rect(window, black, start_button)

    # Draw the button text
    current_time = pygame.time.get_ticks()
    if current_time - last_blink_time > blink_speed:
        last_blink_time = current_time
        blink_on = not blink_on
    text_surface = font.render('Click here to Start', True, black if blink_on else yellow)
    text_rect = text_surface.get_rect(center=start_button.center)
    window.blit(text_surface, text_rect)

    # Change cursor shape when hovering over button
    if start_button.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_cursor(*cursor_hover)
    else:
        pygame.mouse.set_cursor(*cursor_normal)

    # Update the screen
    pygame.display.update()
