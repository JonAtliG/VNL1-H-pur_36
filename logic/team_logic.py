from model.team import Team
from model.player import Player

class Team_Logic():
    def __init__(self, data_connection):
        '''Constructor for Team_Logic class.'''
        self.data_wrapper = data_connection
    
    def make_team_object(self, data, captain: Player , players: list):
        '''Takes in the team data and players, returns Team object'''
        team = Team()
        team.name = data[0]
        team.captain = captain
        team.players = players
        team.club = data[3]
        return team
    
    def get_all_team_data(self):
        '''Returns all team data'''
        return self.data_wrapper.get_all_team_data()
    
    def get_team_data_by_name(self, name):
        '''Returns the team data by name'''
        return self.data_wrapper.get_team_data_by_name(name)
    
    def make_team_captain(self, team: Team, player: Player) -> Team:
        '''Makes a player the captain of a team'''
        players = []
        for member in team.players:
            if member == player:
                team.captain = player
            else:
                players.append(member)
        return team
    
    def add_player_to_team(self, team: Team, player: Player) -> Team:
        '''Adds a player to a team'''
        if player.team == "No team":
            if team.players == "No players":
                team.players = [player]
            else:
                team.players.append(player)
            player.team = team.name
        return team, player
    
    def update_team(self,team):
        '''Takes in team object and forwards to data layer'''
        self.data_wrapper.update_team(team)
    
    def add_team(self, team):
        '''Takes in team object and forwards to data layer'''
        self.data_wrapper.add_team(team)