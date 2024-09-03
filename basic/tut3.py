# PyGame Mouse Events [done using mousemotion event.]
import pygame

x = y = 0
running = True
width, height = 600, 800
screen = pygame.display.set_mode((width, height))
linecolor = (255, 255, 255)
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos

    screen.fill((0, 0, 0))
    # Draw two intersecting lines at the point of click.
    pygame.draw.line(screen, linecolor, (x, 0), (x, height))
    pygame.draw.line(screen, linecolor, (0, y), (width, y))
    pygame.display.flip()
