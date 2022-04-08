from settings import *
import pygame


class Mobs(pygame.sprite.Sprite):
    def __init__(self, position, mtype):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = position
        self.mob_type = mtype
        self.image = pygame.image.load('images/авыва.png').convert()

    def mob_distance(self, pl_pos):
        pl_x, pl_y = pl_pos
        dist = ((pl_x - self.x)**2 + (pl_y - self.y)**2)**0.5
        return dist

    def mob_angle(self, player_position):
        if player_position[0] >= self.x and player_position[1] <= self.y:
            angle = math.pi - math.atan((player_position[1] - self.y) / (self.x - player_position[0] + 0.000001))
        elif player_position[0] >= self.x and player_position[1] >= self.y:
            angle = math.pi + math.atan((player_position[1] - self.y) / (player_position[0] - self.x + 0.000001))
        elif player_position[0] <= self.x and player_position[1] >= self.y:
            angle = (math.pi * (3 / 2)) + math.atan((self.x - player_position[0]) / (player_position[1] - self.y + 0.000001))
        elif player_position[0] <= self.x and player_position[1] <= self.y:
            angle = math.atan((self.y - player_position[1]) / (self.x - player_position[0] + 0.000001))
        return angle
