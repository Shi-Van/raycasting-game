from player import *
sc_pause = pygame.Surface((100, 50))
sc_pause.fill(BLACK)
pause = False
from drawing import Button

def game_pause():
    global pause
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             print(3)
    #             if event.key == pygame.K_ESCAPE and not pause:
    #                 pause = True
    #             elif event.key == pygame.K_ESCAPE:
    #                 pause = False
    #     if pause:
    #         pygame.mouse.set_visible(True)
    #         sc.fill(RED)
    #         pygame.display.flip()
    #     else:
    #         pygame.mouse.set_visible(False)
    #         break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.mouse.set_pos(WIDTH + 10, 0)
        pygame.mouse.set_visible(True)
        pause_button = Button(sc_pause, 100, 50, RED, BLUE)
        pause_button.draw_button(0, 0, 'PAUSE')
        sc.blit(sc_pause())
        pygame.display.flip()