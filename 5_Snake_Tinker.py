import tkinter as tk
import random

# Constants
GAME_WIDTH = 600
GAME_HEIGHT = 400
SNAKE_ITEM_SIZE = 20
SPEED = 100  # milliseconds
FOOD_COLOR = "red"
SNAKE_COLOR = "green"

# Directions
DIRECTIONS = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game using Tkinter")
        self.canvas = tk.Canvas(root, width=GAME_WIDTH, height=GAME_HEIGHT, bg="black")
        self.canvas.pack()
        
        self.score = 0
        self.direction = "Right"
        self.running = True

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = None

        self.root.bind("<Key>", self.change_direction)

        self.draw_snake()
        self.create_food()
        self.update()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SNAKE_ITEM_SIZE, y + SNAKE_ITEM_SIZE,
                                         fill=SNAKE_COLOR, tags="snake")

    def create_food(self):
        if self.food:
            self.canvas.delete("food")
        x = random.randint(0, (GAME_WIDTH - SNAKE_ITEM_SIZE) // SNAKE_ITEM_SIZE) * SNAKE_ITEM_SIZE
        y = random.randint(0, (GAME_HEIGHT - SNAKE_ITEM_SIZE) // SNAKE_ITEM_SIZE) * SNAKE_ITEM_SIZE
        self.food = (x, y)
        self.canvas.create_oval(x, y, x + SNAKE_ITEM_SIZE, y + SNAKE_ITEM_SIZE,
                                fill=FOOD_COLOR, tags="food")

    def change_direction(self, event):
        if event.keysym in DIRECTIONS:
            new_direction = event.keysym
            # Prevent reversing direction
            opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if new_direction != opposite.get(self.direction):
                self.direction = new_direction

    def move_snake(self):
        dx, dy = DIRECTIONS[self.direction]
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx * SNAKE_ITEM_SIZE, head_y + dy * SNAKE_ITEM_SIZE)

        # Check wall or self collision
        if (new_head in self.snake or
            not 0 <= new_head[0] < GAME_WIDTH or
            not 0 <= new_head[1] < GAME_HEIGHT):
            self.running = False
            self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, fill="white",
                                    font="Arial 24 bold", text="Game Over!")
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.create_food()
        else:
            self.snake.pop()

        self.draw_snake()

    def update(self):
        if self.running:
            self.move_snake()
            self.root.after(SPEED, self.update)

# ------------ Run the Game ------------
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
