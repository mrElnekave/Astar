def add_neighbours(self, explore_tile, lst):
    neighbours = 0
    for i in range(1, 8, 2):
        col = i % 3 - 1
        row = i // 3 - 1
        if explore_tile[0] - row < 0:
            continue
        if explore_tile[1] - col < 0:
            continue
        if explore_tile[0] - row > self.maze_object.dimensions[1] - 1:
            continue
        if explore_tile[1] - col > self.maze_object.dimensions[0] - 1:
            continue
        new_tile = (explore_tile[0] - row, explore_tile[1] - col)
        if self.maze[new_tile[0]][new_tile[1]].val == Node.walls:
            continue
        neighbours += 1
        lst.append(new_tile)
        pass
    if neighbours == 3:  # more than the cell it came from and the cell it is going to. (an intersection)
        self.intersections.append((explore_tile, MazeSolver.euclidean_distance(explore_tile, self.finish)))
        print(self.intersections)

def get_explore_tile(self):
    if self.iterations_from_last_closest < 4:
        explore_tile = self.explore.pop()
        if len(self.intersections) != 0:
            if MazeSolver.euclidean_distance(explore_tile, self.finish) > self.intersections[len(self.intersections) - 1][1]:
                self.iterations_from_last_closest += 1
                print(self.iterations_from_last_closest)
            else:
                self.iterations_from_last_closest = 0
    else:
        explore_tile = self.intersections[len(self.intersections) - 1]
        explore_tile = explore_tile[0]
        self.iterations_from_last_closest = 0

    return explore_tile

def solveStep(self):
    if len(self.explore) == 0:
        return False

    # explore_tile = self.explore.pop()
    explore_tile = self.get_explore_tile()

    if explore_tile in self.visited:
        obj = (explore_tile, MazeSolver.euclidean_distance(explore_tile, self.finish))
        if obj in self.intersections:
            self.intersections.remove(obj)
        else:
            return self.solveStep()

    self.visited.add(explore_tile)
    self.maze_object.change(explore_tile, Node.open_space_search)

    if explore_tile == self.finish:
        return explore_tile
    self.add_neighbours(explore_tile, self.explore)
    directional_locs = MazeSolver.direction(explore_tile, self.finish)
    directional_locs.reverse()
    for dir in directional_locs:
        row,col = dir
        row = explore_tile[0] + row
        col = explore_tile[1] + col
        dir = (row, col)

        if dir in self.explore:
            # self.explore.pop(dir)
            self.explore.remove(dir)
            self.explore.append(dir)