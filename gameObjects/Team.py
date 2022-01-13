from Player import Player


class Team:

    def __init__(self, college, mascot):
        self.college = college
        self.nickname = mascot
        self.roster = []
        self.games = 0
        self.wins = 0
        self.losses = 0
        self.points = 0
        self.points_allowed = 0

    def calculate_win_percentage(self):
        return float(self.wins / (self.wins + self.losses))

    def calculate_ppg(self):
        if self.games == 0:
            return 0
        else:
            return round(float(self.points / self.games), 2)

    def calculate_oppg(self):
        if self.games == 0:
            return 0
        else:
            return round(float(self.points_allowed / self.games), 2)

    def play_a_game(self, team_score, opponent_score):
        self.games += 1
        self.points += team_score
        self.points_allowed += opponent_score
        if team_score > opponent_score:
            self.wins += 1
        else:
            self.losses += 1

    def add_player_to_roster(self, last_name, first_name):
        new_player = Player(first_name, last_name, self.college)
        self.roster.append(new_player)

    def is_player_on_roster(self, name_to_check):
        name_list = []
        for athlete in self.roster:
            name_list.append(f"{athlete.last_name}, {athlete.first_name}")
        for name in name_list:
            if name_to_check == name:
                return True
        return False

    def display_fg_splits(self):
        total_fgm = 0
        total_fga = 0
        for player in self.roster:
            total_fgm += player.fgm
            total_fga += player.fga
        if total_fga != 0:
            percentage = round(float(total_fgm/total_fga*100), 1)
        else:
            percentage = 0
        return f"{total_fgm}/{total_fga} - {percentage}%"

    def display_ft_splits(self):
        total_ftm = 0
        total_fta = 0
        for player in self.roster:
            total_ftm += player.ftm
            total_fta += player.fta
        if total_fta != 0:
            percentage = round(float(total_ftm/total_fta*100), 1)
        else:
            percentage = 0
        return f"{total_ftm}/{total_fta} - {percentage}%"

    def display_tp_splits(self):
        total_tpm = 0
        total_tpa = 0
        for player in self.roster:
            total_tpm += player.tpm
            total_tpa += player.tpa
        if total_tpa != 0:
            percentage = round(float(total_tpm/total_tpa*100), 1)
        else:
            percentage = 0
        return f"{total_tpm}/{total_tpa} - {percentage}%"\

    def display_total_rebounds(self, choice):
        total_rebounds = 0
        for player in self.roster:
            total_rebounds += player.oreb
            total_rebounds += player.dreb
        if choice == 0:
            return total_rebounds
        else:
            return round(float(total_rebounds / self.games), 1)

    def display_assists(self, choice):
        total = 0
        for player in self.roster:
            total += player.assists
        if choice == 0:
            return total
        else:
            return round(float(total / self.games), 1)

    def display_steals(self, choice):
        total = 0
        for player in self.roster:
            total += player.steals
        if choice == 0:
            return total
        else:
            return round(float(total / self.games), 1)

    def display_turnovers(self, choice):
        total = 0
        for player in self.roster:
            total += player.turnovers
        if choice == 0:
            return total
        else:
            return round(float(total / self.games), 1)

    def display_blocks(self, choice):
        total = 0
        for player in self.roster:
            total += player.blocks
        if choice == 0:
            return total
        else:
            return round(float(total / self.games), 1)

    def get_ordered_roster(self):
        player_list = []
        for player in self.roster:
            player_list.append(player.display_last_name_first())
        player_list.sort()
        return player_list


