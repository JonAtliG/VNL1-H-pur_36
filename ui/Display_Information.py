from model.league import League
from model.match import Match
from model.game import Game

class Display_Information():
    def __init__(self, logic_connection) -> None:
        '''Constructor for DisplayAll class.'''
        self.logic_wrapper = logic_connection

    def view_all(self):
        '''Displays all players, teams and clubs in the database.'''
        while True:
            print("_"*30)
            print("""
            1. View all players
            2. View all teams and their players
            3. View all clubs, their teams and all players in each team

            'q' Go back
            """)
            player_input = input("Enter option: ")
            if player_input == '1':
                self.display_all_players(self.logic_wrapper.get_all_players())
            elif player_input == '2':
                self.display_all_teams(self.logic_wrapper.get_all_teams())
            elif player_input == '3':
                self.display_all_clubs(self.logic_wrapper.get_all_clubs())
            elif player_input == 'q':
                return
    
    def display_player(self, player):
        '''Displays a player's name and ID.'''
        print(player)
    
    def display_all_players(self, players):
        '''Displays all players in the database.'''
        for player in players:
            print("Name:", player.name + ",", " ID:", player.nid)
            
    
    def display_team(self, team):
        '''Displays a team's name, captain and all players in the team.'''
        cap = team.captain
        print("\nTeam:", team.name)
        print("""
{}

    {}  {} {}""".format("Team Captain:", (cap.name + ","), "ID: ", cap.nid))
        print("\nMembers:\n")
        for player in team.players:
            print("    {}".format(player.name))
        print("_ "*18)
    
    def display_all_teams(self, teams):
        '''Displays all teams in the database.'''
        for team in teams:
            self.display_team(team)
    
    def display_club(self, club):
        '''Displays a club's name and all teams in the club.'''
        print("\nClub:", club.name)
        print("_"*30)
        if club.teams != "No teams":
            for team in club.teams:
                self.display_team(team)
    
    def display_all_clubs(self, clubs):
        '''Displays all clubs in the database.'''
        for club in clubs:
            self.display_club(club)

    def display_finished_matches(self, league: League):
        '''Displays all matches in a league that have been played.'''
        if league.matches == []:
            print("No matches have been played yet")
            return
        print(league.name)
        for match in league.matches:
            if match.games[0].played:
                print("-"*50)
                print(f"{match.home_team.name} vs. {match.away_team.name} | {match.date}")
                print()
                for game in match.games:
                    print(f"{game.home_players[0].name}".ljust(20), end = "")
                    print(f"{game.home_player_score} | {game.away_player_score}".ljust(9), end = "")
                    print(f"{game.away_players[0].name}".ljust(20),end = f"  Game Type: {game.game_type}\n")
                    for i in range(1, game.player_count):
                        print(f"{game.home_players[i].name}".ljust(20), end = "")
                        print(f"  | ".ljust(9), end = "")
                        print(f"{game.away_players[i].name}")
        input("Click enter to go back.")
        return
    

    def display_unfinished_matches(self, league: League):
        '''Displays all matches in a league that have not been played.'''
        if league.matches == []:
            input("There are no matches in the league, click enter to go back.")
            return
        for match in league.matches:
            if match.games[0].played == False:
                print("-"*50)
                print(f"{match.home_team.name} vs. {match.away_team.name} | {match.date}")
                print()
                for game in match.games:
                    if game.home_players == "No players":
                        home_players = ["No player", "No player", "No player", "No player"]
                    else:
                        home_players = [player.name for player in game.home_players]
                    if game.away_players == "No players":
                        away_players = ["No player", "No player", "No player", "No player"]
                    else:
                        away_players = [player.name for player in game.away_players]
                    print(f"{home_players[0]}".ljust(20), end = "")
                    print(f"{game.home_player_score} | {game.away_player_score}".ljust(9), end = "")
                    print(f"{away_players[0]}".ljust(20),end = f"  Game Type: {game.game_type}\n")
                    for i in range(1, game.player_count):
                        print(f"{home_players[i]}".ljust(20), end = "")
                        print(f"  | ".ljust(9), end = "")
                        print(f"{away_players[i]}")
            else:
                continue
        input("Click enter to go back.")
        return

    def display_leaderboard(self, league: League):
        '''Displays the leaderboard for a league.'''
        if league.matches == []:
            print("No matches have been played yet")
            return
        print(league.name)
        teams = [[team.name, 0, 0] for team in league.teams]
        teamnames = [team.name for team in league.teams]
        for match in league.matches:
            home = 0
            away = 0
            for game in match.games:
                if game.home_player_score > game.away_player_score:
                    home += 1
                elif game.home_player_score < game.away_player_score:
                    away += 1
            if home > away:
                teams[teamnames.index(match.home_team.name)][1] += 1
            elif home < away:
                teams[teamnames.index(match.away_team.name)][1] += 1
            
            teams[teamnames.index(match.home_team.name)][2] += home
            teams[teamnames.index(match.away_team.name)][2] += away
        
        teams.sort(key=lambda x: x[0])
        teams.sort(key=lambda x: (x[1], x[2]), reverse=True)
        print("Team | Wins | Points")
        print("--------------------")
        for team in teams:
            print(f"{team[0]} | {team[1]} | {team[2]}")

    def display_leagues(self) -> None:
        '''UI for user to see league information'''
        while True:
            leagues = self.logic_wrapper.get_all_leagues()
            c = 1
            print("_"*30)
            for league in leagues:
                print(f"{c}. {league.name}")
                c += 1
            league_choice = input("Select a league or go back (q): ")
            if league_choice == "q":
                return
            if self.logic_wrapper.validate_number(league_choice, c):
                print("_"*30)
                league = leagues[int(league_choice) - 1]
                host = self.logic_wrapper.get_host_by_league_name(league.name)
                while True:
                    print(f"League: {league.name} ({host.name})")
                    print("1. View finished matches")
                    print("2. View upcoming matches")
                    print("3. View leaderboard")
                    print('"q". Go back')
                    choice = input("Select an option: ")
                    if choice == "1":
                        self.display_finished_matches(league)
                    elif choice == "2":
                        self.display_unfinished_matches(league)
                    elif choice == "3":
                        self.display_leaderboard(league)
                    elif choice == "q":
                        break
                    else:
                        input("Invalid option, click enter to continue.")
            else:
                input("Invalid option, click enter to continue.")
