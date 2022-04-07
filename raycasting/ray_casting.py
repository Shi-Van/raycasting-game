import pygame
from settings import *
from map import world_map, view_range
from threading import Thread


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(sc, player_pos, player_angle, texture):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    depth_h = depth_v = yv = xh = 0
    for ray in range(NUM_RAYS):
        # th = Thread(target=ray_counting, args=(xm, ox, ym, oy, ray, sc, texture, cur_angle, depth_h, depth_v, yv, xh, player_angle))
        # th.start()
        ray_counting(xm, ox, ym, oy, ray, sc, texture, cur_angle, depth_h, depth_v, yv, xh, player_angle)
        cur_angle += DELTA_ANGLE
    # for mob in mobs:
    #     angle = (mob.mob_angle(player_pos) - player_angle) % (2 * math.pi)
    #     if 0 <= angle <= FOV:
    #         ray = angle // DELTA_ANGLE
    #         dist = mob.mob_distance(player_pos)
    #         mob_height = int((PROJ_COEF / 1.5) / dist)
    #         pygame.draw.rect(sc, BLUE, (ray * SCALE - mob_height // 2, HALF_HEIGHT - mob_height // 2, (ray * SCALE + mob_height // 2, HALF_HEIGHT + mob_height // 2)))


def ray_counting(xm, ox, ym, oy, ray, sc, texture, cur_angle, depth_h, depth_v, yv, xh, player_angle):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for _ in range(0, view_range, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            if mapping(x + dx, yv) in world_map:
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for _ in range(0, view_range, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            if mapping(xh, y + dy) in world_map:
                break
            y += dy * TILE

        # projection
        depth, offset = (depth_v, yv) if depth_v < depth_h else (depth_h, xh)
        offset = int(offset) % TILE
        depth = depth if depth else 0.000001
        depth *= math.cos(player_angle - cur_angle)
        proj_height = int(PROJ_COEF / depth)

        wall_vertical = pygame.transform.scale(texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE,
                                                                  TEXTURE_HEIGHT), (SCALE, proj_height))
        sc.blit(wall_vertical, (ray * SCALE, HALF_HEIGHT - proj_height // 2))
