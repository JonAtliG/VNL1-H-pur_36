from data.admin_data import Admin_Data
from data.host_data import Host_Data
from data.club_data import Club_Data
from data.team_data import Team_Data
from data.player_data import Player_Data
from data.league_data import League_Data
from data.match_data import Match_Data
from data.game_data import Game_Data
from data.teams_in_tournament import Registered_Teams
from data.scores import Scores

class Data_Wrapper:
    def __init__(self):
        self.admin_data = Admin_Data()
        self.host_data = Host_Data()
        self.club_data = Club_Data()
        self.team_data = Team_Data()
        self.player_data = Player_Data()
        self.teams_in_tournament = Registered_Teams()
        self.scores = Scores()
        self.leage_data = League_Data()
        self.match_data = Match_Data()
        self.game_data = Game_Data()
   
   ### Admin data 
    def get_admin_id(self):
        return self.admin_data.get_ID()
    
    def get_admin_password(self):
        return self.admin_data.get_password()
    
    ### Host data
    def verify_host_id(self, id):
        return self.host_data.verify_id(id)
    
    def get_host_data_by_id(self, id):
        return self.host_data.get_host_data_by_id(id)
    
    def get_host_data_by_league_name(self, name):
        return self.host_data.get_host_data_by_league_name(name)
    
    def add_host(self, host):
        self.host_data.add_host(host)
    
    def update_host(self, host):
        self.host_data.update_host(host)
    
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
    
    ### League Data
    def get_league_data_by_name(self, name) -> list:
        return self.leage_data.get_league_data_by_name(name)
    
    def get_all_league_data(self) -> list:
        return self.leage_data.get_all_league_data()
    
    def add_league(self, league) -> None:
        self.leage_data.add_league(league)
    
    def update_league(self, league) -> None:
        self.leage_data.update_league(league)
    
    ### Match Data
    def get_match_data_by_id(self, id) -> list:
        return self.match_data.get_match_data_by_id(id)
    
    def get_all_match_data_by_league_name(self, name) -> list:
        league_data = self.get_league_data_by_name(name)
        match_data = []
        for match_id in league_data[2].split(","):
            match_data.append(self.get_match_data_by_id(match_id))
        return match_data

    def get_all_match_data(self) -> list:
        return self.match_data.get_all_match_data()

    def get_all_match_ids(self) -> list:
        return self.match_data.get_all_match_ids()
    
    def add_match(self, match):
        self.match_data.add_match(match)
    
    def update_match(self, match):
        self.match_data.update_match(match)
    
    ### Game Data
    def get_all_game_ids(self):
        return self.game_data.get_all_game_ids()
    
    def get_game_data_by_id(self, id):
        return self.game_data.get_game_data_by_id(id)
    
    def get_all_game_data_by_match_id(self, id):
        match_data = self.get_match_data_by_id(id)
        return [self.get_game_data_by_id(id) for id in match_data[3].split(",")]
    
    def get_all_game_data(self):
        return self.game_data.get_all_game_data()
    
    def add_game(self, game):
        self.game_data.add_game(game)
    
    def update_game(self, game):
        self.game_data.update_game(game)
    