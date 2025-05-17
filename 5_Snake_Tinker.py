import tkinter as tk
import random

# Constants
GAME_WIDTH = 600
GAME_HEIGHT = 400
SNAKE_ITEM_SIZE = 20
INITIAL_SPEED = 100  # milliseconds
FOOD_COLOR = "red"
SNAKE_COLOR = "green"

DIRECTIONS = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game - Enhanced Version")
        self.canvas = tk.Canvas(root, width=GAME_WIDTH, height=GAME_HEIGHT, bg="black")
        self.canvas.pack()

        self.reset_game()
        self.root.bind("<Key>", self.change_direction)
        self.update()

    def reset_game(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.running = True
        self.paused = False
        self.score = 0
        self.speed = INITIAL_SPEED

        self.canvas.delete("all")
        self.score_text = self.canvas.create_text(50, 10, fill="white", font="Arial 14", text=f"Score: {self.score}")
        self.draw_snake()
        self.create_food()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SNAKE_ITEM_SIZE, y + SNAKE_ITEM_SIZE,
                                         fill=SNAKE_COLOR, tags="snake")

    def create_food(self):
        self.canvas.delete("food")
        x = random.randint(0, (GAME_WIDTH - SNAKE_ITEM_SIZE) // SNAKE_ITEM_SIZE) * SNAKE_ITEM_SIZE
        y = random.randint(0, (GAME_HEIGHT - SNAKE_ITEM_SIZE) // SNAKE_ITEM_SIZE) * SNAKE_ITEM_SIZE
        self.food = (x, y)
        self.canvas.create_oval(x, y, x + SNAKE_ITEM_SIZE, y + SNAKE_ITEM_SIZE,
                                fill=FOOD_COLOR, tags="food")

    def change_direction(self, event):
        key = event.keysym
        if key == "p":
            self.paused = not self.paused
        elif key == "r":
            self.reset_game()
        elif key in DIRECTIONS:
            opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if key != opposite.get(self.direction):
                self.direction = key

    def move_snake(self):
        dx, dy = DIRECTIONS[self.direction]
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx * SNAKE_ITEM_SIZE, head_y + dy * SNAKE_ITEM_SIZE)

        # Collision Check
        if (new_head in self.snake or
            not 0 <= new_head[0] < GAME_WIDTH or
            not 0 <= new_head[1] < GAME_HEIGHT):
            self.running = False
            self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, fill="white",
                                    font="Arial 24 bold", text="Game Over!\nPress 'R' to Restart")
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.speed = max(50, INITIAL_SPEED - (self.score * 2))
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.create_food()
        else:
            self.snake.pop()

        self.draw_snake()

    def update(self):
        if self.running and not self.paused:
            self.move_snake()
        self.root.after(self.speed, self.update)


# ------------ Run the Game ------------
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
