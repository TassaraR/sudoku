import pygame
import numpy as np
from block import *
from params import *


class Grid:
    def __init__(self, matrix, win):

        self._matrix = np.array(matrix)
        self._board = np.array([[Block(i, j, self._matrix[i, j], self.init_status(i, j)) for j in range(NUM_BLOCKS)]
                                for i in range(NUM_BLOCKS)])
        self._win = win

        self._selected = None

    def init_status(self, i, j):
        if self._matrix[i, j] != 0:
            return 'sys'
        return 'usr'

    def board_values(self):
        # np.vectorize function is provided primarily for convenience, not for performance.
        # The implementation is essentially a for loop.
        return np.vectorize(lambda x: x.get_value(), otypes=[int])(self._board)

    def reset_board(self):
        for row in range(NUM_BLOCKS):
            for col in range(NUM_BLOCKS):
                if self._board[row, col].get_status() == 'usr':
                    self._board[row, col].set_value(0)

    def draw_board(self):

        for row in range(NUM_BLOCKS):
            for col in range(NUM_BLOCKS):
                self._board[row, col].draw(self._win)

        for line in range(NUM_BLOCKS + 1):
            if line % 3 == 0:
                line_thickness = GRID_BIG_LINE_THICKNESS
            else:
                line_thickness = GRID_NORMAL_LINE_THICKNESS

            # Horizontal Lines
            pygame.draw.line(self._win,
                             LINES_COLOR,
                             (PADDING_X + line * BLOCK_SIZE, PADDING_Y),
                             (PADDING_X + line * BLOCK_SIZE, PADDING_Y + BLOCK_SIZE * NUM_BLOCKS),
                             line_thickness)
            # Vertical Lines
            pygame.draw.line(self._win,
                             LINES_COLOR,
                             (PADDING_X, PADDING_Y + line * BLOCK_SIZE),
                             (PADDING_X + BLOCK_SIZE * NUM_BLOCKS, PADDING_Y + line * BLOCK_SIZE),
                             line_thickness)

    def handle_selection(self, mouse_pos):
        pos_x, pos_y = mouse_pos

        mouse_row = (pos_y - PADDING_Y) // BLOCK_SIZE
        mouse_col = (pos_x - PADDING_X) // BLOCK_SIZE

        # there are way better ways to resolve this performance-wise
        for row in range(NUM_BLOCKS):
            for col in range(NUM_BLOCKS):
                self._board[row, col].set_selected(False)
        self._selected = None

        # Board dimension constraints
        if PADDING_X <= pos_x <= PADDING_X + BLOCK_SIZE * NUM_BLOCKS and PADDING_Y <= pos_y <= BLOCK_SIZE * NUM_BLOCKS \
                and self._board[mouse_row, mouse_col].get_status() == 'usr':

            self._board[mouse_row, mouse_col].set_selected(True)
            self._selected = (mouse_row, mouse_col)

    def usr_input(self, mode, val):
        if self._selected is not None:
            row, col = self._selected
            if mode == 'input':
                self._board[row, col].set_value(val)
            if mode == 'remove':
                self._board[row, col].set_value(0)

    def is_valid(self, i, j, val):

        brd = self.board_values()

        if val in brd[i, :]:
            return False
        if val in brd[:, j]:
            return False
        i_ini = (i // 3) * 3
        j_ini = (j // 3) * 3
        square = brd[i_ini:i_ini + 3, j_ini:j_ini + 3]
        if np.where(square == val, True, False).any():
            return False
        return True

    def solve(self):

        for i in range(NUM_BLOCKS):
            for j in range(NUM_BLOCKS):
                if self._board[i, j].get_value() == 0:

                    for val in range(1, 10):

                        if self.is_valid(i, j, val):
                            self._board[i, j].set_value(val)

                            self._board[i, j].solver_update(self._win, VALID_COLOR)
                            pygame.display.update()
                            pygame.time.delay(SOLVE_DELAY_MS)

                            self.solve()
                            if 0 not in self.board_values().ravel():
                                return

                            self._board[i, j].set_value(0)

                            self._board[i, j].solver_update(self._win, INVALID_COLOR)
                            pygame.display.update()
                            pygame.time.delay(SOLVE_DELAY_MS)

                    return
