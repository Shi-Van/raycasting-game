from player import *
from drawing import Button
sc_pause = pygame.Surface((WIDTH, HEIGHT))
sc_pause.fill(DARKGRAY)
sc_pause.set_alpha(128)



def game_pause(sc):
    global pause
    pygame.mouse.set_visible(True)
    pause_button = Button(sc_pause, 500, 200, RED, BLUE)
    pause_button.draw_button(WIDTH // 2 - 250, HEIGHT // 2 - 100, 'PAUSE')
    sc.blit(sc_pause, (0, 0))
    pygame.display.flip()
