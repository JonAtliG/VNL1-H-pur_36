from data.CSV_Handler import CSV_Handler
from model.club import Club

'''
name index    = 0
teams index   = 1
address index = 2
phone index   = 3
'''

class Club_Data():
    def __init__(self) -> None:
        '''Constructor for Club_Data class.'''
        self.file_name = "data/files/club_data.csv"
        self.__CSV_Handler = CSV_Handler(self.file_name)
    
    def __create_club_data_from_object(self, club: Club) -> str:
        '''Takes in a club object and returns the club data as a string'''
        line = club.name + ";"
        if club.teams == "No teams":
            line += "No teams;"
        else:
            line += ",".join([team_name for team_name in [team.name for team in club.teams]]) + ";"
        line += club.address + ";" + club.phone
        return line
    
    def __get_club_index_by_name(self, name: str) -> int:
        '''Fetches the club index for the name and returns it'''
        return self.__CSV_Handler.get_line_index_by_data(name, 0)
    
    def get_club_data_by_name(self, name: str) -> list:
        '''Fetches the club data for the name and returns it'''
        return self.__CSV_Handler.get_data_by_data(name, 0)
    
    def get_all_club_data(self) -> list:
        '''Fetches all club data and returns it'''
        return self.__CSV_Handler.get_all_data()
    
    def update_club(self, club: Club) -> None:
        '''Updates the club in the database'''
        index = self.__get_club_index_by_name(club.name)
        club_data = self.__create_club_data_from_object(club)
        self.__CSV_Handler.replace_line(index, club_data)
        
    def add_club(self, club: Club) -> None:
        '''Adds a club to the database'''
        club_data = self.__create_club_data_from_object(club)
        self.__CSV_Handler.add_line(club_data)