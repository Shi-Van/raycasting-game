from player import *
from drawing import Button
sc_pause = pygame.Surface((WIDTH, HEIGHT))
sc_pause.fill(DARKGRAY)
sc_pause.set_alpha(1)



def game_pause(sc):
    global pause
    pygame.mouse.set_visible(True)
    pause_button = Button(sc_pause, 500, 200, RED, BLUE)
    # position = pause_button.get_rect(center=(surf_weight // 2, surf_height // 2))
    pause_button.draw_button(WIDTH // 2, HEIGHT // 2, 'PAUSE')
    sc.blit(sc_pause, (0, 0))
    pygame.display.flip()
