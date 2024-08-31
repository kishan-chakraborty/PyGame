import pygame

running = True

# Declare the screen dimension.
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

bar_color = [(0, 0, i * 4) for i in range(1, 63)]
bar_color2 = [(0, 0, 255 - i * 4) for i in range(1, 63)]
bar_color = bar_color + bar_color2

bar_color_red = [(i * 4, 0, 0) for i in range(1, 63)]
bar_color_red2 = [(255 - i * 4, 0, 0) for i in range(1, 63)]
bar_color_red += bar_color_red2
bar_height = 124

running = True
y = 0
dir = 1
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 0))
    for i in range(bar_height):
        pygame.draw.line(screen, bar_color[i], (0, y + i), (width, y + i))

    for i in range(bar_height):
        pygame.draw.line(
            screen, bar_color_red[i], (0, height - y - i), (width, height - y - i)
        )

    for i in range(bar_height):
        pygame.draw.line(screen, bar_color[i], (y + i, 0), (y + i, height))

    for i in range(bar_height):
        pygame.draw.line(
            screen, bar_color_red[i], (width - y - i, 0), (width - y - i, height)
        )

    y += dir

    if bar_height + y > height or y < 0:
        dir *= -1

    pygame.display.flip()
