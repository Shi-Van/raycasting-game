from mobs import *


@njit(fastmath=True)
def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(sc, player_position, direction_angle, textures, mobs, worldmap):
    ox, oy = player_position
    xm, ym = mapping(ox, oy)
    cur_angle = direction_angle - HALF_FOV
    depth_h = depth_v = yv = xh = 0
    rays_depth = []
    new_walls = set()
    for ray in range(NUM_RAYS):
        values = ray_counting(xm, ox, ym, oy, ray, cur_angle, depth_h, depth_v, yv, xh, direction_angle, worldmap)
        rays_depth += [values[:-1]]
        if values[6] in worldmap:
            new_walls |= {values[6]}
        cur_angle += DELTA_ANGLE

    for mob in mobs:
        angle = (mob.mob_angle(player_position) - (direction_angle - HALF_FOV)) % (2 * math.pi)
        if 0 <= angle <= FOV + 200 * DELTA_ANGLE:
            ray = angle / DELTA_ANGLE
            dist = mob.mob_distance(player_position)
            dist *= math.cos(direction_angle - cur_angle)
            mob_height = int((PROJ_COEF / 1.5) / (dist + 0.00001))
            rays_depth += [(dist, mob.type, mob_height, ray, mob)]
        elif - 200 * DELTA_ANGLE <= angle - 2 * math.pi:
            ray = (angle - 2 * math.pi) / DELTA_ANGLE
            dist = mob.mob_distance(player_position)
            dist *= math.cos(direction_angle - cur_angle)
            mob_height = int((PROJ_COEF / 1.5) / (dist + 0.00001))
            rays_depth += [(dist, mob.type, mob_height, ray, mob)]

    rays_depth.sort(reverse=True)
    screen_blit(rays_depth, textures, sc)
    return new_walls


@njit(fastmath=True)
def ray_counting(xm, ox, ym, oy, ray, cur_angle, depth_h, depth_v, yv, xh, direction_angle, worldmap):
    sin_a = math.sin(cur_angle)
    cos_a = math.cos(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = cos_a if cos_a else 0.000001
    texture_hor = texture_ver = 1

    # verticals
    x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
    for _ in range(0, view_range, TILE):
        depth_v = (x - ox) / cos_a
        yv = oy + depth_v * sin_a
        tile_v = mapping(x + dx, yv)
        if tile_v in worldmap:
            texture_ver = worldmap[tile_v]
            break
        x += dx * TILE

    # horizontals
    y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
    for _ in range(0, view_range, TILE):
        depth_h = (y - oy) / sin_a
        xh = ox + depth_h * cos_a
        tile_h = mapping(xh, y + dy)
        if tile_h in worldmap:
            texture_hor = worldmap[tile_h]
            break
        y += dy * TILE

    # projection
    depth, offset, texture, tile = (depth_v, yv, texture_ver, tile_v) if depth_v < depth_h \
        else (depth_h, xh, texture_hor, tile_h)
    offset = int(offset) % TILE
    depth = depth if depth else 0.000001
    depth *= math.cos(direction_angle - cur_angle)
    proj_height = int(PROJ_COEF / depth)

    return depth, 0, texture, offset, proj_height, ray, tile


def screen_blit(rays_depth, textures, sc):
    for game_object in rays_depth:
        if game_object[1] == 0:
            dist, wall_type, texture, offset, proj_height, ray = game_object
            if proj_height >= HEIGHT:
                offset2 = (TEXTURE_HEIGHT / (proj_height / HEIGHT))
                proj_height = HEIGHT
                wall_vertical = textures[texture].subsurface(offset * TEXTURE_SCALE, (TEXTURE_HEIGHT - offset2) // 2,
                                                             TEXTURE_SCALE, offset2)
                wall_vertical = pygame.transform.scale(wall_vertical, (SCALE, proj_height))
            else:
                wall_vertical = pygame.transform.scale(
                    textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE,
                                                 TEXTURE_HEIGHT), (SCALE, proj_height))
            sc.blit(wall_vertical, (ray * SCALE, HALF_HEIGHT - proj_height // 2))
        else:
            dist, mob_type, mob_height, ray, mob = game_object
            mob_im = pygame.transform.scale(mob.image, (mob_height, mob_height))
            mob_rect = mob_im.get_rect()
            mob_rect.center = (ray * SCALE, HALF_HEIGHT)
            sc.blit(mob_im, mob_rect)
