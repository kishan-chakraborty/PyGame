import pygame

running = True

# Declare the screen dimension.
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
line_color = (255, 0, 0)
bg_color = (0, 0, 0)

y = 1
dirc = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    # Move a horizontal line vertically
    screen.fill(bg_color)
    pygame.draw.line(screen, line_color, (0, y), (width - 1, y))
    pygame.draw.line(screen, line_color, (0, height - y), (width, height - y))
    pygame.draw.line(screen, line_color, (0, 2 * y), (width - 1, 2 * y))
    pygame.draw.line(screen, line_color, (0, height - 2 * y), (width, height - 2 * y))

    # Move a vertical line horizontally
    pygame.draw.line(screen, (0, 255, 0), (y, 0), (y, height))
    pygame.draw.line(screen, (0, 255, 0), (width - y, 0), (width - y, height))
    pygame.draw.line(screen, (0, 255, 0), (y * 2, 0), (y * 2, height))
    pygame.draw.line(screen, (0, 255, 0), (width - y * 2, 0), (width - y * 2, height))

    y = y + dirc
    if y < 0 or y > height - 1:
        dirc *= -1

    pygame.display.flip()
