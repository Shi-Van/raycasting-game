from mobs import Mobs, CMobs
from player import Player
from drawing import *
from buttons import *
from map import world_map, world_map2
from snake_quest import *
pygame.init()
pygame.display.set_caption("3d shooter")
# x = pygame.image.load('images/game-1.png').convert()
# sc.blit(x, (0, 0))
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
sc.fill((0, 100, 0))
bg_image = sc.copy()
sc_map = pygame.Surface((MAP_SIZE, MAP_SIZE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
pygame.mouse.set_visible(False)
paused = False
map_open = False
mob = Mobs((2900, 4100), 1)
mob2 = CMobs((600, 6200), 1)
# mobs = [mob, mob2]
mobs = []
pause_music = False
play_music = False
Continue = False
vol = 1.0
kill = False
First = True


# buttons functions
def pause_button_active():
    global paused
    paused = False
    pygame.mouse.set_visible(False)
    pygame.mouse.get_rel()


def exit_button_active():
    exit()


# win/fail function
def win():
    for win_button in win_buttons:
        win_button.draw_button()
    pygame.display.flip()
    pygame.mouse.set_visible(True)


def fail():
    for fail_button in fail_buttons:
        fail_button.draw_button()
    pygame.display.flip()
    pygame.mouse.set_visible(True)


buttons = []
# pause_button
buttons += [Button(sc, 300, 100, WIDTH // 2, HEIGHT // 2, pause_button_active, 'CONTINUE')]
# exit_button
buttons += [Button(sc, 50, 50, WIDTH - 50, 50, exit_button_active, 'X')]
# win_button
win_buttons += [Button(sc, 600, 200, WIDTH // 2, HEIGHT // 2, exit_button_active, 'YOU WIN!!!')]
# fail_button
fail_buttons += [Button(sc, 600, 200, WIDTH // 2, HEIGHT // 2, exit_button_active, 'WASTED')]
fail_buttons += [Button(sc, 50, 50, WIDTH - 50, 50, exit_button_active, 'X')]
while True:
    # click tracking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # map screen
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

        elif 4695 <= player.pos[0] <= 4795 and 375 <= player.pos[1] <= 475 and event.type == pygame.KEYDOWN\
                and event.key == pygame.K_e:
            snake_game(sc)
            world_map = world_map2

        # changing the volume
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if vol - 0.1 <= 0:
                vol = 0
            else:
                vol -= 0.1
            pygame.mixer.music.set_volume(vol)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if vol + 0.1 >= 1.0:
                vol = 1.0
            else:
                vol += 0.1
            pygame.mixer.music.set_volume(vol)

    # music in different modes
    if not play_music and not paused:
        pygame.mixer.music.load('music/doom.mp3')
        pygame.mixer.music.set_volume(vol)
        if First:
            vol -= 0.5
            pygame.mixer.music.set_volume(vol)
            First = False
        pygame.mixer.music.play(-1)
        play_music = True
    if paused and not pause_music:
        pygame.mixer.music.load('music/Alexander Nakarada - Chase.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_pos(4.38)
        play_music = False
    if not paused and pause_music:
        pause_music = False
        pygame.mixer.music.pause()

    # pause window
    if paused:
        game_pause(sc, bg_image, buttons)
        pause_music = True
    # winning/losing the game
    elif kill:
        fail()
        if not Continue:
            pygame.mixer.music.load('music/Iogann_Sebastyan_Bakh_-_Tokkata_i_fuga_re_minor_organ_-_Valter_Kraft_68309978.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_pos(1.0)
        Continue = True

    elif 8025 <= player.pos[0] <= 8175 and 125 <= player.pos[1] <= 310:
        win()
        if not Continue:
            pygame.mixer.music.load('music/gta-san-andreas-opening-intro.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_pos(24.38)
        Continue = True
    # open big map
    elif map_open:
        drawing.open_map(bg_image, player.pos)
    # game
    else:
        pygame.mixer.music.unpause()
        player.movement(world_map)
        for mob in mobs:
            if mob.mob_distance(player.pos) <= 1600:
                kill = mob.update(player.pos, world_map)
        # sc.fill(BLACK)
        drawing.background(player.angle)
        drawing.world(player.pos, player.angle, mobs, world_map)
        drawing.fps(clock)
        drawing.mini_map(player)
        drawing.compass(player.angle)
        pygame.display.flip()
        clock.tick(FPS)
