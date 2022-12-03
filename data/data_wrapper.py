from data.teams_in_tournament import Registered_Teams
from data.club_data import Club
from data.scores import Scores
from data.players import Player_Data

class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_Data()
        self.teams_in_tournament = Registered_Teams()
        self.club_data = Club()
        self.scores = Scores()

    def get_all_clubs(self):
        return self.club_data.get_all_clubs()

    def get_teams_by_club(self, club_name):
        return self.club_data.get_teams_by_club(club_name)

    def add_club(self, club_name, teams):
        return self.club_data.add_club(club_name, teams)
    
    def add_teams_to_club(self, club_name, teams):
        return self.club_data.add_teams_to_club(club_name, teams)
    
    def get_teams(self):
        return self.teams_in_tournament.get_teams()
    
    def add_team(self, team):
        return self.teams_in_tournament.add_team(team)
    
    def get_scores(self):
        return self.scores.get_scores()
    
    def add_score(self, game):
        return self.scores.add_score(game)
    
    def get_players():
        return Player_Data.get_players()
    
    def add_player(self, player):
        print("recieved in data wrapper")
        return self.player_data.add_player(player)
