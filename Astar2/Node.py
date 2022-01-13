
dic = {
    "walls" : "#",
    "open_spaces" : ".",
    "open_space_search" : "-",
    "open_space_solution" : ":",
    "start" : "o",
    "finish" : "*",
    "wallColor" : (0, 0, 0),
    "open_spaceColor" : (255, 255, 255),
    "open_space_searchColor" : (100, 100, 100),
    "open_space_solutionColor" : (128, 0, 128),
    "startColor" : (0, 200, 0),
    "finishColor" : (200, 0, 0),
    }


class Node:
    walls = "#"
    open_spaces = "."
    open_space_search = "-"
    open_space_solution = "="
    start = "o"
    finish = "*"
    teleporter = "@"
    used_teleporter = "%"
    wallColor = (0, 0, 0)
    open_spaceColor = (255, 255, 255)
    open_space_searchColor = (100, 100, 100)
    open_space_solutionColor = (128, 0, 128)
    startColor = (0, 200, 0)
    finishColor = (200, 0, 0)
    teleporterColor = (255, 0, 255)
    used_teleporterColor = (150, 0, 255)

    def __init__(self, val, row, col):  # if i ever want to make them all there own Nodes; which i do right now.
        self.val = Node.fromChar(val)
        self.value = val
        self.row = row
        self.col = col
        self.loc = (row, col)
        self.color = Node.getColourFromChar(val)
        pass

    # def get_neighbours(self):
    #     return self.neighbours

    @staticmethod
    def getColourFromChar(self):
        if self == Node.open_space_search:
            return Node.open_space_searchColor
            pass
        elif self == Node.open_space_solution:
            return Node.open_space_solutionColor
            pass
        elif self == Node.walls:
            return Node.wallColor
            pass
        elif self == Node.open_spaces:
            return Node.open_spaceColor
            pass
        elif self == Node.start:
            return Node.startColor
            pass
        elif self == Node.finish:
            return Node.finishColor
            pass
        elif self == Node.teleporter:
            return Node.teleporterColor
            pass
        elif self == Node.used_teleporter:
            return Node.used_teleporterColor
            pass
        return False

    def getColour(self):
        if self.val == Node.open_space_search:
            return Node.open_space_searchColor
            pass
        elif self.val == Node.open_space_solution:
            return Node.open_space_solutionColor
            pass
        elif self.val == Node.walls:
            return Node.wallColor
            pass
        elif self.val == Node.open_spaces:
            return Node.open_spaceColor
            pass
        elif self.val == Node.start:
            return Node.startColor
            pass
        elif self.val == Node.finish:
            return Node.finishColor
            pass
        elif self.val == Node.teleporter:
            return Node.teleporterColor
            pass
        elif self.val == Node.used_teleporter:
            return Node.used_teleporterColor
            pass

    def toString(self):
        return self.value

    @staticmethod
    def fromChar(char: chr):
        if char == "#":
            return Node.walls
        elif char == ".":
            return Node.open_spaces
        elif char == "-":
            return Node.open_space_search
        elif char == "=":
            return Node.open_space_solution
        elif char == "o":
            return Node.start
        elif char == "*":
            return Node.finish
        elif char == "@":
            return Node.teleporter
        elif char == "%":
            return Node.used_teleporter
