import tkinter as tk
import random
from functools import partial

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🃏 Memory Card Block Game")
        
        self.cards = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.cards)

        self.buttons = []
        self.flipped = []
        self.matched = []

        self.create_ui()

    def create_ui(self):
        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.root, text=" ", width=8, height=4,
                                command=partial(self.flip_card, i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def flip_card(self, i, j):
        if len(self.flipped) == 2 or (i, j) in self.matched:
            return

        card_index = i * 4 + j
        char = self.cards[card_index]
        self.buttons[i][j].config(text=char, state='disabled')
        self.flipped.append((i, j, char))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        (i1, j1, c1), (i2, j2, c2) = self.flipped
        if c1 == c2:
            self.matched.extend([(i1, j1), (i2, j2)])
        else:
            self.buttons[i1][j1].config(text=" ", state='normal')
            self.buttons[i2][j2].config(text=" ", state='normal')
        self.flipped = []

        if len(self.matched) == len(self.cards):
            self.win_message()

    def win_message(self):
        win_label = tk.Label(self.root, text="🎉 You Win!", font=("Arial", 20), fg="green")
        win_label.grid(row=4, column=0, columnspan=4, pady=10)

#  Run the Game 
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
