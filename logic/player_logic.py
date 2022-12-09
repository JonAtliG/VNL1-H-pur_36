from model.player import Player

class Player_Logic():
    def __init__(self, data_connection):
        '''Constructor for Player_Logic class.'''
        self.__data_wrapper = data_connection
    
    def create_player_object_with_data(self, data: list) -> Player:
        '''Recieves data and returns Player object'''
        player = Player(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        return player
    
    def is_valid_id(self, id) -> bool:
        '''Returns True if id is valid, False if not'''
        return self.__data_wrapper.is_valid_player_id(id)
    
    def get_player_by_id(self, id):
        '''Returns Player object of the player with the given id'''
        return self.create_player_object_with_data(self.__data_wrapper.get_player_data_by_id(id))
    
    def get_all_players(self):
        '''Returns list of Player objects for every player in the data layer'''
        return [self.create_player_object_with_data(data) for data in self.__data_wrapper.get_all_player_data()]
    
    def update_player(self, player: Player) -> None:
        '''Takes in player object and forwards to data layer'''
        self.__data_wrapper.update_player(player)
    
    def add_player(self, player: Player) -> None:
        '''Takes in player object and forwards to data layer'''
        self.__data_wrapper.add_player(player)
    
