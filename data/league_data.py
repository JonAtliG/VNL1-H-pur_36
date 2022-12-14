from data.CSV_Handler import CSV_Handler
from model.league import League

class League_Data():
    def __init__(self) -> None:
        '''Constructor for League_Data class.'''
        self.file_name = "data/files/league_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)

    def __create_league_data_from_object(self, league: League):
        '''Takes in a league object and returns the league data as a string'''
        league_data = f"{league.name};"
        if league.teams == "No teams":
            league_data +="No teams;"
        else:
            league_data += ",".join([team.name for team in league.teams]) + ";"
        if league.matches == "No matches":
            league_data += "No matches;"
        else:
            league_data += ",".join([str(match.id) for match in league.matches]) + ";"
        league_data += f"{league.start_date};{league.end_date}"
        return league_data

    def __get_league_index_by_name(self, name: str):
        '''Fetches the league index for the name and returns it'''
        return self.__CSV_Handler.get_line_index_by_data(name, 0)
    
    def get_league_data_by_name(self, name: str) -> list:
        '''Fetches the league data for the name and returns it'''
        return self.__CSV_Handler.get_data_by_data(name, 0)
    
    def get_all_league_data_by_team_name(self, name: str) -> list:
        '''Fetches all league data for the team name and returns it'''
        return self.__CSV_Handler.get_all_data_by_data_in_data(name, 1)
    
    def get_all_league_data(self) -> list:
        '''Fetches all league data and returns it'''
        return self.__CSV_Handler.get_all_data()

    def update_league(self, league: League) -> None:
        '''Updates the league in the database'''
        index = self.__get_league_index_by_name(league.name)
        league_data = self.__create_league_data_from_object(league)
        self.__CSV_Handler.replace_line(index, league_data)

    def add_league(self, league: League) -> None:
        '''Adds a league to the database'''
        league_data = self.__create_league_data_from_object(league)
        self.__CSV_Handler.add_line(league_data)