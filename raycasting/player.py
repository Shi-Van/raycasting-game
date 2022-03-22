from settings import *
from map import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = player_pos
        self.angle = player_angle
        self.side = player_width * 2
        self.rect = pygame.Rect(*player_pos, self.side, self.side)

    @property
    def pos(self):
        return self.rect.centerx, self.rect.centery

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        delt_x = delt_y = 0
        cube_x_pos, cube_y_pos = int(self.x // TILE * TILE), int(self.y // TILE * TILE)

        if keys[pygame.K_LSHIFT]:
            player_speed = 3
        elif keys[pygame.K_CAPSLOCK]:
            player_speed = 0.5
        else:
            player_speed = 1.5

        if keys[pygame.K_w]:
            delt_x += player_speed * cos_a
            delt_y += player_speed * sin_a
        if keys[pygame.K_s]:
            delt_x += -player_speed * cos_a
            delt_y += -player_speed * sin_a
        if keys[pygame.K_a]:
            delt_x += player_speed * sin_a
            delt_y += -player_speed * cos_a
        if keys[pygame.K_d]:
            delt_x += -player_speed * sin_a
            delt_y += player_speed * cos_a

        rel = pygame.mouse.get_rel()
        pygame.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
        self.angle += rel[0] * sens_koef

        if delt_y <= 0:
            if (cube_x_pos, cube_y_pos - TILE) in world_map:
                if cube_y_pos + player_width > self.y + delt_y:
                    delt_y = cube_y_pos + player_width - self.y
        if delt_x < 0:
            if (cube_x_pos - TILE, cube_y_pos) in world_map:
                if cube_x_pos + player_width > self.x + delt_x:
                    delt_x = cube_x_pos + player_width - self.x
        if delt_y > 0:
            if (cube_x_pos, cube_y_pos + TILE) in world_map:
                if cube_y_pos + TILE - player_width < self.y + delt_y:
                    delt_y = self.y - cube_y_pos - TILE + player_width
        if delt_x > 0:
            if (cube_x_pos + TILE, cube_y_pos) in world_map:
                if cube_x_pos + TILE - player_width < self.x + delt_x:
                    delt_x = self.x - cube_x_pos - TILE + player_width

        if ((self.x + delt_x + player_half_width) // TILE * TILE, (self.y + delt_y + player_half_width) // TILE * TILE) in world_map \
            or ((self.x + delt_x + player_half_width) // TILE * TILE, (self.y + delt_y - player_half_width) // TILE * TILE) in world_map \
            or ((self.x + delt_x - player_half_width) // TILE * TILE, (self.y + delt_y + player_half_width) // TILE * TILE) in world_map \
            or ((self.x + delt_x - player_half_width) // TILE * TILE, (self.y + delt_y - player_half_width) // TILE * TILE) in world_map:
            delt_x = delt_y = 0

        self.x += delt_x
        self.y += delt_y
        self.rect.centerx = self.x
        self.rect.centery = self.y


