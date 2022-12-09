from model.league import League

class League_Logic():
    def __init__(self, data_connection) -> None:
        self.__data_wrapper = data_connection
    
    def get_all_league_data_by_team_name(self, name: str) -> list:
        return self.__data_wrapper.get_all_league_data_by_team_name(name)
    
    def get_league_data_by_name(self, name) -> list:
        return self.__data_wrapper.get_league_data_by_name(name)
    
    def get_all_league_data(self) -> list:
        return self.__data_wrapper.get_all_league_data()
    
    def create_league_object(self, data, teams: list, matches: list):
        league = League()
        league.name = data[0]
        league.teams = teams
        league.matches = matches
        league.start_date = data[3]
        league.end_date = data[4]
        return league
    
    def add_leage(self, league: League) -> None:
        self.__data_wrapper.add_league(league)
    
    def update_league(self, league: League) -> None:
        self.__data_wrapper.update_league(league)
