from tkinter import *
from Scoreboard import *
from tkinter import ttk
from tkinter import font


class StatSheetWindow(Toplevel):
    def __init__(self, current_game):
        Toplevel.__init__(self)
        self.current_game = current_game
        self.current_game.start_game()

        self.title("Play Game")
        self.geometry("850x600")
        self.tkraise()

        score_board = Scoreboard(self, self.current_game)
        score_board.grid(row=1, column=1, padx=20, pady=20)

    def dismiss(self):
        self.grab_release()
        self.destroy()



