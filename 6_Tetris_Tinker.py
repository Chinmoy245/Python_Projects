import tkinter as tk
import random

# Game constants
CELL_SIZE = 30
COLUMNS = 10
ROWS = 20
DELAY = 300  # milliseconds

# Shapes (tetrominoes)
SHAPES = {
    "I": [[1, 1, 1, 1]],
    "O": [[1, 1],
          [1, 1]],
    "T": [[0, 1, 0],
          [1, 1, 1]],
    "S": [[0, 1, 1],
          [1, 1, 0]],
    "Z": [[1, 1, 0],
          [0, 1, 1]],
    "J": [[1, 0, 0],
          [1, 1, 1]],
    "L": [[0, 0, 1],
          [1, 1, 1]]
}

COLORS = {
    "I": "cyan",
    "O": "yellow",
    "T": "purple",
    "S": "green",
    "Z": "red",
    "J": "blue",
    "L": "orange"
}

class Tetris:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CELL_SIZE * COLUMNS, height=CELL_SIZE * ROWS, bg="black")
        self.canvas.pack()

        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.score = 0

        self.current_shape = None
        self.shape_type = None
        self.x = 0
        self.y = 0

        self.root.bind("<Left>", lambda event: self.move(-1))
        self.root.bind("<Right>", lambda event: self.move(1))
        self.root.bind("<Down>", lambda event: self.drop())
        self.root.bind("<Up>", lambda event: self.rotate())

        self.spawn_new_shape()
        self.update()

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLUMNS):
                color = self.board[r][c]
                if color:
                    self.draw_cell(c, r, color)

        for r, row in enumerate(self.current_shape):
            for c, val in enumerate(row):
                if val:
                    self.draw_cell(self.x + c, self.y + r, COLORS[self.shape_type])

    def draw_cell(self, x, y, color):
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def spawn_new_shape(self):
        self.shape_type = random.choice(list(SHAPES.keys()))
        self.current_shape = SHAPES[self.shape_type]
        self.x = COLUMNS // 2 - len(self.current_shape[0]) // 2
        self.y = 0

        if not self.valid_position():
            self.game_over()

    def valid_position(self, dx=0, dy=0, shape=None):
        if shape is None:
            shape = self.current_shape
        for r, row in enumerate(shape):
            for c, val in enumerate(row):
                if val:
                    new_x = self.x + c + dx
                    new_y = self.y + r + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                        return False
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return False
        return True

    def move(self, dx):
        if self.valid_position(dx=dx):
            self.x += dx
            self.draw_board()

    def drop(self):
        if self.valid_position(dy=1):
            self.y += 1
        else:
            self.lock_shape()
            self.clear_lines()
            self.spawn_new_shape()
        self.draw_board()

    def rotate(self):
        rotated = list(zip(*self.current_shape[::-1]))
        if self.valid_position(shape=rotated):
            self.current_shape = rotated
        self.draw_board()

    def lock_shape(self):
        for r, row in enumerate(self.current_shape):
            for c, val in enumerate(row):
                if val:
                    self.board[self.y + r][self.x + c] = COLORS[self.shape_type]

    def clear_lines(self):
        lines = [row for row in self.board if all(row)]
        cleared = len(lines)
        self.score += cleared * 100
        if cleared:
            self.board = [[None for _ in range(COLUMNS)] for _ in range(cleared)] + \
                         [row for row in self.board if not all(row)]

    def update(self):
        self.drop()
        self.draw_board()
        if self.running:
            self.root.after(DELAY, self.update)

    def game_over(self):
        self.canvas.create_text(CELL_SIZE * COLUMNS // 2, CELL_SIZE * ROWS // 2,
                                text="GAME OVER", fill="white", font=("Arial", 24))
        self.running = False

    @property
    def running(self):
        return hasattr(self, "_running") and self._running

    @running.setter
    def running(self, value):
        self._running = value

#  Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    root.title("🧱 Tetris Game using Tkinter")
    game = Tetris(root)
    game.running = True
    root.mainloop()
