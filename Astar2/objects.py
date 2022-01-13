from Astar2 import Maze
from Astar2 import MazeSolver
from enum import Enum


# Game State
class State(Enum):
    STEPPING = 1
    PAUSED = 2
    PLAYING = 3
    GAME_OVER = 4
    LOAD = 5
state = State.PLAYING


# Maze
m = Maze.Maze("star3")
m_solve = MazeSolver.MazeSolver(m)
m_solve2 = MazeSolver.MazeSolver2(m)
found = False


# BUTTONS
load = None
LOAD_SIZE = 40
start = None
step = None
toggle_anim = None