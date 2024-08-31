"""
First pygame tutorial.
based on https://lorenzod8n.wordpress.com/2007/05/25/pygame-tutorial-1-getting-started/
"""

import pygame

# tutorial 1
screen = pygame.display.set_mode((640, 400))
pygame.time.wait(300)
screen = pygame.display.set_mode((800, 700))
# while True:
#     pass


# Tutorial 2
# Use break statementto do away with the running loop.
running = True
while running:
    # Inside the loop we use the poll method to grab the next event from the event queue.
    event = pygame.event.poll()

    # QUIT, which gets triggered when the user clicks on the window’s close button.
    if event.type == pygame.QUIT:
        # If QUIT stop the game.
        running = False
        # break [Used to do away with the running flag.]

    # Tutorial 3
    # fill the screent with a color
    screen.fill((255, 0, 0))
    pygame.display.flip()
