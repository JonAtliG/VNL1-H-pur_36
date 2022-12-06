from data.CSV_Handler import CSV_Handler
from model.game import Game

class Game_Data():
    def __init__(self) -> None:
        self.file_name = "data/files/game_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def __create_game_data_from_object(self, game: Game):
        pass
    
    def __get_game_index_by_id(self, id: str):
        return self.__CSV_Handler.get_line_index_by_data(id, 0)
    
    def update_game(self, game: Game) -> None:
        index = self.__get_game_index_by_id(game.id)
        game_data = self.__create_game_data_from_object(game)
        self.__CSV_Handler.replace_line(index, game_data)

    def add_game(self, game: Game) -> None:
        game_data = self.__create_game_data_from_object(game)
        self.__CSV_Handler.add_line(game_data)
