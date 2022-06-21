import pygame
from random import randrange
from settings import HALF_HEIGHT, HALF_WIDTH

RES = 700
SIZE = 50
snake_speed = 10
pygame.init()
surface = pygame.Surface((RES, RES))
aim = 12
clock = pygame.time.Clock()
fps = 60
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 65, bold=True)
img = pygame.image.load("images\ваня.png")
img = pygame.transform.scale(img, (50, 50))
img2 = pygame.image.load("data\_cr01mQK8.png")
img2 = pygame.transform.scale(img2, (50, 50))
img3 = pygame.image.load("images\ваня.png")
img3 = pygame.transform.scale(img3, (40, 40))
img4 = pygame.image.load("data\Visual_Night.jpg")
img4 = pygame.transform.scale(img4, (RES, RES))


def close_game(sc):
    global score, max_score
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = snake_game(sc)
                if not x:
                    return True

def next_key():
    global dx, dy, dirs
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }


def render_image(snake, apple):
    surface.blit(img4, (0, 0))
    render_score = font_score.render(f'младенцев избито: {score}', True, (139, 0, 255))
    surface.blit(render_score, (5, 5))
    [surface.blit(img3, (i + 5, j + 5)) for i, j in snake[:-1]]
    surface.blit(img2, snake[-1])
    surface.blit(img, apple)


def snake_game(sc):
    global score, max_score
    global dx, dy, dirs
    global aim
    x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    length = 1
    snake = [(x, y)]
    score = 0
    speed_count = 0
    dx, dy = 0, 0
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}

    while True:
        for event in pygame.event.get():
            pass
        if score == aim:
            return False

        render_image(snake, apple)

        speed_count += 1
        if not speed_count % snake_speed:
            x = (x + dx * SIZE)
            y = (y + dy * SIZE)
            snake.append((x, y))
            snake = snake[-length:]

        if snake[-1] == apple:
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
            length += 1
            score += 1

        if x < 0 or x > RES - SIZE or y > RES - SIZE or y < 0 or len(snake) != len(set(snake)):
            while True:
                render_end = font_end.render('GAME OVER', True, pygame.Color('blue'))
                render_p = font_score.render('нажмите пробел для перезапуска', True, (139, 0, 255))
                surface.blit(render_end, (RES // 2 - 200, RES // 3))
                surface.blit(render_p, (RES // 2 - 200, RES // 3 + 100))
                sc.blit(surface, (HALF_WIDTH - (RES // 2), HALF_HEIGHT - (RES // 2)))
                pygame.display.flip()
                if close_game(sc):
                    return False

        pygame.display.flip()
        next_key()
        sc.blit(surface, (HALF_WIDTH - (RES // 2), HALF_HEIGHT - (RES // 2)))
        clock.tick(fps)
