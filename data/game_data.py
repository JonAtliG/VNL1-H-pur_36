from data.CSV_Handler import CSV_Handler
from model.game import Game

class Game_Data():
    def __init__(self) -> None:
        self.file_name = "data/files/game_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def __create_game_data_from_object(self, game: Game):
        game_data = f"{game.id};"
        if game.home_players == "No players":
            game_data += "No players;"
        else:
            game_data += ",".join(player.nid for player in game.home_players) + ";"
        if game.away_players == "No players":
            game_data += "No players;"
        else:
            game_data += ",".join(player.nid for player in game.away_players) + ";"
        game_data += f"{game.home_player_score};{game.away_player_score};{game.game_type};{game.player_count};{game.played}"
        return game_data
    
    def __get_game_index_by_id(self, id: str):
        return self.__CSV_Handler.get_line_index_by_data(id, 0)
    
    def get_all_game_ids(self):
        return self.__CSV_Handler.get_all_data_by_column_index(0)
    
    def get_game_data_by_id(self, id):
        return self.__CSV_Handler.get_data_by_data(id, 0)
    
    def get_all_game_data(self):
        return self.__CSV_Handler.get_all_data()
    
    def update_game(self, game: Game) -> None:
        index = self.__get_game_index_by_id(str(game.id))
        game_data = self.__create_game_data_from_object(game)
        self.__CSV_Handler.replace_line(index, game_data)

    def add_game(self, game: Game) -> None:
        game_data = self.__create_game_data_from_object(game)
        self.__CSV_Handler.add_line(game_data)
