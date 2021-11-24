from GameStatSheet import GameClock


class BasketballGame:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_lineup = []
        self.away_lineup = []
        self.is_played = False
        self.home_score = 0
        self.away_score = 0
        self.possession_arrow_to_home = True
        self.home_fouls = 0
        self.away_fouls = 0
        self.home_timeouts = 3
        self.away_timeouts = 3
        self.half = 1
        self.game_clock = GameClock(20)

    def start_game(self):
        self.home_score = 0
        self.away_score = 0
        self.home_lineup = []
        self.away_lineup = []
        self.possession_arrow_to_home = True
        self.home_fouls = 0
        self.away_fouls = 0
        self.home_timeouts = 3
        self.away_timeouts = 3
        self.half = 1
        self.game_clock = GameClock(20)

    def save_game_result(self):
        self.is_played = True
        self.home_team.play_a_game(self.home_score, self.away_score)
        self.away_team.play_a_game(self.away_score, self.home_score)

    def display_game_result(self):
        if self.is_played:
            if self.home_score > self.away_score:
                return f"{self.home_team.college} defeated {self.away_team.college} by " \
                       f"{self.home_score - self.away_score} points "
            else:
                return f"{self.away_team.college} defeated {self.home_team.college} by " \
                       f"{self.away_score - self.home_score} points"
        else:
            return "The game has not yet been played"

    def display_info(self):
        if self.is_played:
            return self.display_game_result()
        else:
            return f"{self.away_team.college} {self.away_team.nickname} at " \
                   f"{self.home_team.college} {self.home_team.nickname}"

