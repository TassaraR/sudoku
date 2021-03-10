import pygame
from params import *

pygame.font.init()


class Block:

    def __init__(self, row, col, value, status):

        self._row = row
        self._col = col
        self._value = value
        # usr, sys
        self._status = status
        # highlights cell
        self._selected = False

    def draw(self, win):
        block_text = pygame.font.Font(pygame.font.get_default_font(), FONT_BLOCK_SIZE)
        pos_i = PADDING_X + BLOCK_SIZE * (self._col + 1)
        pos_j = PADDING_Y + BLOCK_SIZE * (self._row + 1)

        if self._value != 0:
            if self._status == 'sys':
                txt_color = VALUE_NORMAL_COLOR
            elif self._status == 'usr':
                txt_color = USER_INPUT_COLOR

            block_text_render = block_text.render(str(self._value), True, txt_color)
            text_width, text_height = block_text.size(str(self._value))

            win.blit(block_text_render,
                     (pos_i - BLOCK_SIZE//2 - text_width//2, pos_j - BLOCK_SIZE//2 - text_height//2))

        if self._selected:
            pygame.draw.rect(win, SELECTION_COLOR,
                             pygame.Rect(pos_i - BLOCK_SIZE,
                                         pos_j - BLOCK_SIZE,
                                         BLOCK_SIZE, BLOCK_SIZE),
                             width=SELECTION_WIDTH)

    def solver_update(self, win, txt_color):
        block_text = pygame.font.Font(pygame.font.get_default_font(), FONT_BLOCK_SIZE)
        pos_i = PADDING_X + BLOCK_SIZE * (self._col + 1)
        pos_j = PADDING_Y + BLOCK_SIZE * (self._row + 1)

        # Draws a background-colored square behind text. Helps solver animation
        pygame.draw.rect(win, BACKGROUND_COLOR,
                         pygame.Rect(pos_i - BLOCK_SIZE // 2 - FONT_BLOCK_SIZE // 2,
                                     pos_j - BLOCK_SIZE // 2 - FONT_BLOCK_SIZE // 2,
                                     FONT_BLOCK_SIZE, FONT_BLOCK_SIZE),
                         width=0)

        if self._value != 0:
            block_text_render = block_text.render(str(self._value), True, txt_color)
            text_width, text_height = block_text.size(str(self._value))

            win.blit(block_text_render,
                     (pos_i - BLOCK_SIZE // 2 - text_width // 2, pos_j - BLOCK_SIZE // 2 - text_height // 2))

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self._status

    def set_selected(self, selected):
        self._selected = selected

    def is_selected(self):
        if self._selected:
            return True
        return False
