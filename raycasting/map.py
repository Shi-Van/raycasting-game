from settings import *
import pygame

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWW',
    'W W               W   W',
    'W                   W W',
    'W                     W',
    'WW                       WW',
    'W      WWW            W',
    'W               W  W  W',
    'WWWWWWWWWWWWWWWWWWWWWWW'
]


class Platform_minimap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, MAP_TILE, MAP_TILE)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, TILE, TILE)

world_map = set()
# mini_map = pygame.sprite.Group()
mini_map = []
function_map = []
for j, row in enumerate(text_map):
    function_map += [list(row)]
    for i, char in enumerate(row):
        if char == 'W':
            pf_minimap = Platform_minimap(i * MAP_TILE, j * MAP_TILE)
            pf = Platform(i * TILE, j * TILE)
            world_map.add((i * TILE, j * TILE))
            function_map[j][i] = pf
            mini_map.append(pf_minimap)

width_map = len(row) * MAP_TILE
height_map = len(text_map) * MAP_TILE
for x in function_map:
    print(x)
