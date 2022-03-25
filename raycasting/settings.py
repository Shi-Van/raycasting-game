import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)
view_range = 2300
sensitivity = 800

# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 400
while WIDTH % NUM_RAYS != 0:
    NUM_RAYS -= 10
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (HALF_WIDTH + 100, HALF_HEIGHT)
player_angle = 0
player_speed_system = 3
rotation_speed = 0.005
player_width = 25
player_half_width = 12.5
cube_angle_width = player_width // 3
sens_koef = sensitivity / 800 ** 2

TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)

ind_hit = [(1, 1), (-1, -1), (0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1)]
