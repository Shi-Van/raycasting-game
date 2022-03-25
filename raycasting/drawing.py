import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map, height_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_compass1 = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_compass2 = pygame.font.SysFont('Arial', 20, bold=True)
        self.texture = pygame.image.load('images/2.png').convert()
        self.texture = pygame.transform.scale(self.texture, (1200, 1200))
        self.sky_texture = pygame.image.load('images/sky.jpg').convert()
        self.sky_texture = pygame.transform.scale(self.sky_texture, (WIDTH, HEIGHT // 2))

    def background(self, angle):
        sky_pos = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.sky_texture, (sky_pos, 0))
        self.sc.blit(self.sky_texture, (sky_pos - WIDTH, 0))
        self.sc.blit(self.sky_texture, (sky_pos + WIDTH, 0))
        pygame.draw.rect(self.sc, GREEN, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.texture)

    def compass(self, angle):
        dir = str(int(math.degrees(angle)) % 360)
        dir1 = str(int(math.degrees(angle) - 15) % 360)
        dir2 = str(int(math.degrees(angle) + 15) % 360)
        render = self.font_compass1.render(dir, 1, BLACK)
        self.sc.blit(render, (WIDTH // 2, 5))
        render = self.font_compass2.render(dir1, 1, BLACK)
        self.sc.blit(render, (WIDTH // 2 - 60, 5 + 10))
        render = self.font_compass2.render(dir2, 1, BLACK)
        self.sc.blit(render, (WIDTH // 2 + 90, 5 + 10))

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.rect.centerx // MAP_SCALE, player.rect.centery // MAP_SCALE

        for platform in mini_map:
            pygame.draw.rect(self.sc_map, PURPLE, platform.rect)

        # player om mini map
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 6 * math.cos(player.angle),
                                                               map_y + 6 * math.sin(player.angle)), 3)
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 8 * math.cos(player.angle),
                                                               map_y + 8 * math.sin(player.angle)), 1)
        pygame.draw.circle(self.sc_map, YELLOW, (int(map_x), int(map_y)), 5)
        self.sc.blit(self.sc_map, (0, HEIGHT - height_map))
