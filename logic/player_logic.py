from model.player import Player

class Player_Logic():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
    
    def get_all_players(self):
        '''Fetches list of players from data layer and forwards to logic_wrapper'''
        return self.data_wrapper.get_players()
    
    def create_player(self, player):
        '''Takes in player object and forwards to data layer'''
        print("recieved in player_logic")
        self.data_wrapper.add_player(player)
    
