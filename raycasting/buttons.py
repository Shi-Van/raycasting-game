import pygame
from settings import *


class Button:
    def __init__(self, sc, width, hieght, x, y):
        self.sc = sc
        self.rect = pygame.Rect(x, y, width, hieght)
        self.rect.center = (x, y)
        self.message_size = hieght // 2

    def draw_button(self, message, action_act=None):
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.rect.x <= mouse_position[0] <= self.rect.bottomright[0]) and (self.rect.y <= mouse_position[1] <= self.rect.bottomright[1]):
            pygame.draw.rect(self.sc, active_colour, self.rect)
            if click[0] and action_act is not None:
                action_act()
        else:
            pygame.draw.rect(self.sc, not_active_colour, self.rect)

        self.texting(message, WHITE, 'arial', self.message_size, self.sc)

    def texting(self, message, text_colour, f_sys, f_size, surface):
        f_sys = pygame.font.SysFont(f_sys, f_size)
        sc_text = f_sys.render(message, True, text_colour)
        pos = sc_text.get_rect(center=self.rect.center)
        surface.blit(sc_text, pos)

# Shooter_Pause
sc_pause = pygame.Surface((WIDTH, HEIGHT))
sc_pause.fill(DARKGREY)
sc_pause.set_alpha(128)


def game_pause(sc, bg_image, pause_button, action):
    pygame.mouse.set_visible(True)
    sc.blit(bg_image, (0, 0))
    sc.blit(sc_pause, (0, 0))
    pause_button.draw_button('PAUSE', action)
    pygame.display.flip()



