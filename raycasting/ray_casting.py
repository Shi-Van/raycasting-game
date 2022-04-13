from map import world_map
from mobs import *


@njit(fastmath=True)
def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(sc, player_position, direction_angle, textures, mobs):
    ox, oy = player_position
    xm, ym = mapping(ox, oy)
    cur_angle = direction_angle - HALF_FOV
    depth_h = depth_v = yv = xh = 0
    rays_depth = []
    for ray in range(NUM_RAYS):
        rays_depth += [
            ray_counting(xm, ox, ym, oy, ray, cur_angle, depth_h, depth_v, yv, xh, direction_angle)]
        cur_angle += DELTA_ANGLE

    for mob in mobs:
        angle = (mob.mob_angle(player_position) - (direction_angle - HALF_FOV)) % (2 * math.pi)
        if 0 <= angle <= FOV:
            ray = angle / DELTA_ANGLE
            dist = mob.mob_distance(player_position)
            mob_height = int((PROJ_COEF / 1.5) / (dist + 0.00001))
            rays_depth += [(dist, mob.type, mob_height, ray, mob)]

    rays_depth.sort(reverse=True)
    screen_blit(rays_depth, textures, sc)


# @njit(fastmath=True)
def ray_counting(xm, ox, ym, oy, ray, cur_angle, depth_h, depth_v, yv, xh, direction_angle):
    sin_a = math.sin(cur_angle)
    cos_a = math.cos(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = cos_a if cos_a else 0.000001
    texture_hor = texture_ver = '1'

    # verticals
    x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
    for _ in range(0, view_range, TILE):
        depth_v = (x - ox) / cos_a
        yv = oy + depth_v * sin_a
        tile_v = mapping(x + dx, yv)
        if tile_v in world_map:
            texture_ver = world_map[tile_v]
            break
        x += dx * TILE

    # horizontals
    y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
    for _ in range(0, view_range, TILE):
        depth_h = (y - oy) / sin_a
        xh = ox + depth_h * cos_a
        tile_h = mapping(xh, y + dy)
        if tile_h in world_map:
            texture_hor = world_map[tile_h]
            break
        y += dy * TILE

    # projection
    depth, offset, texture = (depth_v, yv, texture_ver) if depth_v < depth_h else (depth_h, xh, texture_hor)
    offset = int(offset) % TILE
    depth = depth if depth else 0.000001
    depth *= math.cos(direction_angle - cur_angle)
    proj_height = int(PROJ_COEF / depth)

    return depth, 0, texture, offset, proj_height, ray


def screen_blit(rays_depth, textures, sc):
    for game_object in rays_depth:
        if game_object[1] == 0:
            dist, wall_type, texture, offset, proj_height, ray = game_object
            try:
                wall_vertical = pygame.transform.scale(
                    textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE,
                                                 TEXTURE_HEIGHT), (SCALE, proj_height))
                sc.blit(wall_vertical, (ray * SCALE, HALF_HEIGHT - proj_height // 2))
            except ValueError:
                print(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        else:
            dist, mob_type, mob_height, ray, mob = game_object
            mob_im = pygame.transform.scale(mob.image, (mob_height, mob_height))
            mob_rect = mob_im.get_rect()
            mob_rect.center = (ray * SCALE, HALF_HEIGHT)
            sc.blit(mob_im, mob_rect)
