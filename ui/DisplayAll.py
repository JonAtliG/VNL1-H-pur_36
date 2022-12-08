from model.league import League
from model.match import Match
from model.game import Game

class DisplayAll():
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def view_all(self):
        while True:
            print("""
            1. View all players
            2. View all teams and their players
            3. View all clubs, their teams and all players in each team

            'q' Logout
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
        print(player)
    
    def display_all_players(self, players):
        for player in players:
            print("Name:", player.name + ",", " ID:", player.nid)
            
    
    def display_team(self, team):
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
        for team in teams:
            self.display_team(team)
    
    def display_club(self, club):
        print("\nClub:", club.name)
        print("_"*30)
        for team in club.teams:
            self.display_team(team)
    
    def display_all_clubs(self, clubs):
        for club in clubs:
            self.display_club(club)
# match = Match()
# match.home_team
# match.away_team
# match.date
# match.games :list
#
#game = Game()
#game.home_player
#game.away_player
#game.home_player_score
#game.away_player_score
#game.played

    def display_finished_matches(self, league: League):
        if league.matches == []:
            print("No matches have been played yet")
            return
        print(league.name)
        for match in league.matches:
            print(f"{match.home_team.name} --- {match.away_team.name} | {match.date}")
            for game in match.games:
                if game.played == True:
                    print(f"{','.join(player.name for player in game.home_players)} ({game.home_player_score}) | {','.join(player.name for player in game.away_players)} ({game.away_player_score})")
    

    def display_unfinished_matches(self, league: League):
        if league.matches == []:
            print("No matches have been played yet")
            return
        print(league.name)
        for match in league.matches:
            print(f"{match.home_team.name} --- {match.away_team.name} | {match.date}")
            for game in match.games:
                if game.played == False:
                    print(f"{','.join(player.name for player in game.home_players)} ({game.home_player_score}) | {','.join(player.name for player in game.away_players)} ({game.away_player_score})")
    

    def display_leaderboard(self, league: League):
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
