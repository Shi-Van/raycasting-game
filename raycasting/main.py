import pygame
from player import Player
from drawing import *
from buttons import *
pygame.init()
pygame.display.set_caption("3d shooter")
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
sc_map = pygame.Surface((MAP_SIZE, MAP_SIZE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
pygame.mouse.set_visible(False)
paused = False
# buttons
pause_button = Button(sc, 300, 100, WIDTH // 2, HEIGHT // 2)
exit_button = Button(sc, 50, 50, WIDTH - 50, 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and paused:
            paused = False
            pygame.mouse.get_rel()
            pygame.mouse.set_visible(False)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paused = True
            bg_image = sc.copy()
            sc.blit(sc_pause, (0, 0))
    if paused:
        game_pause(sc, bg_image, pause_button, pause_button_active, exit_button, exit_button_active)
    else:
        player.movement()
        sc.fill(BLACK)
        drawing.background(player.angle)
        drawing.world(player.pos, player.angle)
        drawing.fps(clock)
        drawing.mini_map(player)
        drawing.compass(player.angle)
        pygame.display.flip()
        clock.tick(FPS)
