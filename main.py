import pygame

import random

WIDTH, HIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HIGHT))

FPS = 8

SNAKE_LEN = 1

move_side = ''

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

board = [
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,],
]
#snake spawn
pos_y = random.randrange(0,20)
pos_x = random.randrange(0,20)
board[pos_y][pos_x] = 'G'
#snake
snake_pos = [
    [pos_y, pos_x],
             ]
#apple spawn
apple_pos_y = random.randrange(0,20)
apple_pos_x = random.randrange(0,20)
board[apple_pos_y][apple_pos_x] = 'R'


def move(move_side):
    global pos_y, pos_x,SNAKE_LEN,apple_pos_x,apple_pos_y,FPS,snake_pos,run
    if move_side != '':
        board[pos_y][pos_x] = None

    if move_side == 'up':
        pos_y = 20 if pos_y == 0 else pos_y
        pos_y -= 1

    elif move_side == 'down':
        pos_y = -1 if pos_y == 19 else pos_y
        pos_y += 1

    elif move_side == 'left':
        pos_x = 20 if pos_x == 0 else pos_x
        pos_x -= 1

    elif move_side == 'right':
        pos_x = -1 if pos_x == 19 else pos_x
        pos_x += 1

    board[pos_y][pos_x] = 'G'

    if [pos_y,pos_x] in snake_pos and SNAKE_LEN>4:
        run = False

    if SNAKE_LEN < len(snake_pos)+1:
        board[snake_pos[-1][0]][snake_pos[-1][1]] = None
        snake_pos.pop(-1)

    snake_pos = snake_pos[::-1]
    snake_pos.append([pos_y, pos_x])
    snake_pos = snake_pos[::-1]

    snake_draw()

    if [apple_pos_x,apple_pos_y] == [pos_x,pos_y]  :
        # алманын жеуы

        SNAKE_LEN += 1
        apple_pos_y = random.randrange(0, 20)
        apple_pos_x = random.randrange(0, 20)
        if not [apple_pos_y,apple_pos_x] in snake_pos:
            board[apple_pos_y][apple_pos_x] = 'R'

def snake_draw():
    for i in snake_pos:
        board[i[0]][i[1]] = 'G'


def draw_board():
    step = 30
    height = 0
    for i in board:
        width = 0
        for j in i:
            color = GREEN if j == 'G' else RED if  j == 'R' else BLACK

            rect = pygame.Rect(width, height, width+step,height+step)
            pygame.draw.rect(WIN, color,rect)

            width += step

        height += step

def draw_window():

    draw_board()
    move(move_side)
    pygame.display.update()

run = True
def main():
    global move_side,run
    clock = pygame.time.Clock()
    while run:
        pygame.display.set_caption(str(SNAKE_LEN))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and move_side != 'down':
                    move_side = 'up'
                elif event.key == pygame.K_DOWN and move_side != 'up':
                    move_side = 'down'
                elif event.key == pygame.K_LEFT and move_side != 'right':
                        move_side = 'left'
                elif event.key == pygame.K_RIGHT and move_side != 'left':
                        move_side = 'right'

        draw_window()


    pygame.quit()

if __name__ == '__main__':
    main()