import random
from BasketballGame import *


class Conference:
    def __init__(self, team_list, number):
        self.teams = team_list
        self.schedule = []
        self.make_schedule()
        self.id = number

    def make_schedule(self):
        game_list = list()
        game_list.append(BasketballGame(self.teams[0], self.teams[1]))
        game_list.append(BasketballGame(self.teams[2], self.teams[3]))
        game_list.append(BasketballGame(self.teams[0], self.teams[2]))
        game_list.append(BasketballGame(self.teams[1], self.teams[3]))
        game_list.append(BasketballGame(self.teams[0], self.teams[3]))
        game_list.append(BasketballGame(self.teams[1], self.teams[2]))

        game_list.append(BasketballGame(self.teams[1], self.teams[0]))
        game_list.append(BasketballGame(self.teams[3], self.teams[2]))
        game_list.append(BasketballGame(self.teams[2], self.teams[0]))
        game_list.append(BasketballGame(self.teams[3], self.teams[1]))
        game_list.append(BasketballGame(self.teams[3], self.teams[0]))
        game_list.append(BasketballGame(self.teams[2], self.teams[1]))

        random.shuffle(game_list)
        self.schedule = game_list

    def display_schedule(self):
        counter = 0
        for game in self.schedule:
            counter += 1
            print(f"Game {counter}: {game.display_info()}")

    def get_next_game(self):
        for game in self.schedule:
            if not game.is_played:
                return game
        print("No games available")

    def display_standings(self):
        print("-----------------------")
        print("Team\t\t\tW\tL")
        print("-----------------------")

        sorted_teams = sorted(self.teams, key=lambda x: (-x.wins, x.losses))
        for team in sorted_teams:
            print('{0:15} {1:1d}\t{2:1d}'.format(team.college, team.wins, team.losses))
