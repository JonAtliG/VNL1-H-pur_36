from model.game import Game
from model.player import Player

class Game_Logic():
    def __init__(self, data_connection) -> None:
        self.__data_wrapper = data_connection
    
    def __get_int_list_of_all_ids(self):
        return [int(id) for id in self.data_wrapper.get_all_game_ids()]
    
    def __create_unique_id(self):
        currentids = self.__get_int_list_of_all_ids()
        if len(currentids) > 0:
            new_id = max(currentids) + 1
        else:
            new_id = 1
        return new_id
    
    def create_game_object(self, data, home_players: list, away_players: list):
        game = Game()
        game.id = data[0]
        game.home_players = home_players
        game.away_players = away_players
        game.home_player_score = int(data[3])
        game.away_player_score = int(data[4])
        game.game_type = data[5]
        game.player_count = int(data[6])
        if data[7] == "True":
            game.played = True
        else:
            game.played = False
        return game

    def give_game_list_ids(self, games: list) -> list:
        id = self.__create_unique_id()
        updated_games = []
        for game in games:
            game.id = id
            id += 1
            updated_games.append(game) # possibly not a needed list testing needed!
        return updated_games
    
    def give_game_id(self, game: Game) -> Game:
        game.id = self.__create_unique_id()
        return game
    
    def get_game_data_by_id(self, id):
        return self.__data_wrapper.get_game_data_by_id(id)
    
    def add_game(self, game: Game) -> str:
        self.__data_wrapper.add_game(game)
    
    def update_game(self, game: Game) -> None:
        self.__data_wrapper.update_game(game)
    