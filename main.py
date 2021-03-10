import pygame
import numpy as np
import grid
from params import *
from utils import *

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
values = np.array(parse_test_boards('test_boards.csv')[1])
grid = grid.Grid(values, win)
pygame.display.set_caption(WINDOW_NAME)


def main_loop():
    win.fill(BACKGROUND_COLOR)
    grid.draw_board()
    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # handles selection
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid.handle_selection(pygame.mouse.get_pos())

            # handles user inputs
            if event.type == pygame.KEYDOWN:

                if event.unicode in map(str, range(1, 10)):
                    key_pressed = int(event.unicode)
                    grid.usr_input('input', key_pressed)

                if event.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                    try:
                        grid.usr_input('remove', key_pressed)
                    except UnboundLocalError:
                        # temp fix for when user presses the button with nothing selected
                        pass

                if event.key == pygame.K_END:
                    grid.reset_board()

                if event.key == pygame.K_SPACE:
                    grid.reset_board()
                    main_loop()
                    grid.solve()
                    pygame.time.delay(SOLVED_DELAY_MS)

        main_loop()

    pygame.quit()


if __name__ == '__main__':
    main()
