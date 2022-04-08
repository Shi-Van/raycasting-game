from settings import *
import pygame


class Mobs(pygame.sprite.Sprite):
    def __init__(self, position, mob_type):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = position
        self.mob_type = mob_type
        self.image = pygame.image.load('images/воловик.png').convert()

    def mob_distance(self, pl_pos):
        pl_x, pl_y = pl_pos
        dist = ((pl_x - self.x)**2 + (pl_y - self.y)**2)**0.5
        return dist

    def mob_angle(self, player_position):
        player_x, player_y = player_position
        if player_x >= self.x and player_y <= self.y:
            angle = math.pi - math.atan((player_y - self.y) / (self.x - player_x + 0.000001))
        elif player_x >= self.x and player_y >= self.y:
            angle = math.pi + math.atan((player_y - self.y) / (player_x - self.x + 0.000001))
        elif player_x <= self.x and player_y >= self.y:
            angle = 1.5 * math.pi + math.atan((self.x - player_x) / (player_y - self.y + 0.000001))
        else:
            angle = math.atan((self.y - player_y) / (self.x - player_x + 0.000001))
        return angle
