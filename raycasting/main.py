import pygame

from mobs import Mobs
from player import Player
from drawing import *
from buttons import *
pygame.init()
pygame.display.set_caption("3d shooter")
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
bg_image = sc.copy()
sc_map = pygame.Surface((MAP_SIZE, MAP_SIZE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
pygame.mouse.set_visible(False)
paused = False
mob = Mobs((500, 500), 1)
mobs = [mob]


# buttons functions
def pause_button_active():
    global paused
    paused = False
    pygame.mouse.set_visible(False)
    pygame.mouse.get_rel()


def exit_button_active():
    exit()


buttons = []
# pause_button
buttons += [Button(sc, 300, 100, WIDTH // 2, HEIGHT // 2, pause_button_active, 'CONTINUE')]
# exit_button
buttons += [Button(sc, 50, 50, WIDTH - 50, 50, exit_button_active, 'X')]


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
        game_pause(sc, bg_image, buttons)
    else:
        player.movement()
        sc.fill(BLACK)
        drawing.background(player.angle)
        drawing.world(player.pos, player.angle, mobs)
        drawing.fps(clock)
        drawing.mini_map(player)
        drawing.compass(player.angle)
        pygame.display.flip()
        clock.tick(FPS)