from model.team import Team

class Team_Logic():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
    
    def make_team_object(self, data):
        team = Team()
        team.name = data[0]
        team.captain = self.data_wrapper.get_player_by_id(data[1])
        team.players = [self.data_wrapper.get_player_by_id(id) for id in data[2].split(",")]
        team.club = data[3]
        return team
    
    def get_team_by_name(self, name):
        return self.make_team_object(self.data_wrapper.get_team_data_by_name(name))
    
    def create_team(self, team):
        '''Takes in team object and forwards to data layer'''
        pass