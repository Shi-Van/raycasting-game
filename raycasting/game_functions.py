from importing_images import *


def close_game():
    global score, max_score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > max_score:
                with open('data\max_score.txt', 'w') as fin:
                    print(str(score), file=fin)
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if score > max_score:
                    with open('data\max_score.txt', 'w') as fin:
                        print(str(score), file=fin)
                my_game()


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
    render_max_score = font_score.render(f'рекорд: {max_score}', 1, pygame.Color('blue'))
    surface.blit(render_max_score, (5, 30))
    render_score = font_score.render(f'Украдено хекстеков: {score}', 1, (139, 0, 255))
    surface.blit(render_score, (5, 5))
    [surface.blit(img3, (i + 5, j + 5)) for i, j in snake[:-1]]
    surface.blit(img2, snake[-1])
    surface.blit(img, apple)


def my_game():
    global score, max_score
    global dx, dy, dirs
    x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    length = 1
    snake = [(x, y)]
    with open('data\max_score.txt', 'r') as fin:
        max_score = int(fin.read())
    score = 0
    speed_count = 0
    dx, dy = 0, 0
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

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
                render_end = font_end.render('GAME OVER', 1, pygame.Color('blue'))
                render_p = font_score.render('нажмите пробел для перезапуска', 1, (139, 0, 255))
                surface.blit(render_end, (RES // 2 - 200, RES // 3))
                surface.blit(render_p, (RES // 2 - 200, RES // 3 + 100))
                pygame.display.flip()
                close_game()

        pygame.display.flip()
        clock.tick(fps)
        next_key()
