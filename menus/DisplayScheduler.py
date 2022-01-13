from tkinter import ttk, messagebox
from tkinter import *
import random
from GameStatKeeper import GameStatKeeper
from gameObjects.League import save_league
from resources.KBFonts import *


def create_group_panel(container, group):
    frame = ttk.Frame(container)
    conference_title = f"Group {group.id}"
    
    lbl_group_name = ttk.Label(frame, text=conference_title)
    lbl_group_name.config(font=UNDERLINE_MEDIUM)
    lbl_group_name.grid(row=1, column=1)

    game_info = ""

    for game in group.schedule:
        if not game.is_played:
            game_info = game.display_info()
            break
    rb_game = ttk.Radiobutton(frame, text=game_info, variable=container.v_choice, value=group.id)
    rb_game['style'] = 'Display.TRadiobutton'
    rb_game.grid(row=2, column=1)

    return frame


class ScheduleWindow(ttk.Frame):
    def __init__(self, root, league):
        ttk.Frame.__init__(self, root)
        self.root = root

        self.league = league
        self.v_choice = IntVar()
        self.v_choice.set(1)

        counter = 0
        for j in range(2):
            for k in range(4):
                group_container = create_group_panel(self, self.league.conferences[counter])
                group_container.grid(row=k + 1, column=j + 1, padx=20, pady=20)
                counter += 1

        btn_random = ttk.Button(self, text="Random", command=self.random_selection, width=20)
        btn_random.grid(row=6, column=1, pady=15)
        btn_play_game = ttk.Button(self, text='Play Game', command=self.start_game, width=20)
        btn_play_game.grid(row=6, column=2, pady=15)

    def random_selection(self):
        self.v_choice.set(random.randint(1, 8))

    def start_game(self):
        choice = self.v_choice.get()
        active_game = self.league.conferences[choice - 1].get_next_game()
        active_game.home_score = 0
        active_game.away_score = 0

        new_root = GameStatKeeper(active_game)
        new_root.lift()

        if active_game.home_score != 0 and active_game.away_score != 0:
            active_game.save_game_result()
            messagebox.showinfo('Game Result', active_game.display_game_result())

            save_league(self.league)

            self.parent.destroy()
