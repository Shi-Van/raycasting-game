from player import *
sc_pause = pygame.Surface((WIDTH, HEIGHT))
pause = False


def game_pause():
    global pause
    while True:
        for event in pygame.event.get(p):
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE and not pause:
                    pause = True
                elif event.key == K_ESCAPE:
                    pause = False
        if pause:
            pygame.mouse.set_visible(True)
            sc.fill(RED)
            pygame.display.flip()
        else:
            pygame.mouse.set_visible(False)
            break







