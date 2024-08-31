"""
Drawing a line on the game screen.
"""

import numpy as np
import pygame

# Declare the screen dimension.
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

# Define line geometry.
line_color = (255, 0, 0)
line1_start = (0, 0)
line1_end = (width, height)
line2_start = (0, height)
line2_end = (width, 0)


def connect_to_point(
    screen,
    point: tuple,
    points: list[tuple],
    line_color: tuple = (255, 255, 255),
) -> None:
    """
    Function which connect points on the edge to the given point.
    Connect fifty point on the edge and connect them to the given point.

    Args:
        screen: Game screen to draw the lines in.
        point: Point to connect to.
        points: list of points to connect.
        line_color: color of the connected lines.
    Return:
        None
    """
    for pt in points:
        pygame.draw.aaline(screen, line_color, pt, point)


def draw_curve():
    pass


running = True
while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False

    # Exercise 1-5
    # Draw two diagonal lines using pygame.draw.line or aaline.
    pygame.draw.line(screen, line_color, line1_start, line1_end)  # uneven line.
    pygame.draw.aaline(screen, line_color, line2_start, line2_end)  # less jagged.

    # Draw two perpendicular lines along boh axis at the center of the screen.
    pygame.draw.line(screen, line_color, (width / 2, 0), (width / 2, height))
    pygame.draw.line(screen, line_color, (0, height / 2), (width, height / 2))

    # It is a method to update the screen.
    # Used when we want to display all the drawn content on the screen at once.
    screen.fill((0, 0, 0))

    # Exercise 6
    # ADDING THE VERTICAL LINES
    n_points = 30
    # Upper left corner
    point_range = np.linspace(0, height / 2, n_points)
    points = [(0, pt) for pt in point_range]
    point_to_cont = (width / 2, 0)
    connect_to_point(screen, point_to_cont, points)

    # Upper right corner
    points = [(width, pt) for pt in point_range]
    connect_to_point(screen, point_to_cont, points)

    # Bottom right corner
    point_to_cont = (width / 2, height)
    points = [(width, pt + height / 2) for pt in point_range]
    connect_to_point(screen, point_to_cont, points)

    # Bottom left corner
    point_to_cont = (width / 2, height)
    points = [(0, pt + height / 2) for pt in point_range]
    connect_to_point(screen, point_to_cont, points)

    # ADDING THE VERTICAL LINES
    # upper left quadrant
    point_range = np.linspace(0, width / 2, n_points)
    point_to_cont = (0, height / 2)
    points = [(pt, 0) for pt in point_range]
    connect_to_point(screen, point_to_cont, points, line_color=(100, 100, 100))

    # bottom left quadrant
    points = [(pt, height) for pt in point_range]
    connect_to_point(screen, point_to_cont, points, line_color=(100, 100, 100))

    # bottom right quadrant
    point_to_cont = (width, height / 2)
    points = [(pt + width / 2, height) for pt in point_range]
    connect_to_point(screen, point_to_cont, points, line_color=(100, 100, 100))

    # Upper right qudrant
    points = [(pt + width / 2, 0) for pt in point_range]
    connect_to_point(screen, point_to_cont, points, line_color=(100, 100, 100))

    ellipse = pygame.Rect(0, 0, width, height)
    pygame.draw.ellipse(screen, (0, 0, 0), ellipse)

    pygame.display.flip()
