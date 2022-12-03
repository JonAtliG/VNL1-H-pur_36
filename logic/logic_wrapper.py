from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_Logic
from logic.team_logic import Team_Logic
from logic.league_logic import League_Logic
from logic.club_logic import Club_Logic


class Logic_Wrapper():
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        
    def get_all_players(self):
        '''Returns dictonary of all players'''
        pass
        
    def create_leage(self):
        pass
        
    def create_team(self):
        pass
    
    def create_club(self):
        pass
    
    def create_player(self, player):
        '''Recieves player from player_logic and forwards to data layer'''
        self.player_logic.create_player(player)
    
