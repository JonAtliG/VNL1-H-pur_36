from model.player import Player
from data.CSV_Handler import CSV_Handler

'''
name index      = 0
nid index       = 1
mail index      = 2
birthdate index = 3
phone index     = 4
address index   = 5
team index      = 6
'''

class Player_Data():
    def __init__(self):
        '''Constructor for Player_Data class.'''
        self.file_name = "data/files/player_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def __create_player_data_from_object(self, player: Player) -> str:
        '''Takes in a player object and returns the player data as a string'''
        player_data = ";".join([player.name, player.nid, player.mail, player.birthdate, player.phone, player.address, player.team])
        return player_data
    
    def __get_player_index_by_id(self, id: str) -> int:
        '''Fetches the player index for the id and returns it'''
        return self.__CSV_Handler.get_line_index_by_data(id, 1)
    
    def is_valid_id(self, id):
        '''Checks if the id is valid'''
        try:
            self.get_player_data_by_id(id)
            return True
        except:
            return False
 
    def get_player_data_by_id(self, id: str) -> list:
        '''Fetches the player data for the id and returns it'''
        return self.__CSV_Handler.get_data_by_data(id, 1)

    def get_all_player_data(self) -> list:
        '''Fetches all player data and returns it'''
        return self.__CSV_Handler.get_all_data()
    
    def update_player(self, player: Player):
        '''Updates the player in the database'''
        index = self.__get_player_index_by_id(player.nid)
        player_data = self.__create_player_data_from_object(player)
        self.__CSV_Handler.replace_line(index, player_data)
    
    def add_player(self, player: Player):
        '''Adds a player to the database'''
        player_data = self.__create_player_data_from_object(player)
        self.__CSV_Handler.add_line(player_data)
