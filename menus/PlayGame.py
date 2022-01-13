from tkinter import *
from tkinter import ttk
from tkinter import font
import easygui as gui


class GameWindow(Toplevel):
    def __init__(self, current_team):
        Toplevel.__init__(self)
        self.active_team = current_team
        self.players_played = int(gui.integerbox(msg=f"How many players played for {self.active_team.college}",
                                                 title='Number of players', lowerbound=5, upperbound=14))

        self.combo_boxes = []
        self.ordered_player_list = []
        self.min_result = []
        self.fgm_result = []
        self.fga_result = []
        self.ftm_result = []
        self.fta_result = []
        self.tpm_result = []
        self.tpa_result = []
        self.oreb_result = []
        self.dreb_result = []
        self.ast_result = []
        self.stl_result = []
        self.blk_result = []
        self.to_result = []
        self.pf_result = []
        self.points = []
        self.initialize_results()
        self.btn_exit = ttk.Button(self, text='Exit', width=20)
        self.btn_save = ttk.Button(self, text='Save', command=self.save_state, width=20)
        self.btn_validate = ttk.Button(self, text='Validate', command=self.validate, width=20)

        self.title("Play Game")
        self.geometry("550x400")
        self.tkraise()

        self.add_labels()
        self.create_grid()
        self.create_buttons()

    def dismiss(self):
        self.grab_release()
        self.destroy()

    def update_points(self, index):
        total_points = self.fgm_result[index].get() * 2 + self.ftm_result[index].get() + self.tpm_result[index].get()
        self.points[index].config(text=f"{total_points}")

    def initialize_results(self):
        for i in range(self.players_played):
            self.ordered_player_list.append(StringVar())
            self.min_result.append(IntVar())
            self.fgm_result.append(IntVar())
            self.fga_result.append(IntVar())
            self.ftm_result.append(IntVar())
            self.fta_result.append(IntVar())
            self.tpm_result.append(IntVar())
            self.tpa_result.append(IntVar())
            self.oreb_result.append(IntVar())
            self.dreb_result.append(IntVar())
            self.ast_result.append(IntVar())
            self.stl_result.append(IntVar())
            self.blk_result.append(IntVar())
            self.to_result.append(IntVar())
            self.pf_result.append(IntVar())

    def add_labels(self):
        f1 = font.Font(family="Times", size=18, weight="bold")
        ttk.Label(self, text=f"{self.active_team.college} {self.active_team.nickname}", font=f1) \
            .grid(column=0, row=0, columnspan=14)
        ttk.Label(self, text="Min").grid(column=1, row=2)
        ttk.Label(self, text="FG").grid(column=2, row=2, columnspan=2)
        ttk.Label(self, text="FT").grid(column=4, row=2, columnspan=2)
        ttk.Label(self, text="3-PT").grid(column=6, row=2, columnspan=2)
        ttk.Label(self, text="Reb").grid(column=8, row=2, columnspan=2)
        ttk.Label(self, text="Ast").grid(column=10, row=2)
        ttk.Label(self, text="Stl").grid(column=11, row=2)
        ttk.Label(self, text="Blk").grid(column=12, row=2)
        ttk.Label(self, text="TO").grid(column=13, row=2)
        ttk.Label(self, text="PF").grid(column=14, row=2)
        ttk.Label(self, text="Pts").grid(column=15, row=2)

    def create_grid(self):
        player_list = []
        for player in self.active_team.roster:
            player_list.append(player.display_last_name_first())
        player_list.sort()
        minutes = []
        fga = []
        fgm = []
        fta = []
        ftm = []
        tpa = []
        tpm = []
        oreb = []
        dreb = []
        assists = []
        stl = []
        blk = []
        turnovers = []
        pf = []

        for i in range(self.players_played):
            self.combo_boxes.append(ttk.Combobox(self, values=player_list, textvariable=self.ordered_player_list[i],
                                                 state="readonly"))
            minutes.append(ttk.Entry(self, textvariable=self.min_result[i], width=3))
            fgm.append(ttk.Entry(self, width=3, textvariable=self.fgm_result[i]))
            fga.append(ttk.Entry(self, width=3, textvariable=self.fga_result[i]))
            ftm.append(ttk.Entry(self, width=3, textvariable=self.ftm_result[i]))
            fta.append(ttk.Entry(self, width=3, textvariable=self.fta_result[i]))
            tpm.append(ttk.Entry(self, width=3, textvariable=self.tpm_result[i]))
            tpa.append(ttk.Entry(self, width=3, textvariable=self.tpa_result[i]))
            oreb.append(ttk.Entry(self, width=3, textvariable=self.oreb_result[i]))
            dreb.append(ttk.Entry(self, width=3, textvariable=self.dreb_result[i]))
            assists.append(ttk.Entry(self, width=3, textvariable=self.ast_result[i]))
            stl.append(ttk.Entry(self, width=3, textvariable=self.stl_result[i]))
            blk.append(ttk.Entry(self, width=3, textvariable=self.blk_result[i]))
            turnovers.append(ttk.Entry(self, width=3, textvariable=self.to_result[i]))
            pf.append(ttk.Entry(self, width=3, textvariable=self.pf_result[i]))
            self.points.append(ttk.Label(self, text='0'))

        for j in range(self.players_played):
            self.combo_boxes[j].grid(column=0, row=j + 3, padx=5)
            minutes[j].grid(column=1, row=j + 3)
            fgm[j].grid(column=2, row=j + 3)
            fga[j].grid(column=3, row=j + 3)
            ftm[j].grid(column=4, row=j + 3)
            fta[j].grid(column=5, row=j + 3)
            tpm[j].grid(column=6, row=j + 3)
            tpa[j].grid(column=7, row=j + 3)
            oreb[j].grid(column=8, row=j + 3)
            dreb[j].grid(column=9, row=j + 3)
            assists[j].grid(column=10, row=j + 3)
            stl[j].grid(column=11, row=j + 3)
            blk[j].grid(column=12, row=j + 3)
            turnovers[j].grid(column=13, row=j + 3)
            pf[j].grid(column=14, row=j + 3)
            self.points[j].grid(column=15, row=j + 3)
            fgm[j].bind('<Key>', lambda event, index=j: self.update_points(index))
            ftm[j].bind('<Key>', lambda event, index=j: self.update_points(index))
            tpm[j].bind('<Key>', lambda event, index=j: self.update_points(index))

        for k in range(self.players_played):
            self.min_result[k].set(0)
            self.fgm_result[k].set(0)
            self.fga_result[k].set(0)
            self.ftm_result[k].set(0)
            self.fta_result[k].set(0)
            self.tpm_result[k].set(0)
            self.tpa_result[k].set(0)
            self.oreb_result[k].set(0)
            self.dreb_result[k].set(0)
            self.ast_result[k].set(0)
            self.stl_result[k].set(0)
            self.blk_result[k].set(0)
            self.to_result[k].set(0)
            self.pf_result[k].set(0)

    def validate(self):
        if self.check_players_unique() and self.check_players_null() and self.check_personal_foul_limit() \
                and self.check_attempts_more_than_makes():
            self.btn_save.config(state='!disabled')

    def create_buttons(self):
        self.btn_exit.grid(column=0, row=self.players_played + 3, columnspan=14, pady=5)
        self.btn_validate.grid(column=0, row=self.players_played + 4, columnspan=14, pady=5)
        self.btn_save.grid(column=0, row=self.players_played + 5, columnspan=14, pady=5)
        self.btn_save.config(state='disabled')

    def check_players_unique(self):
        player_list = []
        for cb_player in self.combo_boxes:
            player_list.append(cb_player.get())
        if len(set(player_list)) == len(player_list):
            return True
        else:
            return False

    def check_players_null(self):
        player_list = []
        for cb_player in self.combo_boxes:
            player_list.append(cb_player.get())
        return not "" in player_list

    def check_personal_foul_limit(self):
        for pf in self.pf_result:
            if pf.get() > 5:
                return False
        return True

    def check_attempts_more_than_makes(self):
        for k in range(self.players_played):
            if self.fgm_result[k].get() > self.fga_result[k].get():
                return False
            if self.ftm_result[k].get() > self.fta_result[k].get():
                return False
            if self.tpm_result[k].get() > self.tpa_result[k].get():
                return False
            if self.tpm_result[k].get() > self.fgm_result[k].get():
                return False
            if self.tpa_result[k].get() > self.fga_result[k].get():
                return False
        return True

    def save_state(self):
        for k in range(self.players_played):
            for player in self.active_team.roster:
                if player.display_last_name_first() == self.ordered_player_list[k].get():
                    self.save_player(player, k)
                    self.active_team.game_points += (self.fgm_result[k].get() * 2 + self.ftm_result[k].get()
                                                     + self.tpm_result[k].get())
        print(f"{self.active_team.college} scored {self.active_team.game_points} points")
        self.destroy()

    def save_player(self, player_to_save, num):
        stat_line = [self.min_result[num].get(),
                     self.fgm_result[num].get(),
                     self.fga_result[num].get(),
                     self.tpm_result[num].get(),
                     self.tpa_result[num].get(),
                     self.ftm_result[num].get(),
                     self.fta_result[num].get(),
                     self.oreb_result[num].get(),
                     self.dreb_result[num].get(),
                     self.ast_result[num].get(),
                     self.to_result[num].get(),
                     self.stl_result[num].get(),
                     self.blk_result[num].get(),
                     self.pf_result[num].get(),
                     ]
        player_to_save.play_game(stat_line)
