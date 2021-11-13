class Player:
    def __init__(self, fname, lname, team):
        self.first_name = fname
        self.last_name = lname
        self.team = team
        self.games = 0
        self.minutes = 0
        self.fga = 0
        self.fgm = 0
        self.fta = 0
        self.ftm = 0
        self.tpa = 0
        self.tpm = 0
        self.oreb = 0
        self.dreb = 0
        self.assists = 0
        self.turnovers = 0
        self.steals = 0
        self.blocks = 0
        self.fouls = 0

    def play_game(self, statline):
        self.games += 1
        self.minutes += statline[0]
        self.fgm += statline[1]
        self.fga += statline[2]
        self.tpm += statline[3]
        self.tpa += statline[4]
        self.ftm += statline[5]
        self.fta += statline[6]
        self.oreb += statline[7]
        self.dreb += statline[8]
        self.assists += statline[9]
        self.turnovers += statline[10]
        self.steals += statline[11]
        self.blocks += statline[12]
        self.fouls += statline[13]

    def display_name(self):
        return f"{self.first_name} {self.last_name}"

    def display_last_name_first(self):
        return f"{self.last_name}, {self.first_name}"

    def edit_name(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    def calculate_points(self):
        return (self.fgm * 2) + self.ftm + self.tpm

    def points_per_game(self):
        if self.games == 0:
            return 0
        else:
            return round(float(self.calculate_points() / self.games), 1)

    def display_points(self, modifier):
        if modifier == 0:
            return self.calculate_points()
        elif modifier == 1:
            return self.points_per_game()
        else:
            if self.minutes == 0:
                return 0
            else:
                return round(float(self.calculate_points() / self.minutes * 40), 1)

    def calculate_rebounds(self):
        return self.oreb + self.dreb

    def rebounds_per_game(self):
        if self.games == 0:
            return 0
        else:
            return round(float(self.calculate_rebounds() / self.games), 1)

    def display_total_rebounds(self, modifier):
        if modifier == 0:
            return self.calculate_rebounds()
        elif modifier == 1:
            return self.rebounds_per_game()
        else:
            if self.minutes == 0:
                return 0
            else:
                return round(float(self.calculate_rebounds() / self.minutes * 40), 1)

    def display_off_rebounds(self, modifier):
        if self.minutes == 0 or self.games == 0:
            return 0
        else:
            if modifier == 0:
                return self.oreb
            elif modifier == 1:
                return round(float(self.oreb / self.games), 1)
            else:
                return round(float(self.oreb / self.minutes * 40), 1)

    def display_def_rebounds(self, modifier):
        if self.minutes == 0 or self.games == 0:
            return 0
        else:
            if modifier == 0:
                return self.dreb
            elif modifier == 1:
                return round(float(self.dreb / self.games), 1)
            else:
                return round(float(self.dreb / self.minutes * 40), 1)

    def display_assists(self, modifier):
        if self.minutes == 0 or self.games == 0:
            return 0
        else:
            if modifier == 0:
                return self.assists
            elif modifier == 1:
                return round(float(self.assists / self.games), 1)
            else:
                return round(float(self.assists / self.minutes * 40), 1)

    def display_steals(self, modifier):
        if self.minutes == 0 or self.games == 0:
            return 0
        else:
            if modifier == 0:
                return self.steals
            elif modifier == 1:
                return round(float(self.steals / self.games), 1)
            else:
                return round(float(self.steals / self.minutes * 40), 1)

    def display_blocks(self, modifier):
        if self.minutes == 0 or self.games == 0:
            return 0
        else:
            if modifier == 0:
                return self.blocks
            elif modifier == 1:
                return round(float(self.blocks / self.games), 1)
            else:
                return round(float(self.blocks / self.minutes * 40), 1)

    def display_turnovers(self, modifier):
        if self.minutes == 0 or self.games == 0:
            return 0
        else:
            if modifier == 0:
                return self.turnovers
            elif modifier == 1:
                return round(float(self.turnovers / self.games), 1)
            else:
                return round(float(self.turnovers / self.minutes * 40), 1)

    def display_minutes(self, modifier):
        if self.minutes == 0 or self.games == 0:
            return 0
        else:
            if modifier == 0:
                return self.minutes
            elif modifier == 1:
                return round(float(self.minutes / self.games), 1)
            else:
                return 'N/A'

    def calculate_fg_percentage(self):
        if self.fga == 0:
            return 0
        else:
            return round(float(self.fgm / self.fga * 100), 1)

    def calculate_ft_percentage(self):
        if self.fta == 0:
            return 0
        else:
            return round(float(self.ftm / self.fta * 100), 1)

    def calculate_tp_percentage(self):
        if self.tpa == 0:
            return 0
        else:
            return round(float(self.tpm / self.tpa * 100), 1
                         )

    def display_fg_splits(self):
        return f"{self.fgm}/{self.fga} - {self.calculate_fg_percentage()}%"

    def display_ft_splits(self):
        return f"{self.ftm}/{self.fta} - {self.calculate_ft_percentage()}%"

    def display_3pt_splits(self):
        return f"{self.tpm}/{self.tpa} - {self.calculate_tp_percentage()}%"

    def calculate_ATO_ratio(self):
        if self.turnovers == 0:
            return 0
        else:
            return round(float(self.assists / self.turnovers), 2)
