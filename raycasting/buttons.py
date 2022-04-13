import pygame
from map import map_scale
from settings import *


class Button:
    def __init__(self, sc, width, height, x, y, function, text):
        self.sc = sc
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (x, y)
        self.message_size = height // 2
        self.function = function
        self.text = text

    def draw_button(self):
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.rect.x <= mouse_position[0] <= self.rect.bottomright[0]) and \
                (self.rect.y <= mouse_position[1] <= self.rect.bottomright[1]):
            pygame.draw.rect(self.sc, active_colour, self.rect)
            if click[0]:
                self.function()
        else:
            pygame.draw.rect(self.sc, not_active_colour, self.rect)

        self.texting(WHITE, 'arial', self.message_size, self.sc)

    def texting(self, text_colour, f_sys, f_size, surface):
        f_sys = pygame.font.SysFont(f_sys, f_size)
        sc_text = f_sys.render(self.text, True, text_colour)
        pos = sc_text.get_rect(center=self.rect.center)
        surface.blit(sc_text, pos)


# Pause_button
sc_pause = pygame.Surface((WIDTH, HEIGHT))
sc_pause.fill(DARKGREY)
sc_pause.set_alpha(128)


def game_pause(sc, bg_image, buttons):
    sc.blit(bg_image, (0, 0))
    sc.blit(sc_pause, (0, 0))
    for button in buttons:
        button.draw_button()

    pygame.display.flip()


# open map
def open_map(sc, bg_image, opened_map, opened_map_image, player_position, angle):
    sc.blit(bg_image, (0, 0))
    opened_map.blit(opened_map_image, (0, 0))
    map_x, map_y = player_position
    map_x, map_y = map_x // MAP_SCALE * map_scale, map_y // MAP_SCALE * map_scale

    # player om map
    pygame.draw.line(opened_map, YELLOW, (map_x, map_y), (map_x + 8 * map_scale * math.cos(angle),
                                                          map_y + 8 * map_scale * math.sin(angle)), int(1 * map_scale))
    pygame.draw.circle(opened_map, YELLOW, (int(map_x), int(map_y)), max(5 * map_scale, 5))

    map_rect = opened_map.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
    sc.blit(opened_map, map_rect)
    pygame.display.flip()
