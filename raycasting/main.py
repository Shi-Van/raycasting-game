import pygame
from shooter_pause import game_pause
from settings import *
from player import Player
from drawing import *
from map import width_map, height_map
pygame.init()
pygame.display.set_caption("3d shooter")
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((width_map, height_map))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
pygame.mouse.set_visible(False)
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and paused:
            paused = False
            pygame.mouse.set_visible(False)
            pygame.mouse.get_rel()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_pause(sc)
            paused = True
    if not paused:
        player.movement()
        sc.fill(BLACK)
        drawing.background(player.angle)
        drawing.world(player.pos, player.angle)
        drawing.fps(clock)
        drawing.mini_map(player)
        drawing.compass(player.angle)
        pygame.display.flip()
        clock.tick()
