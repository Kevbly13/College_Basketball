from tkinter import ttk
from tkinter import *
from KBFonts import *


def sort_players(player_list, selected_stat):
    if selected_stat == 'points':
        sorted_list = sorted(player_list, key=lambda x: x.display_points(1), reverse=True)
        return sorted_list
    if selected_stat == 'rebounds':
        sorted_list = sorted(player_list, key=lambda x: x.display_total_rebounds(1), reverse=True)
        return sorted_list
    if selected_stat == 'assists':
        sorted_list = sorted(player_list, key=lambda x: x.display_assists(1), reverse=True)
        return sorted_list
    if selected_stat == 'steals':
        sorted_list = sorted(player_list, key=lambda x: x.display_steals(1), reverse=True)
        return sorted_list
    if selected_stat == 'blocks':
        sorted_list = sorted(player_list, key=lambda x: x.display_blocks(1), reverse=True)
        return sorted_list
    if selected_stat == 'fgp':
        sorted_list = sorted(player_list, key=lambda x: x.calculate_fg_percentage(), reverse=True)
        return sorted_list
    if selected_stat == 'ftp':
        sorted_list = sorted(player_list, key=lambda x: x.calculate_ft_percentage(), reverse=True)
        return sorted_list
    if selected_stat == 'tpp':
        sorted_list = sorted(player_list, key=lambda x: x.calculate_tp_percentage(), reverse=True)
        return sorted_list


class LeadersWindow(ttk.Frame):
    def __init__(self, parent, league):
        ttk.Frame.__init__(self, parent)
        self.league = league
        self.number_of_records = 20

        self.stat_choice = StringVar()
        self.create_radio_buttons()
        self.stat_choice.set('points')

        self.player_list = sort_players(self.league.get_all_players(), self.stat_choice.get())
        self.player_rank_list = []
        self.player_team_list = []
        self.player_stat_list = []
        for n in range(self.number_of_records):
            self.player_rank_list.append(StringVar())
            self.player_team_list.append(StringVar())
            self.player_stat_list.append(IntVar())
        self.update_lists()
        self.create_label_grid()

    def update_lists(self):
        for j in range(self.number_of_records):
            self.player_rank_list[j].set(self.player_list[j].display_name())
            self.player_team_list[j].set(self.player_list[j].team)
            if self.stat_choice.get() == 'points':
                self.player_stat_list[j].set(self.player_list[j].display_points(1))
            if self.stat_choice.get() == 'rebounds':
                self.player_stat_list[j].set(self.player_list[j].display_total_rebounds(1))
            if self.stat_choice.get() == 'assists':
                self.player_stat_list[j].set(self.player_list[j].display_assists(1))
            if self.stat_choice.get() == 'steals':
                self.player_stat_list[j].set(self.player_list[j].display_steals(1))
            if self.stat_choice.get() == 'blocks':
                self.player_stat_list[j].set(self.player_list[j].display_blocks(1))
            if self.stat_choice.get() == 'fgp':
                self.player_stat_list[j].set(self.player_list[j].calculate_fg_percentage())
            if self.stat_choice.get() == 'ftp':
                self.player_stat_list[j].set(self.player_list[j].calculate_ft_percentage())
            if self.stat_choice.get() == 'tpp':
                self.player_stat_list[j].set(self.player_list[j].calculate_tp_percentage())

    def change(self):
        self.player_list = sort_players(self.player_list, self.stat_choice.get())
        self.update_lists()

    def create_radio_buttons(self):
        ttk.Radiobutton(self, text="Points", variable=self.stat_choice, value='points', command=self.change) \
            .grid(row=1, column=2, pady=15)
        ttk.Radiobutton(self, text="Rebounds", variable=self.stat_choice, value='rebounds', command=self.change) \
            .grid(row=1, column=3, pady=15)
        ttk.Radiobutton(self, text="Assists", variable=self.stat_choice, value='assists', command=self.change) \
            .grid(row=1, column=4, pady=15)
        ttk.Radiobutton(self, text="Steals", variable=self.stat_choice, value='steals', command=self.change) \
            .grid(row=1, column=5, pady=15)
        ttk.Radiobutton(self, text="Blocks", variable=self.stat_choice, value='blocks', command=self.change) \
            .grid(row=1, column=6, pady=15)
        ttk.Radiobutton(self, text="FG%", variable=self.stat_choice, value='fgp', command=self.change) \
            .grid(row=1, column=7, pady=15)
        ttk.Radiobutton(self, text="FT%", variable=self.stat_choice, value='ftp', command=self.change) \
            .grid(row=1, column=8, pady=15)
        ttk.Radiobutton(self, text="3pt%", variable=self.stat_choice, value='tpp', command=self.change) \
            .grid(row=1, column=9, pady=15)

    def create_label_grid(self):
        for k in range(self.number_of_records):
            ttk.Label(self, textvariable=self.player_rank_list[k], font=SMALL_FONT).grid(row=k + 2, column=1, padx=25)
            ttk.Label(self, textvariable=self.player_team_list[k], font=SMALL_FONT).grid(row=k + 2, column=2)
            ttk.Label(self, textvariable=self.player_stat_list[k], font=SMALL_FONT).grid(row=k + 2, column=3)





