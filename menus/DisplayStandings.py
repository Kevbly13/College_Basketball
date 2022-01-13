from tkinter import ttk
from resources.KBFonts import *


def create_group_panel(container, conference):
    frame = ttk.Frame(container)
    conference_title = f"Group {conference.id}"
    lbl_group_name = ttk.Label(frame, text=conference_title)
    lbl_group_name.config(font=UNDERLINE_MEDIUM)
    lbl_group_name.grid(row=1, column=1, columnspan=5)
    lbl_wins = ttk.Label(frame, text='W')
    lbl_wins.grid(row=2, column=2)
    lbl_losses = ttk.Label(frame, text='L')
    lbl_losses.grid(row=2, column=3)
    lbl_pf = ttk.Label(frame, text='PF')
    lbl_pf.grid(row=2, column=4)
    lbl_pa = ttk.Label(frame, text='PA')
    lbl_pa.grid(row=2, column=5)

    sorted_teams = sorted(conference.teams, key=lambda x: (-x.wins, x.losses))
    counter = 3
    for team in sorted_teams:
        lbl_team = ttk.Label(frame, text=team.college)
        lbl_team.grid(row=counter, column=1, sticky='W')
        lbl_team_wins = ttk.Label(frame, text=team.wins)
        lbl_team_wins.grid(row=counter, column=2, padx=5)
        lbl_team_losses = ttk.Label(frame, text=team.losses)
        lbl_team_losses.grid(row=counter, column=3, padx=5)
        lbl_team_ppg = ttk.Label(frame, text=team.calculate_ppg())
        lbl_team_ppg.grid(row=counter, column=4, padx=5)
        lbl_team_pa = ttk.Label(frame, text=team.calculate_oppg())
        lbl_team_pa.grid(row=counter, column=5, padx=5)
        counter += 1

    return frame


class StandingsWindow(ttk.Frame):
    def __init__(self, parent, league):
        ttk.Frame.__init__(self, parent)
        self.league = league

        counter = 0
        for j in range(2):
            for k in range(4):
                group_container = create_group_panel(self, self.league.conferences[counter])
                group_container.grid(row=k, column=j, padx=100, pady=5, sticky="W")
                counter += 1
