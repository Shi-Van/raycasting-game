import pygame
from settings import *
from ray_casting import ray_casting
from map import map_image, map_scale, opened_map_image, opened_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_compass1 = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_compass2 = pygame.font.SysFont('Arial', 20, bold=True)
        self.textures = {1: pygame.image.load('images/remn_wall7.png').convert(),
                         2: pygame.image.load('images/remn_wall1.png').convert(),
                         3: pygame.image.load('images/finish.JPG').convert(),
                         4: pygame.image.load('images/snake_door.jpg').convert()}
        for i in self.textures:
            self.textures[i] = pygame.transform.scale(self.textures[i], (1200, 1200))
        self.sky_texture = pygame.image.load('images/sky1.jpg').convert()
        self.sky_texture = pygame.transform.scale(self.sky_texture, (WIDTH, HEIGHT // 2))
        self.seen_walls = set()
        self.opened_map_image = opened_map_image
        self.map_rect = opened_map.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))

    def background(self, angle):
        sky_pos = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.sky_texture, (sky_pos, 0))
        self.sc.blit(self.sky_texture, (sky_pos - WIDTH, 0))
        self.sc.blit(self.sky_texture, (sky_pos + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGREY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_position, dir_angle, mobs, world_map):
        new_walls = ray_casting(self.sc, player_position, dir_angle, self.textures, mobs, world_map)
        new_walls -= self.seen_walls
        x, y = player_position[0] // TILE - 2, player_position[1] // TILE - 2
        for j in range(y, y + 4):
            for i in range(x, x + 4):
                if (i * TILE, j * TILE) in world_map and (i * TILE, j * TILE) not in self.seen_walls:
                    new_walls |= {(i * TILE, j * TILE)}
        self.opened_map_update(new_walls)
        self.seen_walls |= new_walls

    def compass(self, angle):
        dir0 = str(int(math.degrees(angle)) % 360)
        dir1 = str(int(math.degrees(angle) - 15) % 360)
        dir2 = str(int(math.degrees(angle) + 15) % 360)
        render = self.font_compass1.render(dir0, True, BLACK)
        self.sc.blit(render, (WIDTH // 2, 5))
        render = self.font_compass2.render(dir1, True, BLACK)
        self.sc.blit(render, (WIDTH // 2 - 60, 5 + 10))
        render = self.font_compass2.render(dir2, True, BLACK)
        self.sc.blit(render, (WIDTH // 2 + 90, 5 + 10))

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, True, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(LIGHTGREY)
        map_x, map_y = player.rect.centerx // MAP_SCALE, player.rect.centery // MAP_SCALE
        x_offset = map_x - HALF_MAP_SIZE
        y_offset = map_y - HALF_MAP_SIZE
        map_x = map_y = HALF_MAP_SIZE

        self.sc_map.blit(map_image, (-x_offset, -y_offset))

        # player om mini map
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 6 * math.cos(player.angle),
                                                               map_y + 6 * math.sin(player.angle)), 3)
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 8 * math.cos(player.angle),
                                                               map_y + 8 * math.sin(player.angle)), 1)
        pygame.draw.circle(self.sc_map, YELLOW, (int(map_x), int(map_y)), 5)
        self.sc.blit(self.sc_map, (WIDTH - MAP_SIZE - 10, 10))

    def opened_map_update(self, new_walls):
        for platform in new_walls:
            pygame.draw.rect(self.opened_map_image, LIGHTGREY, (platform[0] // TILE * MAP_TILE * map_scale,
                                                                platform[1] // TILE * MAP_TILE * map_scale,
                                                                MAP_TILE * map_scale, MAP_TILE * map_scale))

    def open_map(self, bg_image, player_position):
        self.sc.blit(bg_image, (0, 0))
        opened_map.blit(self.opened_map_image, (0, 0))
        map_x, map_y = player_position
        map_x, map_y = map_x // MAP_SCALE * map_scale, map_y // MAP_SCALE * map_scale

        # player om map
        pygame.draw.circle(opened_map, YELLOW, (int(map_x), int(map_y)), max(5 * map_scale, 5))

        self.sc.blit(opened_map, self.map_rect)
        pygame.display.flip()
