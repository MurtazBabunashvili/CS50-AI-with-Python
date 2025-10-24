from Frontier import Node, StackFrontier, QueueFrontier

class Maze:
    def __init__(self, filename):
        # Read maze from file
        with open(filename) as f:
            contents = f.read()

        contents = contents.splitlines()

        # Validate and store height/width
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Build maze grid and find start/goal
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    cell = contents[i][j]
                except IndexError:
                    cell = " "

                if cell == "A":
                    self.start = (i, j)
                    row.append(False)
                elif cell == "B":
                    self.goal = (i, j)
                    row.append(False)
                elif cell == "#":
                    row.append(True)
                else:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def solve(self):
        start = Node(self.start, None, None)
        frontier = StackFrontier()
        frontier.add(start)

        explored = set()

        while not frontier.empty():
            node = frontier.remove()

            if node.state == self.goal:
                path = []
                while node.parent is not None:
                    path.append(node.state)
                    node = node.parent

                path.reverse()
                self.solution = path
                return path
            explored.add(node.state)
            neighbors = self.neighbors(node.state)
            for neighbor in neighbors:
                if not frontier.contains_state(neighbor) and neighbor not in explored:
                    frontier.add(Node(neighbor, node, None))
        return None



    def neighbors(self, state):
        neighbors = []

        (i,j) = state

        if j+1<self.width and not self.walls[i][j+1]:
            neighbors.append((i,j+1))
        if i+1 < self.height and not self.walls[i+1][j]:
            neighbors.append((i+1,j))
        if j-1 >= 0 and not self.walls[i][j-1]:
            neighbors.append((i,j-1))
        if i-1 >= 0 and not self.walls[i-1][j]:
            neighbors.append((i-1,j))
        return neighbors
