from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_Logic
from logic.admin_logic import Admin_Logic
from logic.team_logic import Team_Logic
from logic.league_logic import League_Logic
from logic.club_logic import Club_Logic


class Logic_Wrapper():
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.admin_logic = Admin_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
    
    def verify_admin_id(self, ID):
        return self.admin_logic.verify_ID(ID)
    
    def verify_admin_password(self, password):
        return self.admin_logic.verify_Password(password)
    
    def get_all_players(self):
        '''Fetches list of all players from player_logic and forwards to ui layer'''
        return self.player_logic.get_all_players()
        
    def create_leage(self):
        pass
    
    def create_club(self):
        pass
    
    def create_player(self, player):
        '''Recieves player from player_logic and forwards to data layer'''
        self.player_logic.create_player(player)
    
    def get_team_by_name(self, name):
        return self.team_logic.get_team_by_name(name)
    
