from Astar2.Maze import Maze
from Astar2.Node import Node
import math


class MazeSolver:

    def __init__(self, m: Maze):
        # maze
        self.maze_object = m
        self.maze = m.maze
        # important locations
        self.finish = m.find(Node.finish)
        self.start = m.find(Node.start)
        self.is_teleport = isinstance(m.find(Node.teleporter), tuple)
        # basicSolve
        self.explore = []
        self.visited = set()
        self.explore.append(m.find(Node.start))
        # advanced solve
        self.intersections = []  # here lie the possible alternate routes the solver can take (Euclidean)
        self.iterations_from_last_closest = 0  # 5 steps before going to a spot of closest.
        self.removed_intersections = []

    def resetVisited(self):
        self.visited = set()

    def in_dimensions(self, new_tile):
        if new_tile[0] < 0:
            return False
        if new_tile[1] < 0:
            return False
        if new_tile[0] > self.maze_object.dimensions[1] - 1:
            return False
        if new_tile[1] > self.maze_object.dimensions[0] - 1:
            return False
        return True

    def add_neighbours(self, explore_tile, lst, intersectionTesting=False):
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
        if neighbours == 3 and not intersectionTesting:  # more than the cell it came from and the cell it is going to. (an intersection)
            self.intersections.append((explore_tile, MazeSolver.euclidean_distance(explore_tile, self.finish)))
            # print("make: ", self.intersections)

    def get_explore_tile(self):
        # if self.iterations_from_last_closest > 0:
        #     print(self.iterations_from_last_closest)
        if self.iterations_from_last_closest < 3:
            explore_tile = self.explore.pop()
            if len(self.intersections) != 0:
                if MazeSolver.euclidean_distance(explore_tile, self.finish) > self.intersections[len(self.intersections) - 1][1]:
                    self.iterations_from_last_closest += 1
                else:
                    self.iterations_from_last_closest = 0
        else:
            run = True
            while run:
                explore_tile = self.intersections[len(self.intersections) - 1]
                explore_tile = explore_tile[0]
                neighbours = []
                self.add_neighbours(explore_tile, neighbours, intersectionTesting=True)
                count = 0
                for neighbour in neighbours:
                    if neighbour in self.visited:
                        count += 1
                if count == 3:
                    self.intersections.pop()
                else:
                    run = False

            self.iterations_from_last_closest = 0

        return explore_tile

    def solveStep(self):
        # if self.is_teleport:
        #     return self.solveStep_teleport()
        if len(self.explore) == 0:
            return False

        # explore_tile = self.explore.pop()
        explore_tile = self.get_explore_tile()
        if explore_tile in self.visited:
            obj = (explore_tile, MazeSolver.euclidean_distance(explore_tile, self.finish))
            if obj in self.intersections and obj not in self.removed_intersections:
                self.intersections.remove(obj)
                self.removed_intersections.append(obj)
            else:
                return self.solveStep()

        self.visited.add(explore_tile)
        self.maze_object.change(explore_tile, Node.open_space_search)

        if explore_tile == self.finish:
            return explore_tile

        if self.maze[explore_tile[0]][explore_tile[1]].value == Node.used_teleporter:
            explore_tile = self.maze_object.find(Node.teleporter)

            self.add_neighbours(explore_tile, self.explore)
            pass
        else:
            self.add_neighbours(explore_tile, self.explore)
            pass
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

    def solveBasicStep(self):
        if len(self.explore) == 0:
            return False

        explore_tile = self.explore.pop()

        if explore_tile in self.visited:
            return self.solveBasicStep()

        self.visited.add(explore_tile)
        self.maze_object.change(explore_tile, Node.open_space_search)

        if explore_tile == self.finish:
            return explore_tile

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
            self.explore.append(new_tile)

    @staticmethod
    def euclidean_distance(cord1: tuple, cord2: tuple):
        distance = math.sqrt(math.pow(cord1[0] - cord2[0], 2) + math.pow(cord1[1] - cord2[1], 2))
        return distance

    @staticmethod
    def direction(start_cord: tuple, end_cord: tuple):
        start_cord_row = start_cord[0]
        start_cord_col = start_cord[1]
        end_cord_row = end_cord[0]
        end_cord_col = end_cord[1]

        new_vector = (end_cord_row - start_cord_row, end_cord_col - start_cord_col)

        # returns possible directions in preference
        if math.fabs(new_vector[0]) > math.fabs(new_vector[1]):
            tpl = []
            tpl.append((int(new_vector[0] // math.fabs(new_vector[0])), 0))
            if new_vector[1] == 0:
                tpl.append((0, 0))
                pass
            else:  # problem here
                tpl.append((0, int(new_vector[1] // math.fabs(new_vector[1]))))
            return tpl
        else:
            tpl = []
            tpl.append((0, int(new_vector[1] // math.fabs(new_vector[1]))))
            if new_vector[0] == 0:
                tpl.append((0, 0))
                pass
            else:  # problem here
                tpl.append((int(new_vector[0] // math.fabs(new_vector[0])), 0))
            return tpl

    def dijsktra(self):
        initial = self.start
        end = self.finish
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()
        while current_node != end:
            visited.add(current_node)
            destinations = []

            if self.maze[current_node[0]][current_node[1]].value == Node.used_teleporter:
                new_tile = self.maze_object.find(Node.teleporter)
                destinations.append(new_tile)
                pass
            else:
                for i in range(1, 8, 2):
                    col = i % 3 - 1
                    row = i // 3 - 1
                    if current_node[0] - row < 0:
                        continue
                    if current_node[1] - col < 0:
                        continue
                    if current_node[0] - row > self.maze_object.dimensions[1] - 1:
                        continue
                    if current_node[1] - col > self.maze_object.dimensions[0] - 1:
                        continue
                    new_tile = (current_node[0] - row, current_node[1] - col)
                    if self.maze[new_tile[0]][new_tile[1]].val == Node.walls or new_tile not in self.visited:
                        continue
                    destinations.append(new_tile)
            distance_to_shortest_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = 1 + distance_to_shortest_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

    # pseudo code
    # At the start:
        # 1. Create an (empty) agenda of locations to explore.
        # 2. Add the start location to it.
    # Each step thereafter:
        # 1. Is the agenda empty? If so, the finish is unreachable; terminate the
        # algorithm.
        # 2. Grab a location from the agenda.
        # 3. Have we pulled this location from the agenda before? If so, no need
        # to explore it again; this step is done.
        # 4. Does the location correspond to the finish square? If so, the finish
        # was reachable; terminate the algorithm.
        # 5. Otherwise, it is a reachable non-finish location that we haven't seen
        # yet. So, explore it as follows:
        # - compute all the adjacent locations that are inside the maze and
        # aren't walls, and
        # - add them to the agenda for later exploration.
        # 6. Also, record the fact that you've explored this location so you won't
        # ever have to explore it again.


class MazeSolver2:

    def __init__(self, m: Maze):
        # maze
        self.maze_object = m
        self.maze = m.maze
        # important locations
        self.finish = m.find(Node.finish)
        self.start = m.find(Node.start)
        self.is_teleport = isinstance(m.find(Node.teleporter), tuple)
        # basicSolve
        self.shortest_paths = {self.start: (None, 0)}
        self.current_node = self.start
        self.visited = set()
        # advanced solve
        self.intersections = []  # here lie the possible alternate routes the solver can take (Euclidean)
        self.iterations_from_last_closest = 0  # 5 steps before going to a spot of closest.
        self.removed_intersections = []

    @staticmethod
    def euclidean_distance(cord1: tuple, cord2: tuple):
        distance = math.sqrt(math.pow(cord1[0] - cord2[0], 2) + math.pow(cord1[1] - cord2[1], 2))
        return distance

    def dijsktra(self):
        end = self.finish
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        if self.current_node == end:
            # Work back through destinations in shortest path
            path = []
            while self.current_node is not None:
                path.append(self.current_node)
                next_node = self.shortest_paths[self.current_node][0]
                self.current_node = next_node
            # Reverse path
            path = path[::-1]
            return path
        else:
            self.visited.add(self.current_node)
            destinations = []

            if self.maze[self.current_node[0]][self.current_node[1]].value == Node.used_teleporter:
                new_tile = self.maze_object.find(Node.teleporter)
                destinations.append(new_tile)
                pass
            else:
                for i in range(1, 8, 2):
                    col = i % 3 - 1
                    row = i // 3 - 1
                    if self.current_node[0] - row < 0:
                        continue
                    if self.current_node[1] - col < 0:
                        continue
                    if self.current_node[0] - row > self.maze_object.dimensions[1] - 1:
                        continue
                    if self.current_node[1] - col > self.maze_object.dimensions[0] - 1:
                        continue
                    new_tile = (self.current_node[0] - row, self.current_node[1] - col)
                    if self.maze[new_tile[0]][new_tile[1]].val == Node.walls:
                        continue
                    destinations.append(new_tile)
            distance_to_shortest_node = self.shortest_paths[self.current_node][1]

            for next_node in destinations:
                weight = 1 + distance_to_shortest_node
                if next_node not in self.shortest_paths:
                    self.shortest_paths[next_node] = (self.current_node, weight)
                else:
                    current_shortest_weight = self.shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        self.shortest_paths[next_node] = (self.current_node, weight)

            next_destinations = {node: self.shortest_paths[node] for node in self.shortest_paths if node not in self.visited}
            if not next_destinations:
                print("Route Not Possible")
                return False
            # next node is the destination with the lowest weight
            self.maze_object.change(self.current_node, Node.open_space_search)
            self.current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        return None


if __name__ == "__main__":
    m = Maze("star3")
    ms = MazeSolver(m)
    print(ms.direction((3, 2), (1, 6)))
