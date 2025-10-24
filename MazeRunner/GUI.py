import tkinter as tk
from Maze import Maze

# --- CONFIGURATION ---
CELL_SIZE = 50
PADDING = 30
WALL_COLOR = "#000000"   # Solid black walls
PATH_COLOR = "#e0e0e0"   # Light gray paths
START_COLOR = "#00e676"  # Bright green
GOAL_COLOR = "#ff1744"   # Bright red
SOLUTION_COLOR = "#ffea00"  # Vivid yellow path
GRID_COLOR = "#444444"   # Dark gray grid lines
BACKGROUND_COLOR = "#101010"  # Dark background window


class MazeGUI:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.window = tk.Tk()
        self.window.title("Maze Solver")
        self.window.configure(bg=BACKGROUND_COLOR)

        canvas_width = maze.width * CELL_SIZE + PADDING * 2
        canvas_height = maze.height * CELL_SIZE + PADDING * 2

        self.canvas = tk.Canvas(
            self.window,
            width=canvas_width,
            height=canvas_height,
            bg=BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(padx=20, pady=20)

        # Solve maze
        self.solution = maze.solve()

        # Draw maze
        self.draw_maze()

        self.center_window(canvas_width, canvas_height)
        self.window.mainloop()

    def center_window(self, width, height):
        """Centers the Tkinter window on the screen."""
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.window.geometry(f"{width+100}x{height+100}+{x}+{y}")

    def draw_maze(self):
        """Draws maze grid, start, goal, walls, and solution path."""
        for i in range(self.maze.height):
            for j in range(self.maze.width):
                x1 = PADDING + j * CELL_SIZE
                y1 = PADDING + i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                # Decide color
                if self.maze.walls[i][j]:
                    color = WALL_COLOR
                elif (i, j) == self.maze.start:
                    color = START_COLOR
                elif (i, j) == self.maze.goal:
                    color = GOAL_COLOR
                elif self.solution and (i, j) in self.solution:
                    color = SOLUTION_COLOR
                else:
                    color = PATH_COLOR

                # Draw rectangle
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline=GRID_COLOR,
                    width=2
                )


if __name__ == "__main__":
    maze = Maze("maze.txt")
    MazeGUI(maze)