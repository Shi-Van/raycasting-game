from buttons import *
sc_pause = pygame.Surface((WIDTH, HEIGHT))
sc_pause.fill(DARKGREY)
sc_pause.set_alpha(128)


def game_pause(sc, bg_image, pause_button):
    pygame.mouse.set_visible(True)
    sc.blit(bg_image, (0, 0))
    sc.blit(sc_pause, (0, 0))
    pause_button.draw_button('PAUSE')
    pygame.display.flip()
