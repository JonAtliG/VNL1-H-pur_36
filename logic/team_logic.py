from model.team import Team
from model.player import Player
class Team_Logic():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
    
    def make_team_object(self, data, captain: Player , players: list):
        team = Team()
        team.name = data[0]
        team.captain = captain
        team.players = players
        team.club = data[3]
        return team
    
    def get_all_team_data(self):
        return self.data_wrapper.get_all_team_data()
    
    def get_team_data_by_name(self, name):
        return self.data_wrapper.get_team_data_by_name(name)
    
    def update_team(self,team):
        self.data_wrapper.update_team(team)
    
    def add_team(self, team):
        '''Takes in team object and forwards to data layer'''
        self.data_wrapper.add_team(team)