# ray casting

import pygame

from settings import *
from map import world_map


def ray_casting(screen, player_position, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_position
    for ray in range(NUM_RAYS):
        sin_angle = math.sin(cur_angle)
        cos_angle = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_angle
            y = yo + depth * sin_angle
            # pygame.draw.line(screen, WHITE, player_position, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        ray * SCALE,
                        HALF_HEIGHT - proj_height // 2,
                        SCALE,
                        proj_height,
                    ),
                )
                break
        cur_angle += DELTA_ANGLE
