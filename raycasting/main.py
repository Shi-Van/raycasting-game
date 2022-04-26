from mobs import Mobs
from player import Player
from drawing import *
from buttons import *
from map import opened_map, world_map

pygame.init()
pygame.display.set_caption("3d shooter")
# x = pygame.image.load('images/game-1.png').convert()
# sc.blit(x, (0, 0))
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
bg_image = sc.copy()
sc_map = pygame.Surface((MAP_SIZE, MAP_SIZE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
pygame.mouse.set_visible(False)
paused = False
map_open = False
mob = Mobs((3000, 4000), 1)
mobs = [mob]
pause_music = False
play_music = False
Continue = 0
vol = 1.0
def Exit():
    exit()
win_buttons = []

# buttons functions
def pause_button_active():
    global paused
    paused = False
    pygame.mouse.set_visible(False)
    pygame.mouse.get_rel()

def exit_button_active():
    exit()


#win!
def win():
    pygame.mixer.music.load('music\gta-san-andreas-opening-intro.mp3')
    pygame.mixer.music.play(1)
    for win_button in win_buttons:
        win_button.draw_button()
    pygame.display.flip()
    pygame.mouse.set_visible(True)




buttons = []
# pause_button
buttons += [Button(sc, 300, 100, WIDTH // 2, HEIGHT // 2, pause_button_active, 'CONTINUE')]
# exit_button
buttons += [Button(sc, 50, 50, WIDTH - 50, 50, exit_button_active, 'X')]
#win_button
win_buttons += [Button(sc, 600, 200, WIDTH // 2, HEIGHT // 2, Exit, 'YOU WIN!!!')]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # map screen
        if 8025 <= player.pos[0] <= 8175 and 125 <= player.pos[1] <= 310:
            win()
        elif event.type == pygame.KEYDOWN and map_open and (event.key == pygame.K_m or event.key == pygame.K_ESCAPE):
            map_open = False
            pygame.mouse.get_rel()
            pygame.mouse.set_visible(False)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            print(player.pos)
            map_open = True
            bg_image = sc.copy()
            pygame.mouse.set_visible(True)
        # pause screen
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and paused:
            paused = False
            pygame.mouse.get_rel()
            pygame.mouse.set_visible(False)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paused = True
            bg_image = sc.copy()
            pygame.mouse.set_visible(True)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            vol -= 0.1
            pygame.mixer.music.set_volume(vol)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            vol += 0.1
            pygame.mixer.music.set_volume(vol)
    if not play_music and not paused:
        pygame.mixer.music.load('music\doom.mp3')
        pygame.mixer.music.play(1)
        play_music = True
    if paused and not pause_music:
        Continue = pygame.mixer.music.get_pos()
        pygame.mixer.music.pause()
        pygame.mixer.music.load('music\Alexander Nakarada - Chase.mp3')
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_pos(4.38)
        play_music = False
    if not paused and pause_music:
        pause_music = False
        pygame.mixer.music.pause()
    if paused:
        game_pause(sc, bg_image, buttons)
        pause_music = True

    elif map_open:
        drawing.open_map(bg_image, opened_map, player.pos, player.angle)
    else:
        pygame.mixer.music.unpause()
        player.movement(world_map)
        sc.fill(BLACK)
        drawing.background(player.angle)
        drawing.world(player.pos, player.angle, mobs, world_map)
        drawing.fps(clock)
        drawing.mini_map(player)
        drawing.compass(player.angle)
        pygame.display.flip()
        clock.tick(FPS)
