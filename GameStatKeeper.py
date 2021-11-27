from tkinter import *
from tkinter import ttk


def player_list_does_not_contain_null(combo_boxes):
    player_list = []
    for cb_player in combo_boxes:
        player_list.append(cb_player.get())
    if "" in player_list:
        return False
    else:
        return True


def player_list_is_unique(combo_boxes):
    player_list = []
    for cb_player in combo_boxes:
        player_list.append(cb_player.get())
    if len(set(player_list)) == len(player_list):
        return True
    else:
        return False


class StartingLineupFrame(ttk.Frame):
    def __init__(self, stat_keeper_obj):
        ttk.Frame.__init__(self, stat_keeper_obj)
        self.parent = stat_keeper_obj
        self.combo_boxes = []
        self.home_selections = []
        self.away_selections = []
        self.game = stat_keeper_obj.game

        self.init_combo_boxes()
        self.lbl_home = ttk.Label(self, text=self.game.home_team.college).grid(row=0, column=0)
        self.lbl_away = ttk.Label(self, text=self.game.away_team.college).grid(row=0, column=1)
        self.btn_set = ttk.Button(self, text="Line-up Set", command=self.check_lineup)
        self.btn_set.grid(row=7, column=0, columnspan=2, pady=10)

    def init_combo_boxes(self):
        home_combo_boxes = []
        away_combo_boxes = []

        for i in range(5):
            self.home_selections.append(StringVar())
            home_combo_boxes.append(ttk.Combobox(self, values=self.game.home_team.get_ordered_roster(),
                                                 textvariable=self.home_selections[i],
                                                 state="readonly"))
        for i in range(len(home_combo_boxes)):
            home_combo_boxes[i].grid(row=i + 1, column=0, padx=10, pady=5)
            home_combo_boxes[i].current(i)

        for i in range(5):
            self.away_selections.append(StringVar())
            away_combo_boxes.append(
                ttk.Combobox(self, values=self.game.away_team.get_ordered_roster(),
                             textvariable=self.away_selections[i],
                             state="readonly"))
        for i in range(len(away_combo_boxes)):
            away_combo_boxes[i].grid(row=i + 1, column=1, padx=10, pady=5)
            away_combo_boxes[i].current(i)

        self.combo_boxes = away_combo_boxes + home_combo_boxes

    def check_lineup(self):
        if player_list_is_unique(self.combo_boxes) and player_list_does_not_contain_null(self.combo_boxes):
            print("Line-up Checks Out")
            for var in self.home_selections:
                player_name = var.get()
                for player in self.game.home_team.roster:
                    if player.display_last_name_first() == player_name:
                        self.game.home_lineup.append(player)
            for var in self.away_selections:
                player_name = var.get()
                for player in self.game.away_team.roster:
                    if player.display_last_name_first() == player_name:
                        self.game.away_lineup.append(player)
            self.parent.switch_frame(JumpBallFrame)
        else:
            print("Does not check out")


class JumpBallFrame(ttk.Frame):
    def __init__(self, stat_keeper_obj):
        ttk.Frame.__init__(self, stat_keeper_obj)
        self.master = stat_keeper_obj
        self.game = stat_keeper_obj.game
        self.home_player_buttons = []
        self.away_player_buttons = []

        self.init_buttons()

    def init_buttons(self):
        for player in self.game.home_lineup:
            self.home_player_buttons.append(Button(self, text=player.display_last_name_first()))
        for player in self.game.away_lineup:
            self.away_player_buttons.append(Button(self, text=player.display_last_name_first()))

        r = 0
        for btn in self.home_player_buttons:
            btn.grid(row=r, column=0, padx=10, pady=7)
            r += 1
        r = 0
        for btn in self.away_player_buttons:
            btn.grid(row=r, column=1, padx=10, pady=7)
            r += 1


class GameStatKeeper(Toplevel):
    def __init__(self, active_game):
        Toplevel.__init__(self)
        self.title("College Basketball Game Stat Keeper")

        window_width = 850
        window_height = 600
        center_x = int(self.winfo_screenwidth() / 2 - window_width / 2)
        center_y = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.game = active_game
        self.game.start_game()

        self._frame = None
        self.switch_frame(StartingLineupFrame)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0)

    def dismiss(self):
        self.grab_release()
        self.destroy()
