from settings import *
import pygame

text_map = [
    '11111111111111111111111',
    '1 2               2   1',
    '1                 2   1',
    '1                     1',
    '1                     1',
    '1                     1',
    '1                     1',
    '1                     1',
    '1                     1',
    '12                    1',
    '1      222            1',
    '1               2  2  1',
    '11111111111111111111111'
]


class PlatformMinimap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, MAP_TILE, MAP_TILE)


world_map = {}
mini_map = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != ' ':
            pf_minimap = PlatformMinimap(i * MAP_TILE, j * MAP_TILE)
            mini_map.append(pf_minimap)
            world_map[(i * TILE, j * TILE)] = char


mini_map_texture = pygame.Surface((MAP_SIZE, MAP_SIZE))

width_map = len(text_map[0]) * MAP_TILE
height_map = len(text_map) * MAP_TILE

map_image = pygame.Surface((width_map, height_map))
map_image.fill(DARKGREY)
for platform in mini_map:
    pygame.draw.rect(map_image, LIGHTGREY, (platform.rect.x, platform.rect.y, MAP_TILE, MAP_TILE))
