import tkinter
from tkinter import ttk
from tkinter.ttk import *
from resources.KBFonts import *


class Scoreboard(ttk.Frame):
    def __init__(self, parent, active_game):
        s = Style()
        s.configure('ScoreBoard.TFrame', background='black')
        ttk.Frame.__init__(self, parent, style='ScoreBoard.TFrame')
        self.parent = parent
        self.game = active_game
        self.game_clock = self.game.game_clock

        self.columnconfigure(1, weight=2, uniform='college')
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=2, uniform='college')

        # Time Panel
        self.time_on_clock = tkinter.StringVar()
        self.time_on_clock.set(self.game_clock.display_time_clock())
        lbl_time_clock = ttk.Label(self, textvariable=self.time_on_clock, font=MEDIUM_BOLD,
                                   foreground='red', background='black')
        lbl_time_clock.grid(row=1, column=2, rowspan=2)

        # Score Panels
        lbl_home_name = ttk.Label(self, text=f'{self.game.home_team.college}', font=MEDIUM_FONT,
                                  foreground='white', background='black')
        lbl_home_name.grid(row=1, column=1, padx=10, pady=5)
        lbl_home_score = ttk.Label(self, text=self.game.home_score, font=MEDIUM_BOLD,
                                   foreground='white', background='black')
        lbl_home_score.grid(row=2, column=1)
        lbl_away_name = ttk.Label(self, text=f'{self.game.away_team.college}', font=MEDIUM_FONT,
                                  foreground='white', background='black')
        lbl_away_name.grid(row=1, column=3, padx=10, pady=5)
        lbl_away_score = ttk.Label(self, text=self.game.away_score, font=MEDIUM_BOLD,
                                   foreground='white', background='black')
        lbl_away_score.grid(row=2, column=3)

        # Bonus Panels
        lbl_home_bonus = ttk.Label(self, text="Bonus", font=SMALL_FONT, foreground='white', background='black')
        lbl_home_bonus.grid(row=3, column=1, padx=10, pady=2)
        lbl_home_bonus.grid_forget()
        lbl_away_bonus = ttk.Label(self, text="Bonus", font=SMALL_FONT, foreground='white', background='black')
        lbl_away_bonus.grid(row=3, column=3, padx=10, pady=2)
        lbl_away_bonus.grid_forget()

        # Possession Arrow
        lbl_possession = ttk.Label(self, text="Poss", font=SMALL_FONT, foreground='white', background='black')
        lbl_possession.grid(row=3, column=2, padx=10, pady=2)
        if self.game.possession_arrow_to_home:
            lbl_possession_arrow = ttk.Label(self, text="<", font=MEDIUM_BOLD, foreground='white', background='black')
        else:
            lbl_possession_arrow = ttk.Label(self, text=">", font=MEDIUM_BOLD, foreground='white', background='black')
        lbl_possession_arrow.grid(row=4, column=2, padx=10, pady=2)

        # Foul Panels
        lbl_home_pf = ttk.Label(self, text="Fouls", font=SMALL_FONT, foreground='white', background='black')
        lbl_home_pf.grid(row=4, column=1, padx=10)
        lbl_away_pf = ttk.Label(self, text="Fouls", font=SMALL_FONT, foreground='white', background='black')
        lbl_away_pf.grid(row=4, column=3, padx=10)
        lbl_home_fouls = ttk.Label(self, text=f'{self.game.home_fouls}', font=SMALL_FONT,
                                   foreground='white', background='black')
        lbl_home_fouls.grid(row=5, column=1, padx=10)
        lbl_away_fouls = ttk.Label(self, text=f'{self.game.away_fouls}', font=SMALL_FONT,
                                   foreground='white', background='black')
        lbl_away_fouls.grid(row=5, column=3, padx=10)

    def time_passed(self):
        self.game_clock.run_clock()
        self.time_on_clock.set(self.game_clock.display_time_clock())


