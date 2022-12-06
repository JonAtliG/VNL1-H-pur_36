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
host index      = 7
'''

class Player_Data():
    def __init__(self):
        self.file_name = "data/files/players.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def __create_player_data_from_object(self, player: Player) -> str:
        player_data = ";".join([player.name, player.nid, player.mail, player.birthdate, player.phone, player.address, player.team])
        if player.host:
            player_data += ";" + "True"
        else:
            player_data += ";" + "False"
        return player_data
    
    def __get_player_index_by_id(self, id: str) -> int:
        return self.__CSV_Handler.get_line_index_by_data(id, 1)     
 
    def get_player_data_by_id(self, id: str) -> list:
        return self.__CSV_Handler.get_data_by_data(id, 1)

    def get_all_player_data(self) -> list:
        return self.__CSV_Handler.get_all_data()
    
    def update_player(self, player: Player):
        index = self.__get_player_index_by_id(player.nid)
        player_data = self.__create_player_data_from_object(player)
        self.__CSV_Handler.replace_line(index, player_data)
    
    def add_player(self, player: Player):
       player_data = self.__create_player_data_from_object(player)
       self.__CSV_Handler.add_line(player_data)
