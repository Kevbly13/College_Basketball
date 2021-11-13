from tkinter import ttk
from tkinter import *
from KBFonts import *


class TeamStatsWindow(ttk.Frame):
    def __init__(self, parent, league):
        ttk.Frame.__init__(self, parent)
        self.league = league
        self.team_list = []
        for team in self.league.team_list:
            self.team_list.append(team.college)

        active_team = self.league.team_list[0]
        self.v_choice = IntVar()
        self.v_choice.set(0)

        self.stat_grid = DataTablePanel(self, active_team, self.v_choice.get())
        self.stat_grid.grid(row=4, column=1, columnspan=5, padx=15)

        self.cb_team = ttk.Combobox(self, values=self.team_list, state='readonly')
        self.cb_team.current(0)
        self.cb_team.grid(row=1, column=1, pady=20, padx=10)
        self.rb_total = ttk.Radiobutton(self, text="Total", variable=self.v_choice, value=0).grid(row=1, column=2)
        self.rb_per_game = ttk.Radiobutton(self, text="Per Game", variable=self.v_choice, value=1).grid(row=1, column=3)
        self.rb_per40 = ttk.Radiobutton(self, text="Per 40", variable=self.v_choice, value=2).grid(row=1, column=4)

        ttk.Button(self, text="Refresh", command=self.callback).grid(row=1, column=5)

    def callback(self):
        active_team = self.league.team_list[0]
        for team in self.league.team_list:
            if team.college == self.cb_team.get():
                active_team = team
        self.stat_grid.update_grid(self, active_team, self.v_choice.get())


