from model.match import Match
from model.team import Team

class Match_Logic():
    def __init__(self, data_connection) -> None:
        '''Constructor for Match_Logic class.'''
        self.__data_wrapper = data_connection
    
    def __get_int_list_of_all_ids(self):
        '''Returns a list of all the match IDs as integers.'''
        return [int(id) for id in self.__data_wrapper.get_all_match_ids()]
    
    def __create_unique_id(self):
        '''Returns a unique ID for a new match.'''
        currentids = self.__get_int_list_of_all_ids()
        if len(currentids) > 0:
            new_id = max(currentids) + 1
        else:
            new_id = 1
        return new_id
    
    def get_match_data_by_id(self, id):
        '''Returns the match data for a match with a given ID.'''
        return self.__data_wrapper.get_match_data_by_id(id)
    
    def create_match_object(self, data, home_team: Team, away_team: Team, games: list) -> Match:
        '''Takes in the match data and teams, returns Match object'''
        match_object = Match()
        match_object.id = data[0]
        match_object.home_team = home_team
        match_object.away_team = away_team
        match_object.games = games
        match_object.date = data[4]
        return match_object
    
    def give_match_list_ids(self, matches: list) -> list:
        '''Gives all matches in a list a unique ID.'''
        id = self.__create_unique_id()
        matches_with_ids = []
        for match in matches:
            match.id = id
            matches_with_ids.append(match)
            id += 1
        return matches_with_ids

    def give_match_id(self, match: Match) -> Match:
        '''Gives a match a unique ID.'''
        id = self.__create_unique_id()
        match.id = id
        return match
    
    def add_match(self, match: Match) -> None:
        '''Adds a match to the database.'''
        self.__data_wrapper.add_match(match)
    
    def update_match(self, match: Match) -> None:
        '''Updates a match in the database.'''
        self.__data_wrapper.update_match(match)
