from Astar2.Node import Node
import pygame
from Astar2 import constants as cst


class Maze:
    def __init__(self, path):
        # Maze
        self.dimensions = []
        self.maze = self.load_maze(path)

        # Graphics
        self.tile_image = pygame.Surface((cst.TILE_WIDTH, cst.TILE_HEIGHT))

    def find(self, symbol: Node):

        for row in range(self.dimensions[1]):
            for col in range(self.dimensions[0]):
                if symbol == self.maze[row][col].val:
                    return (row, col)
        return None

    def load_maze(self, path):
        maze = Maze.load_map(path)
        dimensions = maze.pop(0)
        for i in range(len(dimensions)):
            self.dimensions.append(int(dimensions[i]))

        for row in range(len(maze)):
            maze_row = maze[row]
            for col in range(len(maze_row)):
                tile = maze_row[col]
                maze[row][col] = Node(tile, row, col)
        return maze
        pass

    def get(self, loc):
        """
        :param loc: location
        :return: returns instance of Square
        """
        return self.maze[loc[0]][loc[1]]

    @staticmethod
    def load_map(path):
        f = open(path + ".txt", "r")
        data = f.read()
        f.close()
        data = data.split("\n")
        map = []
        first = True
        for row in data:
            if first:
                row = row.split(" ")
                map.append(row)
                first = False
            else:
                map.append(list(row))
        return map

    def print(self):
        for row in range(len(self.maze)):
            print()
            for col in range(len(self.maze[0])):
                print(self.maze[row][col].value, end="")

    def change(self, loc, new) -> None:
        if self.maze[loc[0]][loc[1]].val == Node.finish or self.maze[loc[0]][loc[1]].val == Node.start or self.maze[loc[0]][loc[1]].val == Node.used_teleporter:
            return
        if self.maze[loc[0]][loc[1]].val == Node.teleporter:
            self.maze[loc[0]][loc[1]] = Node("%", loc[0], loc[1])
            return
        self.maze[loc[0]][loc[1]] = Node(new, loc[0], loc[1])

    def display(self, screen: pygame.Surface):
        for row in range(self.dimensions[1]):
            for col in range(self.dimensions[0]):
                tile = self.maze[row][col]
                # colour = tile.getColour()
                colour = tile.color
                self.tile_image.fill(colour)
                x = cst.GRID_LEFT + (cst.TILE_X_SPACER + cst.TILE_WIDTH) * col
                y = cst.GRID_TOP + (cst.TILE_Y_SPACER + cst.TILE_HEIGHT) * row
                screen.blit(self.tile_image, (x, y))


if __name__ == "__main__":
    m = Maze("star")
    m.print()
    print(m.find(Node.start))
