from tkinter import *
from Scoreboard import *
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


class StatSheetWindow(Toplevel):
    def __init__(self, current_game):
        Toplevel.__init__(self)
        self.combo_boxes = []
        self.current_game = current_game

        self.init_window()
        self.btn_set = ttk.Button(self, text="Line-up Set", command=self.check_lineup)
        self.btn_set.grid(row=6, column=1)
        self.btn_jump_ball = ttk.Button(self, text="Jump Ball", command=self.jump_ball, state=DISABLED)
        self.btn_jump_ball.grid(row=7, column=1)

    def init_window(self):
        self.title("Play Game")
        self.geometry("850x600")
        self.tkraise()

        self.current_game.start_game()

        score_board = Scoreboard(self, self.current_game)
        score_board.grid(row=0, column=1, rowspan=5, padx=20, pady=20)

        self.init_combo_boxes()

    def init_combo_boxes(self):
        home_combo_boxes = []
        away_combo_boxes = []
        for i in range(5):
            self.current_game.home_lineup.append(StringVar())
            home_combo_boxes.append(ttk.Combobox(self, values=self.current_game.home_team.get_ordered_roster(),
                                                 textvariable=self.current_game.home_lineup[i],
                                                 state="readonly"))
        for i in range(len(home_combo_boxes)):
            home_combo_boxes[i].grid(row=i, column=0, padx=5, pady=5)

        for i in range(5):
            self.current_game.away_lineup.append(StringVar())
            away_combo_boxes.append(
                ttk.Combobox(self, values=self.current_game.away_team.get_ordered_roster(),
                             textvariable=self.current_game.away_lineup[i],
                             state="readonly"))
        for i in range(len(away_combo_boxes)):
            away_combo_boxes[i].grid(row=i, column=2, padx=5, pady=5)

        self.combo_boxes = away_combo_boxes + home_combo_boxes

    def jump_ball(self):
        jump_ball_result = JumpBallWindow(self).show()
        print(jump_ball_result)
        if jump_ball_result == "Home":
            self.current_game.possession_arrow_to_home = False
        else:
            self.current_game.possession_arrow_to_home = True
        self.btn_jump_ball.state(["disabled"])

    def check_lineup(self):
        if player_list_is_unique(self.combo_boxes) and player_list_does_not_contain_null(self.combo_boxes):
            print("Line-up Checks Out")
            self.btn_jump_ball.state(["!disabled"])
            self.btn_set.state(["disabled"])
        else:
            print("Does not check out")

    def dismiss(self):
        self.grab_release()
        self.destroy()


class GameClock:
    def __init__(self, minutes_per_half):
        self.minutes = minutes_per_half
        self.seconds = 0
        self.interval_of_seconds = 12

    # This method should be outside of the class
    def run_clock(self):
        if self.seconds < self.interval_of_seconds:
            self.minutes -= 1
            self.seconds += 60
        self.seconds -= self.interval_of_seconds
        # increment player minutes played from a list of players in game

    def time_left_on_clock(self):
        if self.minutes <= 0 and self.seconds <= 0:
            return False
        else:
            return True

    def display_time_clock(self):
        minute = "{0:0=2d}".format(self.minutes)
        sec = "{0:0=2d}".format(self.seconds)
        return f"{minute}:{sec}"


class JumpBallWindow(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.var = StringVar()

        self.title("Jump Ball")
        message = "Which Team Won the Jump Ball?"
        Label(self, text=message).pack(padx=10, pady=3)
        Button(self, text="Home", command=self.home).pack(pady=3)
        Button(self, text="Away", command=self.away).pack(pady=3)

    def home(self):
        self.var = "Home"
        self.destroy()

    def away(self):
        self.var = "Away"
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.wait_window()
        return self.var