class DataTablePanel(ttk.Frame):
    def __init__(self, parent, team, display_option):
        ttk.Frame.__init__(self, parent)
        self.lbl_name = []
        self.lbl_fg = []
        self.lbl_ft = []
        self.lbl_3pt = []
        self.lbl_oreb = []
        self.lbl_dreb = []
        self.lbl_treb = []
        self.lbl_ast = []
        self.lbl_to = []
        self.lbl_ato = []
        self.lbl_stl = []
        self.lbl_blk = []
        self.lbl_min = []
        self.lbl_pts = []

        self.display_labels()
        self.v_choice = display_option

        team.roster.sort(key=lambda x: x.display_points(self.v_choice), reverse=True)

        for player in team.roster:
            self.lbl_name.append(ttk.Label(self, font=SMALL_FONT, text=player.display_name()))
            self.lbl_fg.append(ttk.Label(self, font=SMALL_FONT, text=player.display_fg_splits()))
            self.lbl_ft.append(ttk.Label(self, font=SMALL_FONT, text=player.display_ft_splits()))
            self.lbl_3pt.append(ttk.Label(self, font=SMALL_FONT, text=player.display_3pt_splits()))
            self.lbl_oreb.append(ttk.Label(self, font=SMALL_FONT, text=player.display_off_rebounds(self.v_choice)))
            self.lbl_dreb.append(ttk.Label(self, font=SMALL_FONT, text=player.display_def_rebounds(self.v_choice)))
            self.lbl_treb.append(ttk.Label(self, font=SMALL_FONT, text=player.display_total_rebounds(self.v_choice)))
            self.lbl_ast.append(ttk.Label(self, font=SMALL_FONT, text=player.display_assists(self.v_choice)))
            self.lbl_to.append(ttk.Label(self, font=SMALL_FONT, text=player.display_turnovers(self.v_choice)))
            self.lbl_ato.append(ttk.Label(self, font=SMALL_FONT, text=player.calculate_ATO_ratio()))
            self.lbl_stl.append(ttk.Label(self, font=SMALL_FONT, text=player.display_steals(self.v_choice)))
            self.lbl_blk.append(ttk.Label(self, font=SMALL_FONT, text=player.display_blocks(self.v_choice)))
            self.lbl_min.append(ttk.Label(self, font=SMALL_FONT, text=player.display_minutes(self.v_choice)))
            self.lbl_pts.append(ttk.Label(self, font=SMALL_FONT, text=player.display_points(self.v_choice)))
        for n in range(len(team.roster)):
            active_row = n+4
            self.lbl_name[n].grid(row=active_row, column=1, sticky="W", padx=4)
            self.lbl_fg[n].grid(row=active_row, column=3, sticky="W", padx=4)
            self.lbl_ft[n].grid(row=active_row, column=4, sticky="W", padx=4)
            self.lbl_3pt[n].grid(row=active_row, column=5, sticky="W", padx=4)
            self.lbl_oreb[n].grid(row=active_row, column=7, padx=4)
            self.lbl_dreb[n].grid(row=active_row, column=8, padx=4)
            self.lbl_treb[n].grid(row=active_row, column=9, padx=4)
            self.lbl_ast[n].grid(row=active_row, column=11)
            self.lbl_to[n].grid(row=active_row, column=12)
            self.lbl_ato[n].grid(row=active_row, column=13)
            self.lbl_stl[n].grid(row=active_row, column=14)
            self.lbl_blk[n].grid(row=active_row, column=15)
            self.lbl_min[n].grid(row=active_row, column=16)
            self.lbl_pts[n].grid(row=active_row, column=17)
        self.insert_team_stats(team)

    def insert_team_stats(self, team):
        ttk.Label(self, text="TEAM", font=SMALL_BOLD).grid(row=len(team.roster)+5, column=1, sticky="W", padx=4)
        ttk.Label(self, text=team.display_fg_splits(), font=SMALL_BOLD).\
            grid(row=len(team.roster)+5, column=3, sticky="W", padx=4)
        ttk.Label(self, text=team.display_ft_splits(), font=SMALL_BOLD). \
            grid(row=len(team.roster) + 5, column=4, sticky="W", padx=4)
        ttk.Label(self, text=team.display_tp_splits(), font=SMALL_BOLD). \
            grid(row=len(team.roster) + 5, column=5, sticky="W", padx=4)
        ttk.Label(self, text=team.display_total_rebounds(self.v_choice), font=SMALL_BOLD). \
            grid(row=len(team.roster) + 5, column=9, padx=4)
        ttk.Label(self, text=team.display_assists(self.v_choice), font=SMALL_BOLD). \
            grid(row=len(team.roster) + 5, column=11)
        ttk.Label(self, text=team.display_turnovers(self.v_choice), font=SMALL_BOLD). \
            grid(row=len(team.roster) + 5, column=12)
        ttk.Label(self, text=team.display_steals(self.v_choice), font=SMALL_BOLD). \
            grid(row=len(team.roster) + 5, column=14)
        ttk.Label(self, text=team.display_blocks(self.v_choice), font=SMALL_BOLD). \
            grid(row=len(team.roster) + 5, column=15)

    def update_grid(self, parent, new_team, display_option):
        self.destroy()
        self.__init__(parent, new_team, display_option)
        self.grid(row=4, column=1, columnspan=5, padx=15)

    def display_labels(self):
        ttk.Label(self, text="Shooting", font=SMALL_BOLD).grid(row=1, column=3, columnspan=3)
        ttk.Label(self, text="Rebounds", font=SMALL_BOLD).grid(row=1, column=7, columnspan=3)
        ttk.Label(self, text="FG", font=SMALL_BOLD).grid(row=2, column=3, padx=5)
        ttk.Label(self, text="FT", font=SMALL_BOLD).grid(row=2, column=4, padx=5)
        ttk.Label(self, text="3pt", font=SMALL_BOLD).grid(row=2, column=5, padx=5)
        ttk.Label(self, text="O", font=SMALL_BOLD).grid(row=2, column=7, padx=5)
        ttk.Label(self, text="D", font=SMALL_BOLD).grid(row=2, column=8, padx=5)
        ttk.Label(self, text="T", font=SMALL_BOLD).grid(row=2, column=9, padx=5)
        ttk.Label(self, text="A", font=SMALL_BOLD).grid(row=2, column=11, padx=5)
        ttk.Label(self, text="TO", font=SMALL_BOLD).grid(row=2, column=12, padx=5)
        ttk.Label(self, text="A/TO", font=SMALL_BOLD).grid(row=2, column=13, padx=5)
        ttk.Label(self, text="Stl", font=SMALL_BOLD).grid(row=2, column=14, padx=5)
        ttk.Label(self, text="Blk", font=SMALL_BOLD).grid(row=2, column=15, padx=5)
        ttk.Label(self, text="Min", font=SMALL_BOLD).grid(row=2, column=16, padx=5)
        ttk.Label(self, text="Pts", font=SMALL_BOLD).grid(row=2, column=17, padx=5)
        ttk.Separator(self, orient=VERTICAL).grid(column=2, row=1, rowspan=25, padx=5, sticky="NS")
        ttk.Separator(self, orient=VERTICAL).grid(column=6, row=1, rowspan=25, padx=5, sticky="NS")
        ttk.Separator(self, orient=VERTICAL).grid(column=10, row=1, rowspan=25, padx=5, sticky="NS")
        ttk.Separator(self, orient=HORIZONTAL).grid(column=1, row=3, columnspan=25, pady=2, sticky="EW")
