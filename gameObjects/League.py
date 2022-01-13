import pickle
import csv
import random
from Team import Team
from gameObjects.Conference import Conference


def load_league():
    with open('../data/league.pickle', mode='rb') as f:
        league = pickle.load(f)
    league.sort_teams()
    return league


def save_league(league):
    with open('../data/league.pickle', mode='wb') as f:
        pickle.dump(league, f)


def add_team_players(team):
    with open("../data/player_list.csv", mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=",", skipinitialspace=True)

        for row in reader:
            if row[2] == team.college:
                team.add_player_to_roster(row[1], row[0])


class League:
    def __init__(self):
        self.conferences = []
        self.team_list = []

    def sort_teams(self):
        self.team_list.sort(key=lambda x: x.college, reverse=False)

    def start_a_new_league(self, filename):
        self.conferences.clear()
        self.team_list.clear()

        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=",", skipinitialspace=True)

            for row in reader:
                new_team = Team(row[0], row[1])
                add_team_players(new_team)
                self.team_list.append(new_team)

        top_group = self.team_list[0:8]
        bottom_group = self.team_list[8:]

        for i in range(8):
            random_teams = random.sample(bottom_group, k=3)
            for team in random_teams:
                bottom_group.remove(team)

            team = random.choice(top_group)
            random_teams.append(team)
            top_group.remove(team)
            self.conferences.append(Conference(random_teams, i + 1))

    def get_all_players(self):
        player_list = []
        for team in self.team_list:
            for player in team.roster:
                player_list.append(player)
        return player_list
