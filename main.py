"""The Basis for this Project was Modeled off of a Video Tutorial on Youtube, Found at
https://www.youtube.com/watch?v=SmKBsArp2dI"""

import pygame
import math

from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting


# init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# player
player = Player()


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw
    player.movement()

    screen.fill(BLACK)

    # ray casting
    ray_casting(screen, player.position, player.angle)

    # minimap

    # player
    pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 12)
    pygame.draw.line(
        screen,
        GREEN,
        player.position,
        (
            player.x + WIDTH * math.cos(player.angle),
            player.y + WIDTH * math.sin(player.angle),
        ),
    )

    # map
    for x, y in world_map:
        pygame.draw.rect(screen, WHITE, (x, y, TILE, TILE), 2)

    # frame
    pygame.display.flip()
    clock.tick(FPS)
