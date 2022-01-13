import pygame

pygame.init()


# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPLIT_FIVE = SCREEN_WIDTH/5
SPLIT_FOUR = SCREEN_WIDTH/4
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# For locating cards on the play grid
GRID_LEFT_OFFSET = SCREEN_WIDTH/16       # Distance from left to start drawing grid
GRID_TOP_OFFSET = SCREEN_HEIGHT/6        # Distance from top to start drawing grid
TILE_X_SPACER = 0           # Separation between cards horizontally
TILE_Y_SPACER = 0           # Separation between cards vertically
COLS = 9                    # Beginning number of columns in the grid
ROWS = 9                    # Number of rows in the grid
TILE_HEIGHT = 12
TILE_WIDTH = 12


# From top of window to bottom of grid
GRID_BOTTOM = GRID_TOP_OFFSET + ROWS * (TILE_HEIGHT + TILE_Y_SPACER)
GRID_RIGHT = GRID_LEFT_OFFSET + COLS * (TILE_WIDTH + TILE_X_SPACER)
GRID_LEFT = GRID_LEFT_OFFSET
GRID_TOP = GRID_TOP_OFFSET

# From top of window to top of buttons
# final int BUTTON_LEFT_OFFSET = GRID_LEFT_OFFSET
# final int BUTTON_TOP_OFFSET = GRID_BOTTOM + 16
# final int BUTTON_WIDTH = 200
# final int BUTTON_HEIGHT = 56

# Four buttons: Add Cards, Find Set, New Game, Pause
# public final int NUM_BUTTONS = 4


# Score information
scoreFont = pygame.font.Font("freesansbold.ttf", 32)
SCORE_FILL = (255, 255, 255)    # Black RGB values feel free to change
score = 0
SCORE_LEFT_OFFSET = GRID_LEFT_OFFSET
SCORE_TOP_OFFSET = 25

# Timer information
timerFont = pygame.font.Font("freesansbold.ttf", 32)
TIMER_FILL = (255, 255, 255)    # Black RGB values feel free to change
TIMER_LEFT_OFFSET = SCORE_LEFT_OFFSET+256
TIMER_TOP_OFFSET = SCORE_TOP_OFFSET

# Message information
# public PFont messageFont
# public final color MESSAGE_FILL = #000000    # Black RGB values feel free to change
# public int message
# public final int MESSAGE_LEFT_OFFSET = TIMER_LEFT_OFFSET+256
# public final int MESSAGE_TOP_OFFSET = TIMER_TOP_OFFSET



BACKGROUND_COLOR = (189, 195, 199)
# public final color SELECTED_HIGHLIGHT = #FFDD00
# public final color CORRECT_HIGHLIGHT = #00FF00
# public final color INCORRECT_HIGHLIGHT = #FF0000
# public final color FOUND_HIGHLIGHT = #11CCCC
# public final int HIGHLIGHT_TICKS = 35
# public final int FIND_SET_TICKS = 60
# public int highlightCounter = 0

# TIMER
timeElapsed = 0

# TEXT BOX
TEXT_BOX_X = SCREEN_WIDTH/20
TEXT_BOX_Y = SCREEN_HEIGHT/50


# # BUTTONS
LOAD_SIZE = 40

