import pygame
from settings import *
pygame.mixer.init()


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
                # pygame.mixer.music.load('music\computer-keyboard-button-press-release_m1pp3tnd.mp3')
                # pygame.mixer.music.play(1)
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


# button lists
win_buttons = []
fail_buttons = []
buttons = []
