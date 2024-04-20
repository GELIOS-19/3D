# player

import pygame
import math

from settings import *


class Player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle

    @property
    def position(self):
        return self.x, self.y

    def movement(self):
        # angle
        sin_angle = math.sin(self.angle)
        cos_angle = math.cos(self.angle)

        # keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.x += player_speed * cos_angle
            self.y += player_speed * sin_angle
            print("W")
        if keys[pygame.K_a]:
            self.x += player_speed * sin_angle
            self.y += -player_speed * cos_angle
            print("A")
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_angle
            self.y += -player_speed * sin_angle
            print("S")
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_angle
            self.y += player_speed * cos_angle
            print("D")

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
