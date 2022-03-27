from player import *
from drawing import Button
sc_pause = pygame.Surface((WIDTH, HEIGHT))
sc_pause.fill(DARKGRAY)
sc_pause.set_alpha(128)



def game_pause(sc, bg_image):
    global pause
    pygame.mouse.set_visible(True)
    pause_button = Button(sc, 500, 200, RED, BLUE)
    sc.blit(bg_image, (0, 0))
    sc.blit(sc_pause, (0, 0))
    pause_button.draw_button(WIDTH // 2 - 250, HEIGHT // 2 - 100, 'PAUSE')
    pygame.display.flip()
