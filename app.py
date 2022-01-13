from tkinter import *
from tkinter import ttk
from resources.KBFonts import TITLE_FONT
from menus.DisplayStandings import StandingsWindow
from menus.DisplayScheduler import ScheduleWindow
from menus.LeagueLeaders import LeadersWindow
from menus.TeamStats import TeamStatsWindow
from gameObjects.League import load_league


class StartMenu(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.img = PhotoImage(file='resources/burke.png')

        lbl_title = ttk.Label(self, text="NCAA Basketball Organizer 2018-19")
        lbl_title.config(font=TITLE_FONT)
        lbl_title.grid(row=1, column=1, padx=20, sticky="E")
        ttk.Label(self, image=self.img, compound='image').grid(row=2, column=1, padx=20, pady=30)


def college_basketball_app(root):
    ncaa = load_league()

    tab_manager = ttk.Notebook(root)
    tab_manager.grid(column=1, row=1)
    start_frame = StartMenu(root)
    standings_frame = StandingsWindow(root, ncaa)
    schedule_frame = ScheduleWindow(root, ncaa)
    leaders_frame = LeadersWindow(root, ncaa)
    team_stats_frame = TeamStatsWindow(root, ncaa)
    tab_manager.add(start_frame, text="Start Menu")
    tab_manager.add(standings_frame, text="Standings")
    tab_manager.add(schedule_frame, text="Schedule")
    tab_manager.add(leaders_frame, text="Leaders")
    tab_manager.add(team_stats_frame, text="Team Stats")


def main():
    root = Tk()
    root.title("College Basketball Organizer")

    window_width = 850
    window_height = 600
    center_x = int(root.winfo_screenwidth()/2 - window_width/2)
    center_y = int(root.winfo_screenheight()/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    college_basketball_app(root)
    root.mainloop()


if __name__ == "__main__":
    main()
