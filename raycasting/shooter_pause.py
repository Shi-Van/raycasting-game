from player import *
from drawing import Button
sc_pause = pygame.Surface((100, 50))
sc_pause.fill(BLACK)
pause = False


def game_pause(sc):
    global pause
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.mouse.set_pos(WIDTH + 10, 0)
        pygame.mouse.set_visible(True)
        pause_button = Button(sc_pause, 100, 50, RED, BLUE)
        pause_button.draw_button(0, 0, 'PAUSE')
        sc.blit(sc_pause, (0, 0))
        pygame.display.flip()
