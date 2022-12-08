from data.CSV_Handler import CSV_Handler
from model.match import Match

class Match_Data():
    def __init__(self) -> None:
        self.file_name = "data/files/match_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def __create_match_data_from_object(self, match: Match):
        return f"{match.id};{match.home_team.name};{match.away_team.name};{','.join([game.id for game in match.games])};{match.date}"
    
    def __get_match_index_by_id(self, id: str):
        return self.__CSV_Handler.get_line_index_by_data(id, 0)
    
    def get_all_match_ids(self):
        return self.__CSV_Handler.get_all_data_by_column_index(0)
    
    def get_all_match_data(self) -> list:
        return self.__CSV_Handler.get_all_data()
    
    def get_match_data_by_id(self, id: str):
        return self.__CSV_Handler.get_data_by_data(id, 0)
    
    def update_match(self, match: Match) -> None:
        index = self.__get_match_index_by_id(match.id)
        match_data = self.__create_match_data_from_object(match)
        self.__CSV_Handler.replace_line(index, match_data)
        
    def add_match(self, match: Match) -> None:
        match_data = self.__create_match_data_from_object(match)
        self.__CSV_Handler.add_line(match_data)
