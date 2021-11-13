import random
from League import \
    save_league, load_league


def print_menu():
    print("--------------------\nMenu\n--------------------\n")
    print("1 - Start New League")
    print("2 - Schedule")
    print("3 - Standings")
    print("4 - Play Game")
    print("5 - Team Stats")
    print("6 - Edit Roster")
    print("7 - Quit")
    return int(input(""))


def display_offenses(all_teams):
    print("-----------------------")
    print("Team\t\t\tW\tL")
    print("-----------------------")

    sorted_teams = sorted(all_teams, key=lambda x: (-x.calculate_ppg()))
    for team in sorted_teams:
        print('{0:15} {1:3.2f}'.format(team.college, team.calculate_ppg()))


def display_defenses(all_teams):
    print("-----------------------")
    print("Team\t\t\tW\tL")
    print("-----------------------")

    sorted_teams = sorted(all_teams, key=lambda x: (x.calculate_oppg()))
    for team in sorted_teams:
        print('{0:15} {1:3.2f}'.format(team.college, team.calculate_oppg()))


def show_roster(active_team):
    print(f"\n{active_team.college} {active_team.nickname}' Roster:")
    n = 0
    for athlete in active_team.roster:
        print(f"{n} - {athlete.display_name()}")
        n += 1


def edit_player(active_team, val):
    player_to_edit = active_team.roster[val]
    player_name = input("Enter player's new name: ")
    if player_name == '0':
        active_team.roster.remove(player_to_edit)
    else:
        name = player_name.split(', ')
        player_to_edit.edit_name(name[0], name[1])
    print()


def edit_roster(active_team):
    done = False
    while not done:
        show_roster(active_team)
        player_name = input("Player's Name or Press q to quit: ")
        try:
            val = int(player_name)
            if val < len(active_team.roster):
                edit_player(active_team, val)
            else:
                print("That player is not on the roster")
        except ValueError:
            if player_name == 'q' or player_name == 'Q':
                done = True
            elif active_team.is_player_on_roster(player_name):
                print("That player is already on the roster")
            else:
                name = player_name.split(', ')
                active_team.add_player_to_roster(name[0], name[1])


if __name__ == "__main__":
    ncaa = load_league()

    menu_choice = 0

    while menu_choice != 7:
        menu_choice = print_menu()
        if menu_choice == 1:
            ncaa.start_a_new_league("team_list.csv")
        elif menu_choice == 2:
            for group in ncaa.conferences:
                group.display_schedule()
                print("\n\n")
        elif menu_choice == 3:
            for group in ncaa.conferences:
                group.display_standings()
                print("\n\n")
        elif menu_choice == 4:
            input_choice = "Y"
            while input_choice == "Y":
                activeLeague = random.choice(ncaa.conferences)
                activeLeague.play_next_game()
                print("\n")
                input_choice = str.capitalize(input("Play another game? "))
        elif menu_choice == 5:
            input_choice = input("Sort teams by offense (O) or defense (D)").upper()
            if input_choice == 'O':
                display_offenses(ncaa.team_list)
            elif input_choice == 'D':
                display_defenses(ncaa.team_list)
            else:
                print("Not a valid selection -- ")
        elif menu_choice == 6:
            counter = 0
            for college in ncaa.team_list:
                print(f"{counter} - {college.college} {college.nickname}")
                counter += 1
            team_choice = int(input("Please choose the number of the team you would like to edit: "))
            if team_choice < len(ncaa.team_list):
                team_to_edit = ncaa.team_list[team_choice]
                edit_roster(team_to_edit)
            else:
                print("That choice is out of range!\n")
        elif menu_choice == 7:
            pass
        else:
            print("Not a viable choice")

    save_league(ncaa)
