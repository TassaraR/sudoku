FPS = 60
WINDOW_NAME = 'Sudoku'

WINDOW_SIZE = (600, 600)
WIN_WIDTH, WIN_HEIGHT = WINDOW_SIZE
PADDING_X = 10
PADDING_Y = 5

BOARD_SIZE = min(WINDOW_SIZE) - 2*PADDING_X
NUM_BLOCKS = 9
GRID_NORMAL_LINE_THICKNESS = 1
GRID_BIG_LINE_THICKNESS = 4
BLOCK_SIZE = BOARD_SIZE // NUM_BLOCKS
FONT_BLOCK_SIZE = int(0.4 * BLOCK_SIZE)
SELECTION_WIDTH = 4

SOLVE_DELAY_MS = 10
SOLVED_DELAY_MS = 1000

BACKGROUND_COLOR = (255, 255, 255)
VALUE_NORMAL_COLOR = (0, 0, 0)
USER_INPUT_COLOR = (180, 180, 180)
SELECTION_COLOR = (255, 165, 0)
LINES_COLOR = (0, 0, 0)
VALID_COLOR = (0, 200, 0)
INVALID_COLOR = (255, 0, 0)