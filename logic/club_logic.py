from model.club import Club
from model.team import Team

class Club_Logic():
    def __init__(self, data_connection) -> None:
        '''Constructor for Club_Logic class.'''
        self.data_wrapper = data_connection
    
    def make_club_object(self, club_data, teams: list) -> Club:
        '''Takes in the club data and teams, returns Club object'''
        club = Club()
        club.name = club_data[0]
        club.teams = teams
        club.address = club_data[2]
        club.phone = club_data[3]
        return club
    
    def add_team_to_club(self, club: Club, team: Team):
        '''Adds a team to a club'''
        if club.teams == "No Teams":
            club.teams = [team]
        else:
            club.teams.append(team)
        return club
    
    def get_club_data_by_name(self, name: str) -> list:
        '''Returns the club data by name'''
        return self.data_wrapper.get_club_data_by_name(name)
    
    def get_all_club_data(self) -> list:
        '''Returns all club data'''
        return self.data_wrapper.get_all_club_data()
    
    def update_club(self, club: Club) -> None:
        '''Updates the club in the database'''
        self.data_wrapper.update_club(club)
    
    def add_club(self, club: Club) -> None:
        '''Adds a club to the database'''
        self.data_wrapper.add_club(club)