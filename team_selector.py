from random import shuffle, choice

print("""
    Welcome to Team Allocator!
    Don't forget to assign the numbers to the players!
""")


def allocate():
    """ allocates players to as many teams as you need """
    num_of_players = int(input("How many players are there? "))
    num_of_teams = int(input("How many teams do you need? "))
    players_list = []
    teams = []
    for i in range(1, num_of_players + 1):
        players_list.append(i)
    shuffle(players_list)
    while len(players_list) >= num_of_players // num_of_teams:
        teams.append(players_list[:num_of_players // num_of_teams])
        del(players_list[:num_of_players // num_of_teams])
        if len(players_list) < num_of_players // num_of_teams and len(players_list) != 0:
            teams.append(players_list)
    return teams


allocated_players = allocate()


def show_teams():
    """ print each team on single line (as a list of numbers) """
    for number in range(1, len(allocated_players) +1):
        print(f'team {number}: {allocated_players[number - 1]}')


player_names = {
    1: "Boss", 2: "Tom", 3: "Erik", 4: "Sam", 5: "Andy", 6: "Meilin", 7: "Jiamin", 8: "Yen"
    }


def show_names():
    """ show names of players assigned in dictionary above """
    for team in allocated_players:
        for player in team:
            for player_number, player_name in player_names.items():
                if player == player_number:
                    team.append(player_name)
        print(team[len(team)//2:])


show_teams()
show_names()