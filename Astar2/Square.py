from enum import Enum


class Square(Enum):
    walls = "#"
    open_spaces = "."
    open_space_search = "-"
    open_space_solution = "="
    start = "o"
    finish = "*"
    wallColor = (0, 0, 0)
    open_spaceColor = (255, 255, 255)
    open_space_searchColor = (100, 100, 100)
    open_space_solutionColor = (128, 0, 128)
    startColor = (0, 200, 0)
    finishColor = (200, 0, 0)

    def __init__(self, val, row, col):
        super(Square, self).__init__(val)
        self.color = Square.getColour(Square.fromChar(val))
        self.row = row
        self.col = col

        pass

    @staticmethod
    def getColour(self):
        if self == Square.open_space_search:
            return Square.open_space_searchColor
            pass
        if self == Square.open_space_solution:
            return Square.open_space_solutionColor
            pass
        if self == Square.walls:
            return Square.wallColor
            pass
        if self == Square.open_spaces:
            return Square.open_spaceColor
            pass
        if self == Square.start:
            return Square.startColor
            pass
        if self == Square.finish:
            return Square.finishColor
            pass

    def toString(self):
        return self.value

    def change(self, obj):
        self = obj

    @staticmethod
    def fromChar(char: chr):
        return Square(char)
    # @staticmethod
    # def fromword(String: str):
    #     return Square(String)


if __name__ == "__main__":
    state = Square.walls

    # def toString(sq: Square):
    #     return sq.value
    # def fromChar(String: str):
    #     return Square(String).name
    print(Square.walls.value)
    print(state.toString())
    print(Square.fromChar("#"))
