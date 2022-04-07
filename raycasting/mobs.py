from settings import *
import pygame

class Mobs(pygame.sprite.Sprite):
    def __init__(self, position, mtype):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = position
        self.mob_type = mtype

    def mob_distance(self, pl_pos):
        pl_x, pl_y = pl_pos
        dist = ((pl_x - self.x)**2 + (pl_y - self.y)**2)**1 // 2
        return dist

    def mob_angle(self, player_pos):
        if player_pos[0] >= self.x and player_pos[1] <= self.y:
            angle = 2 * math.pi - math.atan((player_pos[1] - self.y) / (self.x - player_pos[0]))
        elif player_pos[0] >= self.x and player_pos[1] > self.y:
            angle = math.pi + math.atan((player_pos[1] - self.y) / (player_pos[0] - self.x))
        elif player_pos[0] < self.x and player_pos[1] > self.y:
            angle = (math.pi // 2) + math.atan((self.x - player_pos[0]) / (self.y - player_pos[1]))
        elif player_pos[0] < self.x and player_pos[1] < self.y:
            angle = math.atan((self.y - player_pos[1]) / (self.x - player_pos[0]))
        return angle
