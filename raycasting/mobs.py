from settings import *
import pygame
from numba import njit


class Mobs(pygame.sprite.Sprite):
    def __init__(self, position, mob_type):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = position
        self.speed = mob_speed
        self.type = mob_type
        self.image = pygame.image.load('images/воловик.png').convert_alpha()
        self.mob_wight = 40

    def mob_distance(self, pl_pos):
        return dist_calc(self.x, self.y, pl_pos)

    def mob_angle(self, player_position):
        return angle_calc(self.x, self.y, player_position)

    def update(self, player_position):
        if self.mob_distance(player_position) < self.mob_wight:
            return True

        angle = (self.mob_angle(player_position) + math.pi) % (2 * math.pi)
        delt_y = self.speed * math.sin(angle)
        delt_x = self.speed * math.cos(angle)

        self.x += delt_x
        self.y += delt_y


@njit(fastmath=True)
def angle_calc(x, y, player_position):
    player_x, player_y = player_position
    if player_x > x and player_y <= y:
        angle = math.pi - math.atan((player_y - y) / (x - player_x + 0.000001))
    elif player_x == x and player_y <= y:
        angle = math.pi / 2
    elif player_x >= x and player_y >= y:
        angle = math.pi + math.atan((player_y - y) / (player_x - x + 0.000001))
    elif player_x <= x and player_y >= y:
        angle = 1.5 * math.pi + math.atan((x - player_x) / (player_y - y + 0.000001))
    else:
        angle = math.atan((y - player_y) / (x - player_x + 0.000001))
    return angle


@njit(fastmath=True)
def dist_calc(x, y, pl_pos):
    pl_x, pl_y = pl_pos
    dist = ((pl_x - x) ** 2 + (pl_y - y) ** 2) ** 0.5
    return dist
