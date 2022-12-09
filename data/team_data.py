from data.CSV_Handler import CSV_Handler
from model.team import Team

'''
name index       = 0
captain id index = 1
members id index = 2
club name index  = 3
'''

class Team_Data():
    def __init__(self) -> None:
        self.file_name = "data/files/team_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def __create_team_data_from_object(self, team: Team):
        data = team.name + ";" + team.captain.nid + ";"
        data += ",".join([player.nid for player in team.players])
        data += ";" + team.club
        return data
    
    def __get_team_index_by_name(self, name: str) -> int:
        return self.__CSV_Handler.get_line_index_by_data(name, 0)
    
    def get_team_data_not_in_club(self) -> list:
        '''Returns all team data for teams not in a club'''
        return self.__CSV_Handler.get_all_data_by_data_in_data("No club", 3)

    def get_all_team_data(self) -> list:
        return self.__CSV_Handler.get_all_data()
                
    def get_team_data_by_name(self, name: str) -> list:
        return self.__CSV_Handler.get_data_by_data(name, 0)
    
    def update_team(self, team: Team) -> None:
        team_data = self.__create_team_data_from_object(team)
        team_index = self.__get_team_index_by_name(team.name)
        self.__CSV_Handler.replace_line(team_index, team_data)
    
    def add_team(self, team: Team) -> None:
        team_data = self.__create_team_data_from_object(team)
        self.__CSV_Handler.add_line(team_data)