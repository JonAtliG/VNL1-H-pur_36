from data.admin_data import Admin_Data
from data.club_data import Club_Data
from data.teams_data import Team_Data
from data.player_data import Player_Data
from data.league_data import League_Data
from data.match_data import Match_Data
from data.game_data import Game_Data
from data.teams_in_tournament import Registered_Teams
from data.scores import Scores

class Data_Wrapper:
    def __init__(self):
        self.admin_data = Admin_Data()
        self.club_data = Club_Data()
        self.team_data = Team_Data()
        self.player_data = Player_Data()
        self.teams_in_tournament = Registered_Teams()
        self.scores = Scores()
   
   ### Admin data 
    def get_admin_id(self):
        return self.admin_data.get_ID()
    
    def get_admin_password(self):
        return self.admin_data.get_password()
    
    ### Club data
    def get_club_data_by_name(self, name: str) -> list:
        return self.club_data.get_club_data_by_name(name)
    
    def get_all_club_data(self) -> list:
        return self.club_data.get_all_club_data()
    
    def update_club(self, club):
        self.club_data.update_club(club)
    
    def add_club(self, club):
        self.club_data.add_club(club)
    
    
    ### Team data
    def get_teams(self):
        return self.teams_in_tournament.get_teams()
    
    def get_team_data_by_name(self, name):
        return self.team_data.get_team_data_by_name(name)
    
    def get_all_team_data(self):
        return self.team_data.get_all_team_data()
    
    def update_team(self, team) -> None:
        self.team_data.update_team(team)
    
    def add_team(self, team) -> None:
        self.team_data.add_team(team)
    
    ### Player data
    def get_all_player_data(self):
        return self.player_data.get_all_player_data()
    
    def get_player_data_by_id(self, id):
        return self.player_data.get_player_data_by_id(id)
    
    def update_player(self, player):
        self.player_data.update_player(player)
        
    def add_player(self, player):
        self.player_data.add_player(player)
    
    def get_scores(self):
        return self.scores.get_scores()
    
    def add_score(self, game):
        return self.scores.add_score(game)