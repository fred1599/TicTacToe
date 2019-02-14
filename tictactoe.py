from dataclasses import dataclass

from tkinter import messagebox

from utils import check
from utils import check_game

import tkinter as tk

@dataclass
class Game(tk.Tk):
    notfinish: bool = True
    again: bool = False
    size: int = 3

    def __post_init__(self):
        super().__init__()

        self.grid = [[0 for _ in range(Game.size)] for _ in range(Game.size)]

        self.w, self.h = 320, 320
        self.space = 10
        self.square = int((self.w - 2 * self.space) // self.size)

        self.canvas = tk.Canvas(self, width=self.w, height=self.h)
        self.canvas.bind("<Button-1>", self.draw_canvas)
        self.canvas.pack()

        self.init() # 3x3 cases

        self.player = 1
        self.colors = ('red', 'blue')


        self.mainloop()

    def update(self):
        Game.notfinish = check_game(self.grid)
        if not Game.notfinish:
            self.canvas.update_idletasks()
            self.player = self.player % 2 + 1 # another player play first
        else:
            self.display(f"Le gagnant est: {self.player}", question=False)
            Game.again = self.display("Voulez-vous rejouer ?", question=True)
            if Game.again:
                self.init()
            else:
                self.quit()

    def init(self):
        Game.notfinish = True
        self.grid = [[0 for _ in range(Game.size)] for _ in range(Game.size)]
        for y in range(
                self.space,
                self.square * Game.size,
                self.square
            ):
            for x in range(
                self.space,
                self.square * Game.size,
                self.square
            ):
                
                self.canvas.create_rectangle(
                    x, y, 
                    x + self.square,
                    y + self.square,
                    fill="white"
                )

    def draw_canvas(self, event):
        x, y = event.x, event.y
        case = self.canvas.find_closest(x, y) 
        x, y, x1, y1 = self.canvas.coords(case)
        column = int((x1 - self.square) // self.square)
        line = int((y1 - self.square) // self.square)
        if check(self.grid, line, column, self.player):
            self.draw(self.player, x+5, y+5, x1-5, y1-5) # 5 is space between square and oval
            self.update()

    def draw(self, figure, *coords):
        color = self.colors[figure-1]
        self.canvas.create_oval(*coords, fill=color)


    def display(self, message, question=True):
        if question:
            res = messagebox.askquestion('question', message)
            if res == 'yes': return True
        else:
            messagebox.showinfo('WINNER', message)
        return False



Game()