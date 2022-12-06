from data.CSV_Handler import CSV_Handler
from model.league import League

class League_Data():
    def __init__(self) -> None:
        self.file_name = "data/files/league_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)

    def __create_league_data_from_object(self, league: League):
        pass

    def __get_league_index_by_id(self, id: str):
        return self.__CSV_Handler.get_line_index_by_data(id, 0)
    
    def get_league_data_by_name(self, name: str) -> list:
        return self.__CSV_Handler.get_data_by_data(name, 0)
    
    def get_all_league_data(self):
        return self.__CSV_Handler.get_all_data()

    def update_league(self, league: League) -> None:
        index = self.__get_league_index_by_id(league.id)
        league_data = self.__create_league_data_from_object(league)
        self.__CSV_Handler.replace_line(index, league_data)

    def add_league(self, league: League) -> None:
        league_data = self.__create_league_data_from_object(league)
        self.__CSV_Handler.add_line(league_data)