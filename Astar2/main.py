from Astar2.textBox import TextBox
from pygame.locals import *
from Astar2 import constants as cst
from Astar2 import objects as obj
from Astar2.Node import Node
from Astar2 import MazeSolver
# from Astar2.constants import State
import pygame, sys

State = obj.State

pygame.init()
mainClock = pygame.time.Clock()

tbX = (cst.SCREEN_WIDTH - (cst.SCREEN_WIDTH/20) * 2) - cst.LOAD_SIZE * 2
tb = TextBox(cst.TEXT_BOX_X, cst.TEXT_BOX_Y, tbX, 40, border=3, text_size=15)


def manageKeys(event):
    mods = pygame.key.get_mods()
    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
        tb.update_text(event.key, shift=True)
    else:
        tb.update_text(event.key)
def collisions(m_pos):  # changed for simplicity pls change back.
    mx, my = m_pos
    if cst.load.collidepoint((mx, my)):
        obj.state = State.LOAD
    elif cst.start.collidepoint((mx, my)):
        obj.state = State.PLAYING
    elif cst.step.collidepoint((mx, my)):
        # obj.state = State.STEPPING
        obj.found = True
        solveMaze()
    elif cst.toggle_anim.collidepoint((mx, my)):
        # if obj.state == State.PAUSED:
        #     obj.state = State.PLAYING
        # if obj.state == State.PLAYING:
        #     obj.state = State.PAUSED
        if obj.found is True:
            obj.found = False
        elif obj.found is False:
            obj.found = True
    else:
        tb.click(m_pos)
def drawStuff():
    cst.load = TextBox.draw_text("load", cst.screen, x=cst.TEXT_BOX_X + tb.Box_w + 10, y=cst.TEXT_BOX_Y)
    cst.start = TextBox.draw_text("start", cst.screen, x=cst.SPLIT_FOUR * 1, y=60, middle=True)
    cst.step = TextBox.draw_text("step", cst.screen, x=cst.SPLIT_FOUR * 2, y=60, middle=True)
    cst.toggle_anim = TextBox.draw_text("toggle animation", cst.screen, x=cst.SPLIT_FOUR * 3, y=60, middle=True)
def draw_TextBox():
    tb.draw(cst.screen)
def solveMazeD():
    ans = obj.m_solve2.dijsktra()
    if ans is False:
        # no result found
        print("no result")
        return None
    if ans is not None:
        obj.found = True
        final_path = ans
        for loc in final_path:
            obj.m.change(loc, Node.open_space_solution)
    pass
def solveMaze():
    # ans = obj.m_solve.solveBasicStep()
    ans = obj.m_solve.solveStep()
    if ans.__class__ == tuple:
        obj.found = True
        final_path = obj.m_solve.dijsktra()
        for loc in final_path:
            obj.m.change(loc, Node.open_space_solution)

    if ans is False:
        # no result found
        print("no result")
        pass
    pass


def game():
    running = True
    while running:
        # Events
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                manageKeys(event)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # fill the cst.screen
        cst.screen.fill((0, 60, 60))

        # do stuff
        draw_TextBox()
        drawStuff()

        if not obj.found:
            solveMaze()
            # solveMazeD()
        obj.m.display(cst.screen)

        # collisions
        m_pos = pygame.mouse.get_pos()
        if click:
            collisions(m_pos)

        # update
        pygame.display.update()
        mainClock.tick(100)


def main_menu():

    while True:
        while obj.state == State.PLAYING:
            game()


main_menu()
