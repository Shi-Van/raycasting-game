from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32

with open('map.txt', 'r') as m:
    text_map = m.readlines()

with open('map2.txt', 'r') as m:
    text_map2 = m.readlines()

class PlatformMinimap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, MAP_TILE, MAP_TILE)


# world_map = {}
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
world_map2 = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = []
mini_map2 = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row[:-1]):
        if char != ' ':
            pf_minimap = PlatformMinimap(i * MAP_TILE, j * MAP_TILE)
            mini_map.append(pf_minimap)
            world_map[(i * TILE, j * TILE)] = int32(char)

for j, row in enumerate(text_map2):
    for i, char in enumerate(row[:-1]):
        if char != ' ':
            pf_minimap2 = PlatformMinimap(i * MAP_TILE, j * MAP_TILE)
            mini_map2.append(pf_minimap2)
            world_map2[(i * TILE, j * TILE)] = int32(char)

mini_map_texture = pygame.Surface((MAP_SIZE, MAP_SIZE))

width_map = (len(text_map[0]) - 1) * MAP_TILE
height_map = len(text_map) * MAP_TILE

map_image = pygame.Surface((width_map, height_map))
map_image.fill(DARKGREY)
for platform in mini_map:
    pygame.draw.rect(map_image, LIGHTGREY, (platform.rect.x, platform.rect.y, MAP_TILE, MAP_TILE))

map_scale = min(WIDTH / (width_map * 2), HEIGHT / (height_map * 2))
opened_map = pygame.Surface((width_map * map_scale, height_map * map_scale))
opened_map_image = pygame.Surface((width_map * map_scale, height_map * map_scale))
opened_map_image.fill(DARKGREY)
